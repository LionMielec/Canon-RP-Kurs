(() => {
'use strict';
const app=document.getElementById('app');
const home=app.innerHTML;
let animation=null;
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function inline(s){return escape(s).replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/\[([^\]]+)\]\(L1-01_ROBIE_SWOJE_PIERWSZE_ZDJECIE.md\)/g,'<a class="subtle-link" href="#lekcja-1">$1</a>');}
function markdown(s){return s.trim().split(/\n\s*\n/).map(block=>block.startsWith('- ')?'<ul>'+block.split('\n').map(x=>'<li>'+inline(x.replace(/^- /,''))+'</li>').join('')+'</ul>':'<p>'+inline(block).replace(/\n/g,' ')+'</p>').join('');}
function helpMarkup(section){return section.body.split(/\n\s*\n/).filter(Boolean).map(p=>{const m=p.match(/^\*\*(.+?)\*\*\s*([\s\S]*)$/);return m?`<details class="lesson-help"><summary>${escape(m[1])}</summary><div class="help-copy">${markdown(m[2])}</div></details>`:markdown(p);}).join('');}
function photoMarkup(step){
 const positions=[{x:19,y:68,label:'Przełącznik ON/OFF'},{x:61,y:64,label:'Pokrętło trybów A+'},{x:79,y:27,label:'Spust migawki'},{x:79,y:27,label:'Spust migawki'},{x:79,y:27,label:'Spust migawki'}];
 const p=positions[step];if(!p)return '';
 return `<figure class="media"><div class="media-stage"><div class="media-plane" id="media-plane" style="transform-origin:${p.x}% ${p.y}%"><img src="./camera-top.jpeg" alt="Canon EOS RP Ani widziany z góry. Zaznaczony element: ${p.label}." width="1600" height="1200"><span class="media-ring" style="left:${p.x}%;top:${p.y}%" aria-hidden="true"></span></div></div><figcaption class="media-bar"><p>${p.label}<br>Animowane zbliżenie</p><button type="button" id="motion-toggle" aria-label="Odtwórz zbliżenie na ${p.label}">▶ Odtwórz</button></figcaption></figure>`;
}
function setupMotion(){const button=document.getElementById('motion-toggle');const plane=document.getElementById('media-plane');if(!button||!plane)return;
 const resetLabel=()=>{button.textContent='↻ Powtórz';button.setAttribute('aria-label','Powtórz animowane zbliżenie');};
 button.onclick=()=>{if(animation?.playState==='running'){animation.pause();button.textContent='▶ Wznów';button.setAttribute('aria-label','Wznów animowane zbliżenie');return;}if(animation?.playState==='paused'){animation.play();button.textContent='Ⅱ Zatrzymaj';button.setAttribute('aria-label','Zatrzymaj animowane zbliżenie');return;}
 animation?.cancel();animation=plane.animate([{transform:'scale(1)',offset:0},{transform:'scale(1.9)',offset:.55},{transform:'scale(1.9)',offset:1}],{duration:reduced.matches?1:4500,easing:'ease-in-out',fill:'forwards'});button.textContent='Ⅱ Zatrzymaj';button.setAttribute('aria-label','Zatrzymaj animowane zbliżenie');animation.onfinish=resetLabel;
 };
}
function render(){
 animation?.cancel();animation=null;
 const match=location.hash.match(/^#lekcja-([12])(?:\/(\d+))?$/);
 if(!match){app.innerHTML=home;document.title='Canon RP — Kurs';if(window.matchMedia('(display-mode: standalone)').matches||navigator.standalone)app.querySelector('.install').hidden=true;window.scrollTo(0,0);return;}
 const lesson=window.CANON_LESSONS.find(l=>l.id===Number(match[1]));
 if(!lesson){location.hash='';return;}
 const help=lesson.sections.find(s=>s.title==='Gdy coś nie wychodzi');
 const pages=lesson.sections.filter(s=>s!==help);
 const pageIndex=Math.min(Number(match[2]||0),pages.length-1);
 const page=pages[pageIndex];
 const steps=pages.filter(s=>s.kind==='step');const stepIndex=steps.indexOf(page);
 const counter=page.kind==='step'?`Krok ${stepIndex+1} z ${steps.length}`:pageIndex===0?'Przygotowanie':pageIndex===pages.length-1?'Podsumowanie':page.title.startsWith('Twoje ćwiczenie')?'Ćwiczenie':'Wyjaśnienie';
 const nextIndex=pageIndex+1;
 const nextLabel=pageIndex===0?'Zaczynamy':pageIndex===pages.length-1?'Wróć do lekcji':pages[nextIndex]?.title.startsWith('Twoje ćwiczenie')?'Czas na ćwiczenie':'Dalej';
 let body=page.body,check='';
 if(body.includes('**Sprawdź:**')){const pieces=body.split('**Sprawdź:**');body=pieces[0];const checkparts=pieces.slice(1).join('**Sprawdź:**').split(/\n\s*\n/);check=`<div class="check"><div class="check-label">✓ Sprawdź</div>${markdown(checkparts.shift())}</div>`;if(checkparts.length)check+=markdown(checkparts.join('\n\n'));}
 const overview=pageIndex===0?`<p class="lead">${inline(lesson.intro)}</p>`:'';
 const humor=lesson.id===1&&pageIndex===0?'<p class="humor">Książka to cierpliwa modelka. Nie mruga i nie pyta, czy już kończymy.</p>':lesson.id===2&&page.title.startsWith('Dlaczego')?'<p class="humor">Lupa nie naprawia zdjęcia — tylko przygląda mu się jak detektyw.</p>':'';
 const media=lesson.id===1&&page.kind==='step'?photoMarkup(stepIndex):'';
 const showHelp=page.kind==='step'||page.title.startsWith('Twoje ćwiczenie');
 app.innerHTML=`<article><a class="crumb" href="#">← Wszystkie lekcje</a><div class="lesson-meta"><span>Lekcja 0${lesson.id} · ${lesson.duration.replace('Około ','')}</span><span>${counter}</span></div><div class="track" role="progressbar" aria-label="Miejsce w lekcji" aria-valuemin="0" aria-valuemax="${pages.length}" aria-valuenow="${pageIndex+1}"><span style="width:${(pageIndex+1)/pages.length*100}%"></span></div><p class="eyebrow">${lesson.id===1?'OSWAJAM APARAT':'OGLĄDAM EFEKT'}</p><h1 class="step-title step-heading" tabindex="-1">${escape(page.title.replace(/^\d+\.\s*/,''))}</h1>${overview}${media}<div class="lesson-text">${markdown(body)}${check}${humor}</div>${showHelp?`<details class="lesson-help"><summary>Coś nie wychodzi?</summary><div>${helpMarkup(help)}</div></details>`:''}<nav class="footer-actions" aria-label="Przechodzenie przez lekcję">${pageIndex>0?`<a class="secondary" href="#lekcja-${lesson.id}/${pageIndex-1}" aria-label="Poprzednia część lekcji">← Wstecz</a>`:''}<a class="primary" href="${nextIndex<pages.length?'#lekcja-'+lesson.id+'/'+nextIndex:'#'}">${nextLabel} <span aria-hidden="true">→</span></a></nav><p class="footer-note">Bez pośpiechu. Aparat poczeka.</p>${pageIndex===pages.length-1&&lesson.id===1?'<a class="end-nav subtle-link" href="#lekcja-2">Przejdź do lekcji 2</a>':''}</article>`;
 document.title=`Lekcja ${lesson.id} · Canon RP`;
 setupMotion();window.scrollTo(0,0);app.querySelector('h1').focus({preventScroll:true});
}
window.addEventListener('hashchange',render);render();
})();
