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

  document.querySelectorAll('[data-print-page="true"]').forEach((button) => {
    button.addEventListener('click', () => window.print());
  });

  const search = document.querySelector('#publication-search');
  const field = document.querySelector('#publication-field');
  const year = document.querySelector('#publication-year');
  const type = document.querySelector('#publication-type');
  const reset = document.querySelector('#publication-reset');
  const count = document.querySelector('#publication-count');
  const empty = document.querySelector('#publication-empty');
  const records = Array.from(document.querySelectorAll('.publication-record[data-field]'));
  const groups = Array.from(document.querySelectorAll('.publication-year-group'));
  const sections = Array.from(document.querySelectorAll('[data-publication-section]'));

  if (records.length && search && field && year && type) {
    const applyFilters = () => {
      const q = search.value.trim().toLowerCase();
      const fieldValue = field.value;
      const yearValue = year.value;
      const typeValue = type.value;
      const filtersActive = Boolean(q) || fieldValue !== 'all' || yearValue !== 'all' || typeValue !== 'all';
      let visible = 0;

      records.forEach((record) => {
        const matchesQuery = !q || (record.dataset.search || '').includes(q);
        const matchesField = fieldValue === 'all' || record.dataset.field === fieldValue;
        const matchesYear = yearValue === 'all' || record.dataset.year === yearValue;
        const matchesType = typeValue === 'all' || record.dataset.type === typeValue;
        const show = matchesQuery && matchesField && matchesYear && matchesType;
        record.hidden = !show;
        if (show) visible += 1;
      });

      groups.forEach((group) => {
        const hasVisible = Array.from(group.querySelectorAll('.publication-record')).some((record) => !record.hidden);
        group.hidden = !hasVisible;
        if (filtersActive && hasVisible) group.open = true;
      });

      sections.forEach((section) => {
        const hasVisible = Array.from(section.querySelectorAll('.publication-record')).some((record) => !record.hidden);
        section.hidden = !hasVisible;
      });

      count.textContent = `${visible} output${visible === 1 ? '' : 's'}`;
      empty.hidden = visible !== 0;
    };

    [search, field, year, type].forEach((control) => {
      control.addEventListener(control === search ? 'input' : 'change', applyFilters);
    });

    reset.addEventListener('click', () => {
      search.value = '';
      field.value = 'all';
      year.value = 'all';
      type.value = 'all';
      records.forEach((record) => { record.hidden = false; });
      groups.forEach((group) => {
        group.hidden = false;
        group.open = Number(group.dataset.yearGroup) >= 2025;
      });
      sections.forEach((section) => { section.hidden = false; });
      applyFilters();
      search.focus();
    });

    applyFilters();
  }
});
