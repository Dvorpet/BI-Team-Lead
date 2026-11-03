(function(){
 var root=document.documentElement;
 function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
 var TITLES={cs:'BI Team Lead – případová studie',en:'BI Team Lead – case study'};
 function setLang(l){root.dataset.lang=l;root.lang=l;document.title=TITLES[l];store('lang',l)}
 function setTheme(t){root.dataset.theme=t;store('theme',t)}
 document.querySelectorAll('[data-setlang]').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.setlang)})});
 document.querySelector('.theme').addEventListener('click',function(){setTheme(root.dataset.theme==='dark'?'light':'dark')});
 setLang(root.dataset.lang||'cs');

 var params=new URLSearchParams(location.search);
 if(params.get('print')){
  var d=params.get('print');document.body.classList.add('print');
  setLang(params.get('lang')||'cs');root.dataset.theme='light';
  document.querySelectorAll('.panel').forEach(function(p){p.hidden=p.dataset.panel!==d});
  return;
 }

 var cur={p1:0,p2:0};
 var count={p1:document.querySelectorAll('.slide[data-deck=p1]').length,p2:document.querySelectorAll('.slide[data-deck=p2]').length};
 function show(deck,i,push){
  i=Math.max(0,Math.min(count[deck]-1,i));cur[deck]=i;
  document.querySelectorAll('[data-deck="'+deck+'"][data-i]').forEach(function(el){el.classList.toggle('on',+el.dataset.i===i)});
  document.querySelector('.counter[data-deck="'+deck+'"]').textContent=(i+1)+' / '+count[deck];
  if(push){history.replaceState(null,'','#'+deck+(i?'-'+(i+1):''))}
 }
 var active='p1';
 function tab(t){
  active=t;
  document.querySelectorAll('.panel').forEach(function(p){p.hidden=p.dataset.panel!==t});
  document.querySelectorAll('.tabs a').forEach(function(a){a.setAttribute('aria-selected',a.dataset.tab===t?'true':'false')});
 }
 function route(){
  var h=(location.hash||'#p1').slice(1),m=h.match(/^(p1|p2)(?:-(\d+))?$/);
  if(m){tab(m[1]);show(m[1],m[2]?+m[2]-1:cur[m[1]],false)}else if(h==='data'){tab('data')}else{tab('p1');show('p1',0,false)}
 }
 window.addEventListener('hashchange',route);
 document.querySelectorAll('.prev').forEach(function(b){b.addEventListener('click',function(){show(b.dataset.deck,cur[b.dataset.deck]-1,true)})});
 document.querySelectorAll('.next').forEach(function(b){b.addEventListener('click',function(){show(b.dataset.deck,cur[b.dataset.deck]+1,true)})});
 document.querySelectorAll('.toc-btn').forEach(function(b){b.addEventListener('click',function(){show(b.dataset.deck,+b.dataset.i,true);document.querySelector('.stage[data-deck="'+b.dataset.deck+'"]').scrollIntoView({behavior:'smooth',block:'nearest'})})});
 document.querySelectorAll('.notes-toggle').forEach(function(b){b.addEventListener('click',function(){
  var n=document.querySelector('.notes[data-deck="'+b.dataset.deck+'"]');n.hidden=!n.hidden;b.setAttribute('aria-pressed',String(!n.hidden))})});
 function stage(){return document.querySelector('.stage[data-deck="'+active+'"]')}
 function exitFake(){var s=document.querySelector('.stage.fake-fs');if(s)s.classList.remove('fake-fs')}
 document.querySelectorAll('.present').forEach(function(b){b.addEventListener('click',function(){
  var s=document.querySelector('.stage[data-deck="'+b.dataset.deck+'"]');
  if(s.requestFullscreen){s.requestFullscreen().catch(function(){s.classList.add('fake-fs')})}else{s.classList.add('fake-fs')}
  s.focus()})});
 document.querySelectorAll('.stage').forEach(function(s){s.addEventListener('click',function(e){
  if(document.fullscreenElement===s||s.classList.contains('fake-fs')){var d=s.dataset.deck;show(d,cur[d]+(e.clientX<innerWidth/3?-1:1),true)}})});
 document.addEventListener('keydown',function(e){
  if(active==='data'||e.altKey||e.ctrlKey||e.metaKey)return;
  var t=e.target.tagName;if(t==='INPUT'||t==='TEXTAREA')return;
  if(e.key==='ArrowRight'||e.key==='PageDown'||(e.key===' '&&(document.fullscreenElement||document.querySelector('.fake-fs')))){e.preventDefault();show(active,cur[active]+1,true)}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();show(active,cur[active]-1,true)}
  else if(e.key==='Home'){show(active,0,true)}else if(e.key==='End'){show(active,count[active]-1,true)}
  else if(e.key==='Escape'){exitFake()}
  else if(e.key==='f'||e.key==='F'){var s=stage();if(s.requestFullscreen&&!document.fullscreenElement)s.requestFullscreen().catch(function(){})}
 });
 show('p1',0,false);show('p2',0,false);route();
})();
