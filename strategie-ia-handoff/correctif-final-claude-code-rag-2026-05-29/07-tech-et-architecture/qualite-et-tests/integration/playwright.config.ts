/**
 * playwright.config.ts — configuration Playwright pour les tests d'intégration UI.
 *
 * Périmètre : tests d'intégration des composants front 06/produit-app/composants/*
 * et site-public/*. Exclut explicitement les tests pipeline RAG (qui vivent en
 * 09/tests/ avec pytest, owner Hub RAG côté workflow CI distinct).
 *
 * Auteur          : Cowork Hub IA Plateforme (Claude Code RAG)
 * Date            : 2026-05-29
 * Owner           : 07-tech-et-architecture/qualite-et-tests
 * Confidentialite : public
 * Statut          : valide (smoke test V1 - extension a venir avec tests composants conversation)
 */

import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: process.env.CI ? [['github'], ['html', { open: 'never' }]] : 'list',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    // Mobile / Firefox / Webkit ajoutables en Vague C contributions (~06-22).
  ],
  webServer: {
    // Sert le dossier composants/journey/ comme racine.
    // Chemin relatif depuis 07/qualite-et-tests/integration/ vers le composant.
    command: 'npx http-server ../../../../06-produit-et-site/produit-app/composants/journey -p 3000 --silent',
    url: 'http://localhost:3000/journey-example.html',
    reuseExistingServer: !process.env.CI,
    timeout: 30 * 1000,
  },
});
