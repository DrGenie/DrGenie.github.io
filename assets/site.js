
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href^="http"]').forEach((link) => {
    try {
      const url = new URL(link.href, window.location.href);
      if (url.origin !== window.location.origin) {
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
      }
    } catch (_) {}
  });

  document.querySelectorAll('[data-print-page="true"]').forEach((button) => {
    button.setAttribute('role', 'button');
    button.setAttribute('tabindex', '0');
    const print = () => window.print();
    button.addEventListener('click', print);
    button.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); print(); }
    });
  });

  const host = document.querySelector('#publication-tools');
  const records = Array.from(document.querySelectorAll('.publication-record[data-field]'));
  if (!host || !records.length) return;

  const years = [...new Set(records.map((record) => record.dataset.year))].sort((a,b) => Number(b)-Number(a));
  host.innerHTML = `
    <div class="publication-controls" aria-label="Publication filters">
      <div class="publication-control">
        <label for="publication-search">Search</label>
        <input id="publication-search" type="search" placeholder="Title, author, journal or keyword" autocomplete="off">
      </div>
      <div class="publication-control">
        <label for="publication-field">Field</label>
        <select id="publication-field">
          <option value="all">All fields</option>
          <option value="preference">Preferences & choice</option>
          <option value="public-health">Public health policy</option>
          <option value="other">Other applied economics</option>
        </select>
      </div>
      <div class="publication-control">
        <label for="publication-year">Year</label>
        <select id="publication-year">
          <option value="all">All years</option>
          ${years.map((year) => `<option value="${year}">${year}</option>`).join('')}
        </select>
      </div>
      <div class="publication-control">
        <label for="publication-type">Output</label>
        <select id="publication-type">
          <option value="all">All outputs</option>
          <option value="journal">Journal articles</option>
          <option value="working">Working papers</option>
          <option value="chapter">Book chapter</option>
          <option value="data">Data</option>
        </select>
      </div>
      <button id="publication-reset" class="filter-reset" type="button">Reset</button>
    </div>`;

  const search = document.querySelector('#publication-search');
  const field = document.querySelector('#publication-field');
  const year = document.querySelector('#publication-year');
  const type = document.querySelector('#publication-type');
  const reset = document.querySelector('#publication-reset');
  const empty = document.querySelector('#publication-empty');
  const groups = Array.from(document.querySelectorAll('.publication-year-section'));
  const sections = Array.from(document.querySelectorAll('[data-publication-section]'));

  const applyFilters = () => {
    const q = search.value.trim().toLowerCase();
    const fv = field.value, yv = year.value, tv = type.value;
    let visible = 0;
    records.forEach((record) => {
      const show = (!q || (record.dataset.search || '').includes(q)) &&
        (fv === 'all' || record.dataset.field === fv) &&
        (yv === 'all' || record.dataset.year === yv) &&
        (tv === 'all' || record.dataset.type === tv);
      record.hidden = !show;
      if (show) visible += 1;
    });
    groups.forEach((group) => {
      group.hidden = !Array.from(group.querySelectorAll('.publication-record')).some((record) => !record.hidden);
    });
    sections.forEach((section) => {
      section.hidden = !Array.from(section.querySelectorAll('.publication-record')).some((record) => !record.hidden);
    });
    empty.hidden = visible !== 0;
  };

  search.addEventListener('input', applyFilters);
  [field, year, type].forEach((control) => control.addEventListener('change', applyFilters));
  reset.addEventListener('click', () => {
    search.value = ''; field.value = 'all'; year.value = 'all'; type.value = 'all';
    applyFilters(); search.focus();
  });
});
