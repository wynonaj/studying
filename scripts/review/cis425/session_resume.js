const SESSION425=KEY425+'-active-session';
function sessionCatalog(){return new Map([...D.questions,...D.checks,...D.vocab,...D.foundations,...D.orientation,...D.topicOrientation,...D.trueFalse,...D.cloze,...D.sorts].map(x=>[x.id,x]))}
function describeSessionItem(x){const result={id:x.id};for(const k of ['kind','options','bank','picked','current','foundation','preparingFor','q','exp'])if(x[k]!==undefined)result[k]=x[k];return result}
function restoreSessionItem(saved,catalog){
 const base=catalog.get(saved.id)||catalog.get(saved.id.replace(/-build$/,''));
 return base?{...base,...saved}:null;
}
function saveActiveSession(){
 if(!session||session.index>=session.items.length)return;
 try{
  const saved={version:1,mode:session.mode,section,index:session.index,total:session.total,right:session.right,cleared:[...session.cleared],first:session.first,graded:session.graded,lastOK:session.lastOK,revealed:session.revealed,lessonNumber:session.lessonNumber,items:session.items.map(describeSessionItem),initial:session.initial||session.items.map(describeSessionItem)};
  localStorage.setItem(SESSION425,JSON.stringify(saved));
 }catch{storageOK=false;stats()}
}
function readActiveSession(){
 try{
  const saved=JSON.parse(localStorage.getItem(SESSION425));
  if(!saved||saved.version!==1||!['practice','flash','exam'].includes(saved.mode)||!Array.isArray(saved.items)||!Number.isInteger(saved.index)||saved.index<0||saved.index>=saved.items.length)return null;
  const catalog=sessionCatalog(),items=saved.items.map(x=>restoreSessionItem(x,catalog));
  if(items.some(x=>!x)||!Array.isArray(saved.cleared)||!saved.first||!Number.isInteger(saved.total)||saved.total<1)return null;
  return {...saved,items};
 }catch{return null}
}
function savedSessionMarkup(){
 const saved=readActiveSession();if(!saved)return '';
 const x=saved.items[saved.index];
 return `<section class="card saved-practice" id="saved-practice"><span class="tag">SAVED PRACTICE</span><h2>Continue where you left off</h2><p><b>Question ${saved.index+1} of ${saved.items.length}</b> · ${saved.cleared.length} / ${saved.total} items completed</p><p>${esc(x.q)}</p><div class="actions"><button class="primary" id="resume-saved-practice">Resume saved ${saved.mode==='exam'?'exam':saved.mode==='flash'?'flashcards':'practice'}</button><button id="restart-saved-practice">Restart this session</button></div><p class="tiny">Restarting begins this session again. Completed lessons, vocabulary progress, and XP stay saved in this browser.</p></section>`;
}
function showSavedSession(){
 if(session)return;
 const html=savedSessionMarkup();if(!html)return;
 $('#app').insertAdjacentHTML('afterbegin',html);
 $('#resume-saved-practice').onclick=()=>resumeSavedSession(false);
 $('#restart-saved-practice').onclick=()=>resumeSavedSession(true);
}
function resumeSavedSession(restart=false){
 const saved=readActiveSession();if(!saved)return;
 section=Number.isInteger(saved.section)?saved.section:0;
 view=saved.mode==='flash'?'flash':saved.mode==='exam'?'exam':'practice';
 const catalog=sessionCatalog();
 if(restart){
  const initial=saved.initial||saved.items;
  const items=initial.map(x=>restoreSessionItem(x,catalog));if(items.some(x=>!x))return;
  session={mode:saved.mode,items:items.map(prepare),index:0,total:items.length,cleared:new Set(),first:{},right:0,graded:false,revealed:false,lessonNumber:saved.lessonNumber,initial};
 }else session={...saved,cleared:new Set(saved.cleared)};
 const wasGraded=!restart&&session.graded,wasRevealed=!restart&&session.revealed;
 renderSession();
 if(wasGraded){
  session.graded=true;session.lastOK=saved.lastOK;
  const x=session.items[session.index];
  document.querySelectorAll('[data-option],[data-blank-word],[data-blank-slot],#check-blanks,#clear-blanks,[data-move],#check-order,[data-word],[data-remove],#check-bank').forEach(b=>b.disabled=true);
  $('#feedback').innerHTML=feedback(x,session.lastOK)+'<button class="primary" id="next">Continue →</button>';
  $('#next').onclick=advance;
 }else if(wasRevealed&&session.mode==='flash'&&$('#flip'))$('#flip').onclick();
 saveActiveSession();$('#app').focus();window.scrollTo(0,0);
}
