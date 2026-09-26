from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[3];s=(ROOT/'dist/cis304.js').read_text()
s=s.replace('CIS 304','CIS 464').replace('cis304','cis464').replace('KEY304','KEY464').replace('304-','464-').replace('module1-v1','chapters-v1').replace('ENTERPRISE ARCHITECTURE','PROJECT MANAGEMENT').replace('Module I','Chapters 1, 2, 3 & 10')
s=s.replace("let D,section=0", "let D,SLIDES,section=0")
s=s.replace("['readings','↗','Assigned readings']","['readings','↗','Slides & sources']").replace("['guide','☷','Full answered guide']","['guide','☷','Complete study reference']").replace("['math','#','Formula lab']","['math','#','Financial lab']")
s=s.replace('guide prompts','lesson checks').replace('original prompts','slide topics').replace('original guide prompt','slide topic').replace('original prompt','slide topic').replace('study-guide prompts','chapter checks').replace('study-guide answer','chapter explanation').replace('study-guide connection','slide connection').replace('Study-guide flashcards','Chapter flashcards').replace('Study guide cards','Study chapter cards').replace('Study questions','Study chapter cards').replace('Study-guide','Chapter').replace('Practice the study guide','Practice the chapters').replace('same guide topics','same chapter topics').replace('guide topics','chapter topics').replace('guide questions','chapter questions')
s=s.replace('Guide ${q.number} / 51','Lesson ${q.number} / ${D.questions.length}')
s=s.replace('${[15,16,17].includes(number)?', '${[30,31,32,33,34,35].includes(number)?').replace('Open the step-by-step formula lab','Open the step-by-step financial lab')
s=s.replace('${s.id}. ${esc(s.title)}','Chapter ${s.id} · ${esc(s.title)}')
# Remove CIS 304-specific context labels and acronym disambiguators.
s=s.replace('${x.number&&({24:1,25:1,26:1,46:1,48:1})[x.number]?`<p class="tiny muted">${esc(({24:"Comparing BPM, BPI, and BPR",25:"Comparing BPM, BPI, and BPR",26:"Choosing BPI or BPR",46:"FAIS and EIS",48:"Enterprise Resource Planning"})[x.number])}</p>`:""}','')
s=s.replace('${["PI","AI","PO","AO"].includes(x.term)?"In the process-measurement formulas, build":"Build"}', 'Build').replace('${["PI","AI","PO","AO"].includes(v.term)?"In the process-measurement formulas, build":"Build"}', 'Build').replace('${["PI","AI","PO","AO"].includes(v.term)?"In the process-measurement formulas":"In this CIS 464 course"}', 'In this CIS 464 course')
s=s.replace("const label=x=>`Chapters 1, 2, 3 & 10 · ${sec(x.section).title}`;", "const label=x=>`Chapter ${x.section} · ${sec(x.section).title}`;")
s=s.replace('Chapters 1, 2, 3 & 10 topic <select','Chapter <select')
replacements={
'sources':'''function sources(x){const q=source(x);if(!q)return '';return `<details class="question-source"><summary>Source & chapter connection</summary><p>Schwalbe Chapter ${q.section}, slide${q.slides.length===1?'':'s'} ${q.slides.join(', ')}.</p><p class="source-note">Explanation and practice authored from your supplied slides, with linked clarifications where needed. These are study aids, not an instructor-issued answer key.</p>${D.references.filter(r=>r.questions.includes(q.number)).map(r=>`<p><a href="${esc(r.url)}" target="_blank" rel="noreferrer">${esc(r.title)}</a></p>`).join('')}<button data-source-chapter="${q.section}" data-source-slide="${q.slides[0]}">See source slide material</button></details>`}''',
'guideHome':'''function guideHome(){$('#app').innerHTML=heading('Your complete chapter reference','Every lesson has its full explanation, a concrete example, and slide references. Use Slides & sources for all original slide material.')+`<div class="notice">${filtered(D.questions).length} of ${D.questions.length} lesson topics shown. Chapter 2 formulas keep money amounts, ratios, timing conventions, and rounding separate. Chapter 10 distinguishes course examples and forecasts from established definitions.</div><div class="lesson-list">${filtered(D.questions).map(q=>`<article class="card"><span class="tag">${label(q)}</span><h3>${esc(q.title)}</h3><details><summary>${esc(q.q)}</summary><div class="lesson-copy">${paragraphs(q.answer)}<h3>Let’s make it simple</h3>${paragraphs(q.teach)}<h3>Example</h3>${paragraphs(q.example)}</div>${sources(q)}<div class="actions"><button data-lesson="${q.number}">Teach me step by step</button><button data-question="${q.number}">Practice this topic</button></div></details></article>`).join('')}</div>`}'''
}
lines=[line for line in s.splitlines() if not line.startswith(('function readingsHome(', 'function readingLink('))]
for i,line in enumerate(lines):
 for name,replacement in replacements.items():
  if line.startswith('function '+name+'('):lines[i]=replacement
s='\n'.join(lines)+'\n'
s=s.replace('Your study guide sets the scope: all 51 prompts are included. The four sections below follow the refresher and Reading Sets 1–3. Added checks practice these same topics.', 'Your four slide decks set the scope. Lessons are organized by Chapters 1, 2, 3, and 10. The slide library retains all 183 slides, including diagrams, images, and classroom prompts.')
s=s.replace('Every original guide prompt has its own lesson.','Each topic is tied to its chapter and source slides.').replace('Every original guide topic has its own lesson.','Each topic is tied to its chapter and source slides.')
s=s.replace('The full answer after each question covers all parts of the original prompt.','The full explanation after each question connects the answer to its chapter topic.')
s=s.replace('Every slide topic has its own lesson.','Each lesson connects to its chapter and source slides.')
s=s.replace('All 51','All chapter').replace('51 original','chapter')
# Drop the other class’s numeric engine and concept map entirely.
s=s[:s.index('let mathCase=null')]+(ROOT/'scripts/review/cis464/activities.js').read_text()+'\n'+s[s.index("document.addEventListener('click'"):]
s=s.replace("else if(b.dataset.lesson)openLesson", "else if(b.dataset.sourceChapter){section=+b.dataset.sourceChapter;view='readings';session=null;chrome();readingsHome(+b.dataset.sourceSlide)}else if(b.dataset.lesson)openLesson")
start=s.index("fetch('cis464-content.json'")
s=s[:start]+'''Promise.all([fetch('cis464-content.json',{cache:'no-store'}),fetch('cis464-slides.json',{cache:'no-store'})].map(async r=>{const response=await r;if(!response.ok)throw Error('Content unavailable');return response.json()})).then(([data,slides])=>{D=data;SLIDES=slides;render()}).catch(()=>{$('#app').innerHTML='<section class="card"><h1>Study content could not load</h1><p>Refresh to retry loading the CIS 464 chapter content and slides.</p><button onclick="location.reload()">Try again</button></section>'});\n'''
(ROOT/'dist/cis464.js').write_text(s)
