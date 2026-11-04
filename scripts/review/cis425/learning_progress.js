function savedLessonStep(q){const value=progress.lessonSteps?.[q.id];return Number.isInteger(value)&&value>=0&&value<=2?value:0}
function lessonProgressBadge(number){
 const q=D.questions.find(q=>q.number===number);if(!q)return '';
 const done=!!progress.lessons[q.id],started=Object.hasOwn(progress.lessonSteps||{},q.id);
 return `<span class="lesson-state ${done?'is-complete':''}">${done?'✓ Completed':started?'Resume · Step '+(savedLessonStep(q)+1)+' of 3':'Not started'}</span>`;
}
function learningResumeCard(route){
 const list=route?route.map(n=>D.questions.find(q=>q.number===n)).filter(Boolean):learningSequence(),last=progress.lastLesson;
 const q=list.find(q=>q.number===last?.number)||list.find(q=>!progress.lessons[q.id]);
 if(!q)return '<p class="lesson-completed" role="status">✓ All lessons in this selection completed</p>';
 const step=savedLessonStep(q),visited=Object.hasOwn(progress.lessonSteps||{},q.id);
 return `<section class="card learning-resume"><span class="tag">${visited?'YOUR SAVED PLACE':'UP NEXT'}</span><h2>${esc(q.title)}</h2><p>Lesson ${q.number} · ${visited?'Step '+(step+1)+' of 3':'Not started'}${progress.lessons[q.id]?' · Completed — available to review':''}</p><button class="primary" data-lesson="${q.number}">${visited?'Resume this lesson':'Start learning'} →</button><p class="tiny">Your place and completed lessons save in this browser.</p></section>`;
}
