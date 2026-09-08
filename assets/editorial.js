(()=>{'use strict';
function addSelectedPublications(){
  const controls=document.querySelector('.publication-controls');
  if(!controls||document.querySelector('.selected-publications'))return;
  const section=document.createElement('section');
  section.className='selected-publications';
  section.innerHTML=`<div class="page-shell narrow"><p class="eyebrow">Selected publications</p><div class="selected-publication-list">
  <article><span>2026 · Social Science & Medicine</span><h2><a href="/publications/fit-for-purpose/">Fit for Purpose? Assessing the Robustness of Discrete Choice Experiment Designs <b>→</b></a></h2></article>
  <article><span>2026 · Health Economics</span><h2><a href="/publications/guidance-or-misdirection/">Guidance or Misdirection? Unpacking the Role of Feedback in Health Preference Assessments <b>→</b></a></h2></article>
  <article><span>2026 · Value in Health</span><h2><a href="/publications/priority-for-self-or-others/">Priority for Self or Others? Incorporating Equity Considerations in Preference-Based Health Value Assessment <b>→</b></a></h2></article>
  <article><span>2026 · Health Policy</span><h2><a href="/publications/feeling-lonely/">Feeling Lonely? Preferences for Support Programmes to Reduce Loneliness <b>→</b></a></h2></article>
  </div></div>`;
  controls.parentNode.insertBefore(section,controls);
}
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
document.addEventListener('DOMContentLoaded',()=>{cleanLegacyUI();addSelectedPublications();refinePublicationFilters();});
})();
