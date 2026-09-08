(()=>{'use strict';
function refinePublicationFilters(){
  const form=document.getElementById('publication-filters');
  if(!form||form.dataset.editorialReady)return;
  form.dataset.editorialReady='1';
  const search=document.getElementById('publication-search')?.closest('.filter-field');
  const field=document.getElementById('publication-field')?.closest('.filter-field');
  const year=document.getElementById('publication-year')?.closest('.filter-field');
  const type=document.getElementById('publication-type')?.closest('.filter-field');
  const reset=form.querySelector('.filter-reset');
  if(!search||!field||!year||!type)return;
  search.classList.add('publication-search-primary');
  const details=document.createElement('details');
  details.className='publication-filter-details';
  const summary=document.createElement('summary');
  summary.textContent='Filters';
  const inner=document.createElement('div');
  inner.className='publication-filter-inner';
  [field,year,type,reset].filter(Boolean).forEach(el=>inner.appendChild(el));
  details.append(summary,inner);
  form.appendChild(details);
}
function cleanLegacyUI(){
  document.querySelectorAll('.breadcrumb').forEach(el=>el.remove());
  document.querySelectorAll('.theme-toggle').forEach(el=>el.remove());
}
document.addEventListener('DOMContentLoaded',()=>{cleanLegacyUI();refinePublicationFilters();});
})();
