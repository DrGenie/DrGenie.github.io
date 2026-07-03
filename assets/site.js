(()=>{'use strict';const root=document.documentElement;const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function icon(theme){return theme==='dark'?'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4a8 8 0 1 0 8 8h-2a6 6 0 1 1-6-6z"/></svg>':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10m0-5h1v3h-1zm0 17h1v3h-1zM2 12h3v1H2zm17 0h3v1h-3zM4.9 4.2 7 6.3l-.7.7-2.1-2.1zm12 12 2.1 2.1-.7.7-2.1-2.1zM19.1 4.9 17 7l-.7-.7 2.1-2.1zM7 17l-2.1 2.1-.7-.7 2.1-2.1z"/></svg>'}
function skip(){if(document.querySelector('.site-skip-link'))return;const a=document.createElement('a');a.className='site-skip-link';a.href='#quarto-content';a.textContent='Skip to main content';document.body.prepend(a)}
function theme(){let host=document.querySelector('.navbar-nav.ms-auto');if(!host){const collapse=document.querySelector('.navbar .navbar-collapse');if(!collapse)return;host=document.createElement('ul');host.className='navbar-nav ms-auto';collapse.appendChild(host)}const b=document.createElement('button');b.type='button';b.className='theme-toggle';b.setAttribute('aria-label','Switch colour theme');const update=()=>{const t=root.dataset.theme||'light';b.innerHTML=icon(t);b.title=t==='dark'?'Use light mode':'Use dark mode';b.setAttribute('aria-pressed',String(t==='dark'))};b.addEventListener('click',()=>{const t=root.dataset.theme==='dark'?'light':'dark';root.dataset.theme=t;root.style.colorScheme=t;localStorage.setItem('mesfin-theme',t);update()});update();const li=document.createElement('li');li.className='nav-item d-flex align-items-center';li.appendChild(b);host.appendChild(li)}
function external(){document.querySelectorAll('a[href^="http"]').forEach(a=>{try{if(new URL(a.href,location.href).origin!==location.origin){a.target='_blank';a.rel='noopener noreferrer'}}catch(_){}})}
function reveal(){const nodes=[...document.querySelectorAll('.reveal')];if(!nodes.length)return;if(reduced||!('IntersectionObserver'in window)){nodes.forEach(n=>n.classList.add('is-visible'));return}const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');io.unobserve(e.target)}}),{threshold:.08});nodes.forEach(n=>io.observe(n))}
async function buildInfo(){try{const r=await fetch('/assets/build-info.json',{cache:'no-store'});if(!r.ok)return;const d=await r.json();const e=document.getElementById('site-last-updated');if(e&&d.last_updated){const dt=new Date(d.last_updated+'T00:00:00Z');e.textContent='Last updated '+new Intl.DateTimeFormat('en-AU',{day:'numeric',month:'long',year:'numeric',timeZone:'UTC'}).format(dt)}}catch(_){}}
function filters(){const form=document.getElementById('publication-filters');if(!form)return;const q=document.getElementById('publication-search'),field=document.getElementById('publication-field'),year=document.getElementById('publication-year'),type=document.getElementById('publication-type');const items=[...document.querySelectorAll('.publication-record[data-search]')],groups=[...document.querySelectorAll('.publication-year-section')],sections=[...document.querySelectorAll('.publication-type-section')],empty=document.getElementById('publication-empty'),status=document.getElementById('publication-status');function apply(){const s=q.value.trim().toLowerCase(),f=field.value,y=year.value,t=type.value;let n=0;items.forEach(el=>{const show=(!s||el.dataset.search.includes(s))&&(f==='all'||el.dataset.field===f)&&(y==='all'||el.dataset.year===y)&&(t==='all'||el.dataset.type===t);el.hidden=!show;if(show)n++});groups.forEach(g=>{const visible=[...g.querySelectorAll('.publication-record')].some(x=>!x.hidden);g.hidden=!visible;if(visible&&(s||f!=='all'||y!=='all'||t!=='all'))g.open=true});sections.forEach(sec=>sec.hidden=![...sec.querySelectorAll('.publication-record')].some(x=>!x.hidden));empty.hidden=n!==0;status.textContent=`Showing ${n} of ${items.length} outputs`}
form.addEventListener('input',apply);form.addEventListener('change',apply);form.addEventListener('reset',()=>setTimeout(apply,0));apply()}
async function metrics(){const tiles=[...document.querySelectorAll('[data-metric-tile]')];if(!tiles.length)return;try{const r=await fetch('/assets/scholar-metrics.json',{cache:'no-store'});if(!r.ok)return;const d=await r.json();const map={citations:d.citations,hindex:d.h_index,i10:d.i10_index};tiles.forEach(t=>{const key=t.dataset.metricTile;const val=map[key];const el=t.querySelector('[data-metric]');if(val!=null&&el){el.textContent=Number(val).toLocaleString('en-AU');t.hidden=false}else{t.hidden=true}})}catch(_){}}
document.addEventListener('DOMContentLoaded',()=>{skip();theme();external();reveal();buildInfo();metrics();filters()});})();
/* Click-to-load YouTube (privacy-enhanced, no player until activated) */
(function(){
  function load(frame){
    var url=frame.getAttribute('data-embed'); if(!url) return;
    var ifr=document.createElement('iframe');
    ifr.setAttribute('src',url+(url.indexOf('?')>-1?'&':'?')+'autoplay=1');
    ifr.setAttribute('title','Featured webinar featuring Dr Mesfin Genie');
    ifr.setAttribute('loading','lazy');
    ifr.setAttribute('allow','accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
    ifr.setAttribute('allowfullscreen','');
    ifr.setAttribute('referrerpolicy','strict-origin-when-cross-origin');
    frame.innerHTML=''; frame.appendChild(ifr);
  }
  document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('.video-frame .video-play').forEach(function(btn){
      btn.addEventListener('click',function(){ load(btn.closest('.video-frame')); });
    });
  });
})();

/* Collapsible author lists: keep it clean, always show Mesfin Genie */
(function(){
  var meRe=/Mesfin\s+(?:G\.?\s+)?Genie/i;
  function fmt(a){ return meRe.test(a) ? '<strong class="author-me">'+a+'</strong>' : a; }
  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.publication-authors').forEach(function(el){
      if(el.dataset.done) return;
      var raw=(el.textContent||'').trim();
      if(!raw) return;
      var authors=raw.split(/;\s*/).map(function(s){return s.trim();}).filter(Boolean);
      var full=authors.map(fmt).join('; ');
      if(authors.length<=5){ el.innerHTML=full; el.dataset.done='1'; return; }
      var meIdx=-1; authors.forEach(function(a,i){ if(meIdx<0 && meRe.test(a)) meIdx=i; });
      var head=authors.slice(0,3).map(fmt);
      if(meIdx>=3){ head.push('&hellip;'); head.push(fmt(authors[meIdx])); }
      var collapsed=head.join('; ');
      el.innerHTML='<span class="authors-view">'+collapsed+'</span>'+
        ' <button type="button" class="authors-toggle" aria-expanded="false">Show all '+authors.length+' authors</button>';
      el.dataset.full=full; el.dataset.collapsed=collapsed; el.dataset.count=authors.length; el.dataset.done='1';
    });
    document.addEventListener('click', function(e){
      var btn=e.target.closest('.authors-toggle'); if(!btn) return;
      var el=btn.closest('.publication-authors');
      var view=el.querySelector('.authors-view');
      var open=btn.getAttribute('aria-expanded')==='true';
      view.innerHTML = open ? el.dataset.collapsed : el.dataset.full;
      btn.setAttribute('aria-expanded', open?'false':'true');
      btn.textContent = open ? ('Show all '+el.dataset.count+' authors') : 'Show fewer authors';
    });
  });
})();

/* Social sharing (no third-party scripts, privacy-friendly) */
(function(){
  var ICON={
    x:'<path d="M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754 11.09h-3.182z"/>',
    linkedin:'<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>',
    facebook:'<path d="M24 12.073c0-6.627-5.373-12-12-12S0 5.446 0 12.073c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078V12.07h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.472h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>',
    whatsapp:'<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>',
    bluesky:'<path d="M12 10.8c-1.087-2.114-4.046-6.053-6.798-7.995C2.566.944 1.561 1.266.902 1.565.139 1.908 0 3.08 0 3.768c0 .69.378 5.65.624 6.479.815 2.736 3.713 3.66 6.383 3.364.136-.02.275-.039.415-.056-.138.022-.276.04-.415.056-3.912.58-7.387 2.005-2.83 7.078 5.013 5.19 6.87-1.113 7.823-4.308.953 3.195 2.05 9.271 7.733 4.308 4.267-4.308 1.172-6.498-2.74-7.078a8.741 8.741 0 0 1-.415-.056c.14.017.279.036.415.056 2.67.297 5.568-.628 6.383-3.364.246-.828.624-5.79.624-6.478 0-.69-.139-1.861-.902-2.206-.659-.298-1.664-.62-4.3 1.24C16.046 4.748 13.087 8.687 12 10.8Z"/>',
    email:'<path d="M1.5 4.5h21A1.5 1.5 0 0 1 24 6v12a1.5 1.5 0 0 1-1.5 1.5h-21A1.5 1.5 0 0 1 0 18V6a1.5 1.5 0 0 1 1.5-1.5Zm.5 2.2V18h20V6.7l-10 6.25L2 6.7Z"/>',
    copy:'<path d="M15.5 2h-8A2.5 2.5 0 0 0 5 4.5v1H4A2.5 2.5 0 0 0 1.5 8v11.5A2.5 2.5 0 0 0 4 22h8a2.5 2.5 0 0 0 2.5-2.5v-1h1A2.5 2.5 0 0 0 18 16V4.5A2.5 2.5 0 0 0 15.5 2ZM12.5 19.5A.5.5 0 0 1 12 20H4a.5.5 0 0 1-.5-.5V8A.5.5 0 0 1 4 7.5h8a.5.5 0 0 1 .5.5Zm3.5-3.5a.5.5 0 0 1-.5.5h-1V8A2.5 2.5 0 0 0 12 5.5H7v-1a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5Z"/>'
  };
  function btn(kind,href,label){
    return '<a class="share-btn share-'+kind+'" href="'+href+'" aria-label="'+label+'"'+(kind==='email'?'':' target="_blank" rel="noopener noreferrer"')+'><svg viewBox="0 0 24 24" aria-hidden="true">'+ICON[kind]+'</svg></a>';
  }
  function fill(bar){
    var url=bar.dataset.shareUrl || (bar.dataset.share==='site' ? 'https://mesfingenie.com/' : location.href);
    var title=bar.dataset.shareTitle || document.title;
    var u=encodeURIComponent(url), t=encodeURIComponent(title);
    bar.innerHTML=
      btn('x','https://twitter.com/intent/tweet?url='+u+'&text='+t,'Share on X')+
      btn('linkedin','https://www.linkedin.com/sharing/share-offsite/?url='+u,'Share on LinkedIn')+
      btn('facebook','https://www.facebook.com/sharer/sharer.php?u='+u,'Share on Facebook')+
      btn('bluesky','https://bsky.app/intent/compose?text='+t+'%20'+u,'Share on Bluesky')+
      btn('whatsapp','https://api.whatsapp.com/send?text='+t+'%20'+u,'Share on WhatsApp')+
      btn('email','mailto:?subject='+t+'&body='+u,'Share by email')+
      '<button type="button" class="share-btn share-copy" aria-label="Copy link"><svg viewBox="0 0 24 24" aria-hidden="true">'+ICON.copy+'</svg></button>';
    var cp=bar.querySelector('.share-copy');
    if(cp) cp.addEventListener('click',function(){
      (navigator.clipboard?navigator.clipboard.writeText(url):Promise.reject()).then(function(){
        cp.classList.add('copied'); setTimeout(function(){cp.classList.remove('copied');},1400);
      }).catch(function(){});
    });
  }
  document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('.share-bar').forEach(fill);
    // auto-add a share bar to blog articles
    if(/\/blog\/posts\/.+/.test(location.pathname)){
      var main=document.querySelector('main.content')||document.querySelector('main');
      if(main && !main.querySelector('.article-share')){
        var wrap=document.createElement('div');
        wrap.className='article-share';
        wrap.innerHTML='<span class="article-share-label">Share this article</span><div class="share-bar"></div>';
        main.appendChild(wrap);
        fill(wrap.querySelector('.share-bar'));
      }
    }
  });
})();
