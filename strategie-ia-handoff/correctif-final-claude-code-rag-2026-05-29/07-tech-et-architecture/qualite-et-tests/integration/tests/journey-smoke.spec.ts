/**
 * journey-smoke.spec.ts — smoke test du composant JOURNEY adapte (06/produit-app/composants/journey).
 *
 * Valide la portabilite technique de la migration §2.1 (hub-ia/css|js/journey.* -> strategie-ia/06)
 * apres le fork content-agnostic + adaptation tokens v2.2 placeholders + injection config externe.
 *
 * Cible exclusive : journey-example.html livre Bundle Vague C #1 par Claude Code Content.
 * Tests = 7 verifications fonctionnelles (pas de pixel-perfect, pas de visual regression -
 * compatible avec le fallback style-agnostic si maquettes Claude Design indispos).
 *
 * Auteur          : Cowork Hub IA Plateforme (Claude Code RAG)
 * Date            : 2026-05-29
 * Owner           : 07-tech-et-architecture/qualite-et-tests/integration
 * Confidentialite : public
 * Statut          : valide
 * Reference       : Brief de scope Vague C 2026-05-28 §2.1 + Reponse RAG amendement #5 + Bundle #1 2026-05-29
 */

import { test, expect } from '@playwright/test';

test.describe('JOURNEY composant — smoke test post-§2.1 migration content-agnostic', () => {
  test('page charge sans erreur console + titre present', async ({ page }) => {
    const consoleErrors: string[] = [];
    page.on('console', msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });
    page.on('pageerror', err => consoleErrors.push(err.message));

    await page.goto('/journey-example.html');
    await expect(page).toHaveTitle(/Stratégie IA/);
    expect(consoleErrors).toEqual([]);
  });

  test('6 sous-composants visibles dans le DOM (fil ariane / itinerary / starter / bridge / modules / next-step)', async ({ page }) => {
    await page.goto('/journey-example.html');

    // SC1 — fil d'Ariane sticky
    await expect(page.locator('.journey')).toBeVisible();
    // SC2 — carte d'itineraire
    await expect(page.locator('.itinerary')).toBeVisible();
    // SC3 — wizard starter
    await expect(page.locator('.starter')).toBeVisible();
    // SC4 — bridges narratifs
    await expect(page.locator('.bridge')).toBeVisible();
    // SC5 — badges progression
    await expect(page.locator('.modules-section')).toBeVisible();
    // SC6 — next-step
    await expect(page.locator('.next-step')).toBeVisible();
  });

  test('fil ariane : 5 stations + "Conversation" current (placeholder)', async ({ page }) => {
    await page.goto('/journey-example.html');
    const steps = page.locator('.journey-step');
    await expect(steps).toHaveCount(5);
    // is-current sur step 2 (placeholder station "Conversation")
    await expect(page.locator('.journey-step.is-current .journey-step-label')).toHaveText('Conversation');
  });

  test('wizard happy path : profil dirigeant + objectif decider -> 3 recommandations rendues', async ({ page }) => {
    await page.goto('/journey-example.html');

    await page.click('[data-profil="dirigeant-pme"]');
    await page.click('[data-objectif="decider"]');

    // 3 recommandations attendues d'apres STRATEGIE_IA_JOURNEY_CONFIG.starter.library
    await expect(page.locator('.starter-recs > *')).toHaveCount(3);
    await expect(page.locator('.starter-results-title')).not.toBeEmpty();
  });

  test('localStorage ecrit sur clic card avec prefixe strategie-ia_ (pas hubia_)', async ({ page }) => {
    await page.goto('/journey-example.html');

    await page.click('.card[data-module="outil-compare"]');

    const stored = await page.evaluate(() =>
      localStorage.getItem('strategie-ia_outil-compare')
    );
    expect(stored).not.toBeNull();
    const parsed = JSON.parse(stored as string);
    expect(parsed.completed).toBe(true);

    // Confirmation absence prefixe hub-ia (regression test cle de l'adaptation §2.1)
    const hubiaKey = await page.evaluate(() =>
      localStorage.getItem('hubia_outil-compare')
    );
    expect(hubiaKey).toBeNull();
  });

  test('API publique window.StrategieIAJourney exposee avec init/refreshBadges/readCompleted', async ({ page }) => {
    await page.goto('/journey-example.html');

    const apiSurface = await page.evaluate(() => {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const api = (window as any).StrategieIAJourney;
      if (!api) return null;
      return {
        hasInit: typeof api.init === 'function',
        hasRefreshBadges: typeof api.refreshBadges === 'function',
        hasReadCompleted: typeof api.readCompleted === 'function',
      };
    });

    expect(apiSurface).not.toBeNull();
    expect(apiSurface).toMatchObject({
      hasInit: true,
      hasRefreshBadges: true,
      hasReadCompleted: true,
    });
  });

  test('badge progression : 1/5 complete apres clic card + refreshBadges', async ({ page }) => {
    await page.goto('/journey-example.html');

    await page.click('.card[data-module="outil-compare"]');
    await page.evaluate(() => {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      (window as any).StrategieIAJourney.refreshBadges();
    });

    const countText = await page.locator(
      '[data-progress-section="outils-pro"] .section-progress-count strong'
    ).textContent();
    expect(countText).toBe('1');
  });
});
