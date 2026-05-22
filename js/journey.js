/* ============================================================
   Hub IA — JOURNEY layer JS
   Additif : Wizard "Par où commencer" + badges progression
   ============================================================ */

(function () {
  'use strict';

  // ----------------------------------------------------------
  // 1. Progression dans le fil d'Ariane
  // ----------------------------------------------------------
  function setupJourneyRail() {
    const track = document.querySelector('.journey-track');
    if (!track) return;
    const steps = [...track.querySelectorAll('.journey-step')];
    const currentIndex = steps.findIndex(s => s.classList.contains('is-current'));
    if (currentIndex < 0) return;
    // Position la barre de progression (0%, 25%, 50%, 75%, 100%)
    const progress = (currentIndex / (steps.length - 1)) * 80;
    track.style.setProperty('--journey-progress', progress + '%');

    // Marque comme is-done les étapes avant la courante
    steps.forEach((s, i) => {
      if (i < currentIndex) s.classList.add('is-done');
    });
  }

  // ----------------------------------------------------------
  // 2. Badges de progression — lit le localStorage des quizs
  //    Format clé : hubia_<module-id> = {completed: true, score, total, date}
  // ----------------------------------------------------------
  function readCompletedModules() {
    const out = new Set();
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (!key || !key.startsWith('hubia_') || key === 'hubia_filters') continue;
      try {
        const val = JSON.parse(localStorage.getItem(key));
        if (val && val.completed) {
          out.add(key.replace('hubia_', ''));
        }
      } catch (e) { /* ignore */ }
    }
    return out;
  }

  function updateProgressBadges() {
    const completed = readCompletedModules();

    // Badges par section
    document.querySelectorAll('[data-progress-section]').forEach(badge => {
      const section = badge.dataset.progressSection;
      const cards = document.querySelectorAll(`.modules-section[data-section="${section}"] .card[data-module]`);
      if (!cards.length) return;
      let done = 0;
      cards.forEach(card => { if (completed.has(card.dataset.module)) done++; });
      const total = cards.length;
      const pct = total === 0 ? 0 : (done / total) * 100;
      badge.querySelector('.section-progress-count').innerHTML =
        `<strong>${done}</strong>/${total} complété${total > 1 ? 's' : ''}`;
      const fill = badge.querySelector('.section-progress-fill');
      if (fill) fill.style.setProperty('--p', pct + '%');
      badge.classList.toggle('is-empty', done === 0);
    });

    // Compteur global (dans le pill du fil d'Ariane si présent)
    const globalPill = document.querySelector('.journey-progress-pill');
    if (globalPill) {
      const total = document.querySelectorAll('.card[data-module]').length || 27;
      globalPill.querySelector('.journey-progress-count').innerHTML =
        `<strong>${completed.size}</strong>/${total} modules`;
    }

    // Marque visuellement les cards complétées (cohérence avec le code existant)
    document.querySelectorAll('.card[data-module]').forEach(card => {
      if (completed.has(card.dataset.module)) {
        card.classList.add('is-done');
      }
    });
  }

  // ----------------------------------------------------------
  // 3. Wizard « Par où commencer ? »
  //    2 questions → recommandation de 3 modules
  // ----------------------------------------------------------
  const STARTER_LIBRARY = {
    // [stage][axis] = array de modules { id, name, reason, axe, niveau, href }
    decouverte: {
      productivite: [
        { id: 'cu-001', name: 'Recherche & veille augmentée', reason: 'Le réflexe IA le plus rentable à acquérir — 0 € et 15 min pour démarrer.', href: 'modules/cu-001-recherche-veille.html' },
        { id: 'cu-002', name: 'Assistant rédactionnel', reason: 'Premier ROI tangible pour tout dirigeant : mails, notes, premiers jets.', href: 'modules/cu-002-assistant-redactionnel.html' },
        { id: 'cu-003', name: 'Comptes-rendus de réunion', reason: 'Transforme un audio en CR structuré — gain immédiat sans aucune compétence technique.', href: 'modules/cu-003-cr-reunion.html' }
      ],
      decision: [
        { id: 'cu-001', name: 'Recherche & veille augmentée', reason: 'Étape zéro pour outiller toute prise de décision — sourcer en minutes.', href: 'modules/cu-001-recherche-veille.html' },
        { id: 'cu-011', name: 'Veille concurrentielle continue', reason: 'Surveille un panel de concurrents sans temps quotidien dédié.', href: 'modules/cu-011-veille-concurrentielle.html' },
        { id: 'cu-008', name: 'Knowledge base interne (RAG)', reason: 'Rendre la mémoire d\'organisation interrogeable — usage décisionnel par excellence.', href: 'modules/cu-008-knowledge-base-rag.html' }
      ],
      croissance: [
        { id: 'cu-002', name: 'Assistant rédactionnel', reason: 'Première brique pour qui veut accélérer la production commerciale.', href: 'modules/cu-002-assistant-redactionnel.html' },
        { id: 'cu-006', name: 'Qualification de leads par chatbot', reason: 'Capter et qualifier les leads chauds 24/7 — entrée commerciale rapide.', href: 'modules/cu-006-leads-chatbot.html' },
        { id: 'cu-023', name: 'Devis simples : porte d\'entrée IA', reason: 'Brouillon de devis en 36 min au lieu d\'1 h — ROI rapide, faible risque.', href: 'modules/cu-023-devis-intelligent.html' }
      ],
      industrie: [
        { id: 'cu-001', name: 'Recherche & veille augmentée', reason: 'Avant la maintenance prédictive, monter en culture sur la stack IA.', href: 'modules/cu-001-recherche-veille.html' },
        { id: 'cu-016', name: 'Maintenance prédictive industrielle', reason: 'Capteurs + IA pour anticiper les défaillances : -15 à 30 % sur coûts maintenance.', href: 'modules/cu-016-maintenance-predictive.html' },
        { id: 'cu-017', name: 'Contrôle qualité par vision IA', reason: 'Détection automatique de défauts à cadence industrielle.', href: 'modules/cu-017-controle-qualite-vision.html' }
      ]
    },
    deploiement: {
      productivite: [
        { id: 'cu-008', name: 'Knowledge base interne (RAG)', reason: 'Industrialiser la connaissance interne — le passage clé après les usages individuels.', href: 'modules/cu-008-knowledge-base-rag.html' },
        { id: 'cu-021', name: 'Finance & comptabilité augmentées', reason: 'ROI 155 % an 1 documenté sur cas PME. Brique structurante.', href: 'modules/cu-021-finance-augmentee.html' },
        { id: 'cu-024', name: 'Order-to-cash automation', reason: 'Cycle complet devis → encaissement, calé sur facturation électronique 2026-2027.', href: 'modules/cu-024-order-to-cash.html' }
      ],
      decision: [
        { id: 'cu-008', name: 'Knowledge base interne (RAG)', reason: 'Couche centrale pour outiller la décision — onboarding, mémoire, archives.', href: 'modules/cu-008-knowledge-base-rag.html' },
        { id: 'cu-020', name: 'Conformité RGPD & AI Act', reason: 'Deadline 2 août 2026 — cadre incontournable avant tout déploiement décisionnel.', href: 'modules/cu-020-conformite-rgpd-ai-act.html' },
        { id: 'cu-025', name: 'Knowledge management dirigeant', reason: 'Système personnel auto-apprenant — briefing matinal, synthèse, archive contextualisée.', href: 'modules/cu-025-knowledge-management-dirigeant.html' }
      ],
      croissance: [
        { id: 'cu-005', name: 'Propositions commerciales B2B', reason: 'RFP, bid management, propal > 20 pages : couplage IA + base de connaissance.', href: 'modules/cu-005-devis-propositions.html' },
        { id: 'cu-009', name: 'Content repurposing', reason: 'Long-form → clips, threads, posts multi-canaux — leverage éditorial.', href: 'modules/cu-009-content-repurposing.html' },
        { id: 'cu-022', name: 'Voicebot accueil téléphonique', reason: 'ROI 2-4 mois, couverture 7h-21h sans surcoût — cap structurant.', href: 'modules/cu-022-voicebot-accueil.html' }
      ],
      industrie: [
        { id: 'cu-016', name: 'Maintenance prédictive industrielle', reason: 'Le cas d\'usage industriel #1 — -20 à 50 % d\'arrêts non planifiés.', href: 'modules/cu-016-maintenance-predictive.html' },
        { id: 'cu-017', name: 'Contrôle qualité par vision IA', reason: 'Cadence industrielle : papier, bois, textile, agro. Brique vision IA mature.', href: 'modules/cu-017-controle-qualite-vision.html' },
        { id: 'cu-018', name: 'Optimisation de production', reason: 'Nesting, ordonnancement, paramètres machine. -10 à 30 % de chutes matière.', href: 'modules/cu-018-optimisation-production.html' }
      ]
    },
    agentique: {
      productivite: [
        { id: 'cu-013', name: 'Workflow email → CRM → réponse', reason: 'Premier pas agentique : 30-60 min/jour libérées sur le tri d\'emails.', href: 'modules/cu-013-workflow-email-crm.html' },
        { id: 'cu-014', name: 'Multi-agents par fonction métier', reason: 'Pattern « un agent par fonction » avec orchestrateur central.', href: 'modules/cu-014-multi-agents.html' },
        { id: 'cu-026', name: 'Gouvernance des agents IA', reason: 'Manager un agent IA comme un employé débutant — 7 dimensions à formaliser.', href: 'modules/cu-026-gouvernance-agents-ia.html' }
      ],
      decision: [
        { id: 'cu-026', name: 'Gouvernance des agents IA', reason: 'Indispensable avant de lâcher des agents en autonomie sur la décision.', href: 'modules/cu-026-gouvernance-agents-ia.html' },
        { id: 'cu-014', name: 'Multi-agents par fonction métier', reason: 'Vision systémique de la transformation IA par fonction.', href: 'modules/cu-014-multi-agents.html' },
        { id: 'cu-020', name: 'Conformité RGPD & AI Act', reason: 'Cadre réglementaire à valider avant tout dispositif agentique décisionnel.', href: 'modules/cu-020-conformite-rgpd-ai-act.html' }
      ],
      croissance: [
        { id: 'cu-010', name: 'Pipeline contenu social automatisé', reason: 'Système 4 agents : recherche → idéation → rédaction → publication.', href: 'modules/cu-010-pipeline-contenu-social.html' },
        { id: 'cu-013', name: 'Workflow email → CRM → réponse', reason: 'Workflow référence pour libérer du temps commercial structurellement.', href: 'modules/cu-013-workflow-email-crm.html' },
        { id: 'cu-015', name: 'Asynchronicité agentique — Stripe Minions', reason: 'Cas-école managérial : équipe IA assistant → équipe IA autonome.', href: 'modules/cu-015-stripe-minions.html' }
      ],
      industrie: [
        { id: 'cu-018', name: 'Optimisation de production', reason: 'Brique d\'orchestration la plus mature côté production multi-filière.', href: 'modules/cu-018-optimisation-production.html' },
        { id: 'cu-014', name: 'Multi-agents par fonction métier', reason: 'Vision agentique transposable à l\'organisation industrielle.', href: 'modules/cu-014-multi-agents.html' },
        { id: 'cu-027', name: 'Faire développer une appli métier', reason: 'Cadrage projet pour dirigeant non-IT — sécurité, scope, prestataire.', href: 'modules/cu-027-dev-applicatif-ia.html' }
      ]
    }
  };

  function setupStarter() {
    const starter = document.querySelector('.starter');
    if (!starter) return;

    const state = { stage: null, axis: null };
    const stageBtns = starter.querySelectorAll('[data-stage]');
    const axisBtns = starter.querySelectorAll('[data-axis]');
    const resultsEl = starter.querySelector('.starter-results');
    const recsEl = starter.querySelector('.starter-recs');
    const titleEl = starter.querySelector('.starter-results-title');
    const restartBtn = starter.querySelector('.starter-restart');

    function tryResolve() {
      if (!state.stage || !state.axis) return;
      const recs = (STARTER_LIBRARY[state.stage] || {})[state.axis] || [];
      if (!recs.length) return;
      const stageLabel = {
        decouverte: 'Tu démarres',
        deploiement: 'Tu industrialises',
        agentique: 'Tu vises l\'autonomie agentique'
      }[state.stage];
      const axisLabel = {
        productivite: 'Productivité',
        decision: 'Décision & gouvernance',
        croissance: 'Croissance commerciale',
        industrie: 'Industrie'
      }[state.axis];
      titleEl.innerHTML = `${stageLabel}, focus <strong>${axisLabel.toLowerCase()}</strong> — 3 modules pour ton itinéraire :`;

      recsEl.innerHTML = recs.map((m, i) => `
        <a class="starter-rec" href="${m.href}">
          <div class="starter-rec-num">Suggestion ${String(i+1).padStart(2,'0')}</div>
          <div class="starter-rec-name">${m.name}</div>
          <div class="starter-rec-reason">${m.reason}</div>
        </a>
      `).join('');
      starter.classList.add('is-resolved');
    }

    function pick(group, value, btn) {
      state[group] = value;
      const peers = starter.querySelectorAll(`[data-${group}]`);
      peers.forEach(b => b.classList.toggle('is-selected', b === btn));
      tryResolve();
    }

    stageBtns.forEach(btn => {
      btn.addEventListener('click', () => pick('stage', btn.dataset.stage, btn));
    });
    axisBtns.forEach(btn => {
      btn.addEventListener('click', () => pick('axis', btn.dataset.axis, btn));
    });
    if (restartBtn) {
      restartBtn.addEventListener('click', () => {
        state.stage = null;
        state.axis = null;
        starter.classList.remove('is-resolved');
        [...stageBtns, ...axisBtns].forEach(b => b.classList.remove('is-selected'));
        recsEl.innerHTML = '';
        starter.scrollIntoView({ behavior: 'smooth', block: 'center' });
      });
    }
  }

  // ----------------------------------------------------------
  // Boot
  // ----------------------------------------------------------
  function init() {
    setupJourneyRail();
    setupStarter();
    updateProgressBadges();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
