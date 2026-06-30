document.addEventListener('DOMContentLoaded', () => {
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
});
