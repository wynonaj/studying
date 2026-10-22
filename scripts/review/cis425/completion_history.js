function completedSetKey(mode,ids){return mode+':'+[...new Set(ids)].sort().join('|')}
function completionReady(s){return s.mode==='exam'?s.index>=s.items.length:s.cleared.size===s.total}
function rememberCompletedSession(s){
 if(!s||!completionReady(s))return null;
 const ids=(s.initial||s.items).map(x=>x.id),key=completedSetKey(s.mode,ids);
 progress.completedSessions??=[];
 let record=progress.completedSessions.find(x=>x.key===key);
 if(s.completionRecorded)return record;
 const number=s.lessonNumber,q=D.questions.find(q=>q.number===number);
 const title=q?q.title:s.mode==='exam'?'Practice exam':s.mode==='flash'?'Flashcard session':'Practice session';
 const result={key,title,mode:s.mode,total:s.total,right:s.right,itemIds:[...new Set(ids)],lessonNumber:number,finishedAt:Date.now(),attempts:(record?.attempts||0)+1};
 if(record)Object.assign(record,result);else{record=result;progress.completedSessions.push(record)}
 s.completionRecorded=true;save();return record;
}
function completionBanner(s){
 if(!completionReady(s))return '';
 rememberCompletedSession(s);
 return `<section class="completion-success" role="status"><h2>✓ ${s.mode==='exam'?'Exam finished':'Completed'}</h2><p>${s.mode==='exam'?`${s.right} of ${s.total} correct on first attempts.`:`All ${s.total} items in this session completed.`}</p><p>This completion is saved. Restarting creates a new attempt and keeps this record.</p><button data-completion-list="true">View saved completions</button></section>`;
}
function completedSessionMarkup(){
 const records=progress.completedSessions||[];
 if(!records.length)return '';
 return `<section class="card completed-history"><h2>✓ Saved completions</h2><p>${records.length} completed practice set${records.length===1?'':'s'}. These records remain when you restart.</p>${[...records].sort((a,b)=>b.finishedAt-a.finishedAt).map(r=>`<article class="completed-record"><span class="lesson-completed">✓ ${r.mode==='exam'?'Exam finished':'Completed'}</span><h3>${esc(r.title)}</h3><p>${r.total} items · ${r.mode==='exam'?`${r.right} correct on first attempts`:'All items completed'} · ${new Date(r.finishedAt).toLocaleString('en-US',{timeZone:'America/New_York'})}</p><button data-view-completion="${esc(r.key)}">View completed session</button></article>`).join('')}</section>`;
}
function viewCompletedSession(key){
 const r=(progress.completedSessions||[]).find(r=>r.key===key);if(!r)return;
 session=null;view='practice';chrome();
 $('#app').innerHTML=`<section class="card completed-history"><span class="lesson-completed">✓ ${r.mode==='exam'?'Exam finished':'Completed'}</span><h1>${esc(r.title)}</h1><p>${r.mode==='exam'?`${r.right} of ${r.total} correct on first attempts.`:`You completed all ${r.total} items in this set.`}</p><p>This saved result remains available after restarting or closing the tab.</p><div class="actions"><button data-completion-list="true">All saved completions</button><button data-review-completion="${esc(r.key)}">Review this set again</button><button data-view="practice">Back to practice</button></div></section>`;
 window.scrollTo(0,0);
}
function reviewCompletedSession(key){
 const r=(progress.completedSessions||[]).find(r=>r.key===key);if(!r)return;
 const catalog=sessionCatalog(),items=r.itemIds.map(id=>catalog.get(id)||catalog.get(id.replace(/-build$/,''))).filter(Boolean);
 if(items.length)start(r.mode,items,r.lessonNumber);
}
function showCompletionList(){session=null;view='practice';chrome();$('#app').innerHTML=completedSessionMarkup()+'<button data-view="practice">Back to practice</button>';window.scrollTo(0,0)}
function restoreBeforeRestart(){
 try{const old=localStorage.getItem(SESSION425+'-before-restart');if(!old)return;localStorage.setItem(SESSION425,old);resumeSavedSession(false)}catch{storageOK=false;stats()}
}
