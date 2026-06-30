document.addEventListener('DOMContentLoaded', () => {
  // --- External links open in a new tab ---
  document.querySelectorAll('a[href^="http"]').forEach((link) => {
    const url = new URL(link.href, window.location.href);
    if (url.origin !== window.location.origin) {
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
    }
  });
  document.querySelectorAll('[data-open-new="true"]').forEach((link) => {
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  });

  // --- Publications filter ---
  const filters = document.querySelectorAll('[data-pub-filter]');
  const publications = document.querySelectorAll('.publication-item[data-field]');
  if (filters.length && publications.length) {
    filters.forEach((button) => {
      button.addEventListener('click', () => {
        filters.forEach((b) => b.classList.remove('active'));
        button.classList.add('active');
        const value = button.dataset.pubFilter;
        publications.forEach((item) => {
          item.hidden = value !== 'all' && item.dataset.field !== value;
        });
      });
    });
  }

  // --- Dark mode toggle (injected into the navbar) ---
  const root = document.documentElement;
  const navRight = document.querySelector('.navbar .navbar-nav.ms-auto, .navbar .quarto-navbar-tools, .navbar-nav');
  const btn = document.createElement('button');
  btn.className = 'theme-toggle';
  btn.setAttribute('aria-label', 'Toggle dark mode');
  const setIcon = () =>
    (btn.innerHTML = root.getAttribute('data-theme') === 'dark'
      ? '<i class="bi bi-sun"></i>'
      : '<i class="bi bi-moon-stars"></i>');
  setIcon();
  btn.addEventListener('click', () => {
    const dark = root.getAttribute('data-theme') === 'dark';
    const next = dark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('mg-theme', next); } catch (e) {}
    setIcon();
  });
  if (navRight) navRight.appendChild(btn);

  // --- Scroll-reveal (respects reduced motion) ---
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach((el) => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add('in');
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    reveals.forEach((el) => io.observe(el));
  }
});
