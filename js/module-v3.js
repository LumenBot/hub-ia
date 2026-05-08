// ========================================
// V3 — Scroll-spy + progress bar + TOC mobile
// JS partagé pour tous les modules V3
// ========================================

// Barre de progression de lecture
function updateProgress() {
  const bar = document.getElementById('readingProgress');
  if (!bar) return;
  const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
  bar.style.width = Math.min(scrolled, 100) + '%';
}
window.addEventListener('scroll', updateProgress, { passive: true });

// Scroll-spy : highlight de la section active dans le TOC
// Support des 2 structures TOC : .module-toc-list a (V3 standard) et .module-toc-nav a (variante 8 modules)
document.addEventListener('DOMContentLoaded', () => {
  const tocSections = document.querySelectorAll('.module-section[id], section[id^="section-"]');
  const tocLinks = document.querySelectorAll('.module-toc-list a, .module-toc-nav a');

  if (tocSections.length === 0 || tocLinks.length === 0) return;

  const tocObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        tocLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === '#' + id);
        });
      }
    });
  }, { rootMargin: '-20% 0px -70% 0px', threshold: 0 });

  tocSections.forEach(section => tocObserver.observe(section));

  // Smooth scroll sur les liens TOC
  tocLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        // Fermer le TOC mobile après clic
        const list = document.getElementById('tocList');
        if (window.innerWidth <= 900 && list) list.classList.remove('open');
      }
    });
  });
});

// Toggle TOC mobile (structure module-toc-list)
function toggleToc() {
  const list = document.getElementById('tocList');
  if (list) list.classList.toggle('open');
  // Compat structure alternative module-toc-nav (8 modules)
  const nav = document.getElementById('tocNav');
  if (nav) {
    nav.classList.toggle('collapsed');
    // Mettre à jour le bouton − / +
    const btn = document.querySelector('.module-toc-toggle');
    if (btn) btn.textContent = nav.classList.contains('collapsed') ? '+' : '−';
  }
}
