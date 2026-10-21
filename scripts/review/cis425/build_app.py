from pathlib import Path
import re,hashlib,json
ROOT=Path(__file__).resolve().parents[3]
p=ROOT/'dist'
s=(p/'cis304.js').read_text(encoding='utf-8').replace('304','425').replace('KEY425','KEY425').replace('cis425-module1-v1','cis425-midterm-v1').replace('Module I','Midterm').replace('ENTERPRISE ARCHITECTURE','DEFENSIVE CYBERSECURITY').replace('51','45')
def replacefn(name,nextname,body):
 global s
 start=s.index('function '+name+'(');end=s.index('function '+nextname+'(',start)
 s=s[:start]+body+'\n'+s[end:]
replacefn('sources','picker',r'''function sources(x){const q=source(x);if(!q)return '';return `<details class="question-source"><summary>Sources and exam wording</summary>${q.sample?`<p><b>Professor sample: ${esc(q.sample)}</b></p>`:''}<p>${esc(q.q)}</p>${q.originalOptions?`<p>Original options: ${q.originalOptions.map(esc).join(' · ')}</p>`:''}${q.refs.map(([id,where])=>`<p class="source-note">${esc(D.sources.find(s=>s.id===id)?.name)} · ${esc(where)}</p>`).join('')}</details>`}''')
s=s.replace("['math','#','Formula lab']","['math','#','RSA & hash lab'],['discussion','◇','Discussion practice']").replace("['readings','↗','Assigned readings']","['readings','↗','Sources & corrections']")
s=s.replace('math:mathHome,terms:', 'math:mathHome,discussion:discussionHome,terms:')
s=s.replace('Your study guide sets the scope: all 45 prompts are included. The four sections below follow the refresher and Reading Sets 1–3. Added checks practice these same topics.','Midterm focus: textbook Chapters 1 and 3, Lectures 1–8, and relevant lab and in-class work. All 21 professor sample prompts are answered, followed by 24 supporting lessons. October 15 notes emphasize business use and defenses rather than memorizing tool commands. Start with the samples, then practice the supporting concepts.')
s=s.replace('Guide ${q.number} / 45','Lesson ${q.number} / 45').replace('guide prompts','lessons').replace('original prompts','lesson prompts').replace('All original topics are preserved. Questions name the concepts they refer to. Answers fill the blanks using course slides and supporting references.','Professor samples and supporting lessons, with complete answers, examples, and source labels.').replace('All 45 prompts. Fully answered.','The answered midterm guide')
s=s.replace('of 45 prompts shown. Short prompts are expanded so you can understand each question on its own. Slide 20 controls the course formulas. The EA properties answer is a synthesis because the materials do not name a separate fixed list.','of 45 lessons shown. Lessons 1–21 answer every professor sample in order. Four disputed or imprecise samples are explained but excluded from scored exams. Open Sources & corrections for the cross-check record.')
s=s.replace("${[15,16,17].includes(number)?", "${[19,39].includes(number)?").replace('Open the step-by-step formula lab','Open RSA & hash lab')
s=s.replace('Build layers & sequences','Build security sequences').replace('These are specific example sequences, not a claim that every business uses identical steps.','Conceptual workflows for the same midterm topics. These teach the reasoning rather than tool commands.').replace('Try: input, enterprise, ERP…','Try: TCP, signature, IDS…')
s=s.replace("const pool=filtered(D.questions),done=pool.filter(completed).length", "const pool=filtered(D.questions).filter(q=>!q.uncertain),done=pool.filter(completed).length")
s=s.replace("${x.number&&({24:1,25:1,26:1,46:1,48:1})[x.number]?`<p class=\"tiny muted\">${esc(({24:\"Comparing BPM, BPI, and BPR\",25:\"Comparing BPM, BPI, and BPR\",26:\"Choosing BPI or BPR\",46:\"FAIS and EIS\",48:\"Enterprise Resource Planning\"})[x.number])}</p>`:\"\"}", "${x.format?`<p class=\"tiny muted\">${esc(x.format==='tf'?'True / False':x.format==='fill'?'Fill-in-the-blank recognition':'Concept check')}</p>`:''}")
s=s.replace("function mixedPool(){return [...D.questions", "function mixedPool(){return [...D.questions.filter(q=>!q.uncertain)")
replacefn('readingsHome','readingLink',r'''function readingsHome(){$('#app').innerHTML=heading('Every source, with corrections','How the supplied material shapes the midterm section.')+`<div class="notice">All 11 sources are accounted for. The single-page CIS 425 - 827.pdf is the replacement you approved for the missing annotated file. The textbook was indexed across 786 PDF pages, with study scope limited to assigned chapters and guide-relevant definitions. Original textbook pages, private submissions, and lab attack instructions are not republished. The second guide describes eight lecture decks; those decks were not separately attached here, so lecture coverage uses its summaries cross-checked with your notes and labs.</div><section class="card"><h2>Exam scope and estimates</h2><p>Professor guide: 15 T/F, 20 multiple choice, 10 blanks, 5–7 discussions. October 15 notes give ranges: 10–15 T/F, 20–25 MC, 10–12 blanks, 5–7 discussions. Counts are estimates.</p><p>Prioritize explanations, technology choices, business impact, and defenses. Career recruiting lists and unrelated textbook chapters stay outside practice.</p></section><h2>Source coverage</h2>${D.sources.map(x=>`<details class="card"><summary>${x.id}. ${esc(x.name)}</summary><p>${esc(D.sourceUses[x.id])}</p><p class="tiny">${x.units} extracted page/slide/note units · ${x.chars.toLocaleString()} text characters${x.note?' · '+esc(x.note):''}</p></details>`).join('')}<h2>Cross-check of the second guide and class materials</h2>${D.corrections.map(([status,title,text])=>`<article class="card"><span class="tag">${esc(status)}</span><h3>${esc(title)}</h3><p>${esc(text)}</p></article>`).join('')}<section class="card"><h2>Primary clarification references</h2><p>The supplied course material sets scope. These references clarify technical terminology. Linked videos are not represented as watched or transcribed.</p><ul>${D.references.map(r=>`<li><a href="${esc(r.url)}" target="_blank" rel="noreferrer">${esc(r.title)}</a></li>`).join('')}</ul></section>`}''')
replacefn('examHome','mathHome',r'''function examHome(){$('#app').innerHTML=heading('Practice the exam format','First answers count. These are authored practice questions, not predicted exam questions.')+`<section class="card"><h2>Midterm rehearsal</h2><p>15 true/false + 20 multiple choice + 10 fill-in-the-blank choices. Then rehearse 6 discussion answers using the separate rubric. Discussion ratings are self-assessment and never added to your objective score.</p><p>Use the answer explanations to review missed concepts, then practice recalling them without choices.</p><div class="actions"><button class="primary" id="mock-exam">Start 45-question rehearsal</button><button id="topic-exam">20 questions from selected topic</button><button data-view="discussion">Discussion rehearsal</button></div></section>`;$('#mock-exam').onclick=()=>{section=0;const tf=shuffle(D.trueFalse).slice(0,15),mc=shuffle(D.questions.filter(q=>!q.uncertain&&!['tf','fill','discussion'].includes(q.format))).slice(0,20),bl=shuffle(D.cloze).slice(0,10);start('exam',[...tf,...mc,...bl])};$('#topic-exam').onclick=()=>{const pool=filtered([...D.questions.filter(q=>!q.uncertain&&!['tf','fill','discussion'].includes(q.format)),...D.trueFalse,...D.cloze]);start('exam',shuffle(pool).slice(0,20))}}''')
# Remove obsolete formula and enterprise map implementations completely.
start=s.index('function mathHome(');end=s.index("document.addEventListener('click'",start)
s=s[:start]+(Path(__file__).parent/'activities.js').read_text(encoding='utf-8')+'\n'+s[end:]
# The audit adds beginner, exact-example, coverage, and discussion views.
start=s.index('function discussionHome(');end=s.index('const mapViews=',start)
s=s[:start]+s[end:]
insert=s.index("document.addEventListener('click'")
s=s[:insert]+(Path(__file__).parent/'audit_views.js').read_text(encoding='utf-8')+'\n'+s[insert:]
s=s.replace("const navs=[", "const navs=[['beginner','○','Start from zero'],['samples','☷','Professor examples'],['coverage','✓','Topic checklist'],")
s=s.replace('const fn={teach:', 'const fn={beginner:beginnerHome,samples:samplesHome,coverage:coverageHome,teach:')
s=s.replace('function navigate(v){view=v;', 'function navigate(v){$("#nav").setAttribute("data-menu-open","false");$("#study-menu").setAttribute("aria-expanded","false");view=v;')
s=s.replace('function picker(){return', 'function picker(){if(["beginner","samples","coverage","readings"].includes(view))return `<p class="tiny muted">Whole midterm</p>`;return')
s=s.replace('Every original guide prompt has its own lesson.','Study one concept at a time, then explain it in a scenario.')
s=s.replace('All 21 professor sample prompts are answered, followed by 24 supporting lessons.','All 21 professor examples are answered, with focused supporting lessons from direct review of all eight lecture decks and assigned textbook sections.')
s=s.replace('Start with the samples, then practice the supporting concepts.</div>', 'New to security? Start from zero. Then use Professor examples and the Topic checklist to connect each source to practice.</div><div class="actions"><button data-view="beginner">Start from zero</button><button data-view="samples">All 21 professor examples</button><button data-view="coverage">Chapter & lecture checklist</button></div>')
s=s.replace('Lesson ${q.number} / 45','Lesson ${q.number} / ${D.questions.length}')
s=s.replace('of 45 lessons shown. Lessons 1–21 answer every professor sample in order.','of ${D.questions.length} lessons shown. Lessons 1–21 answer every professor sample in order.')
s=s.replace('All 11 sources are accounted for.','All ${D.sources.length} source records are accounted for, including the original 11 references and all eight lecture decks.')
s=s.replace('The second guide describes eight lecture decks; those decks were not separately attached here, so lecture coverage uses its summaries cross-checked with your notes and labs.','All eight lecture decks are now reviewed directly. Lectures 2–4 were recovered from PPTs_export.zip, and the duplicate Lecture 3 export has matching slide/note text. The original annotated exercise is now available too and matches the replacement text. Use Topic checklist for source-to-lesson links.')
s=s.replace('Then rehearse 6 discussion answers using the separate rubric.','Then choose 5 or 7 discussion prompts using the separate rubric.')
s=s.replace("const tf=shuffle(D.trueFalse).slice(0,15),mc=shuffle(D.questions.filter(q=>!q.uncertain&&!['tf','fill','discussion'].includes(q.format))).slice(0,20),bl=shuffle(D.cloze).slice(0,10);start('exam',[...tf,...mc,...bl])", "start('exam',buildMidtermItems())")
s=s.replace('${paragraphs([q.teach,q.answer,q.example][step])}', '${step===0?`<p class="notice"><b>Your goal:</b> ${esc(q.goal)}</p><p><button data-view="beginner">Explain the starting vocabulary</button></p>`:""}${paragraphs([q.teach,q.answer,q.example][step])}')
s=s.replace("<button id=\"blank-practice\">Fill in the blanks</button>","<button id=\"blank-practice\">Fill-in-the-blank choices</button><button id=\"recall-blanks\">Recall blanks before revealing</button>")
s=s.replace("$('#blank-practice').onclick=", "$('#recall-blanks').onclick=()=>start('flash',shuffle(filtered(D.cloze)));$('#blank-practice').onclick=")
# Supplementary scenario checks participate in mixed and source-scoped practice.
s=s.replace('...D.vocab,...D.cloze,','...D.checks,...D.vocab,...D.cloze,')
s+='\n$("#study-menu").onclick=()=>{const open=$("#study-menu").getAttribute("aria-expanded")!=="true";$("#study-menu").setAttribute("aria-expanded",String(open));$("#nav").setAttribute("data-menu-open",String(open))};\n'
s=s.replace('CIS 425 needs cis425-content.json alongside this page.','CIS 425 needs cis425-content.json alongside this page.')
# Class-specific source getter for generated practice items.
s=s.replace('const source=x=>x.number?x:D.questions.find(q=>q.number===x.source);','const source=x=>x.number?x:D.questions.find(q=>q.number===x.source);')
s=s.replace('<button id="lesson-complete">${progress.lessons[q.id]?\'✓ Lesson completed\':\'Mark lesson read\'}</button>', '${progress.lessons[q.id]?\'<span class="lesson-completed" role="status">✓ Lesson completed</span>\':\'<button id="lesson-complete">Mark lesson read</button>\'}')
s=s.replace('function openLesson(number,step=0){', 'function openLesson(number,step=null){const target=D.questions.find(q=>q.number===number);if(!target)return;if(step===null)step=savedLessonStep(target);step=Math.max(0,Math.min(2,Number.isInteger(step)?step:0));progress.lessonSteps??={};progress.lessonSteps[target.id]=step;progress.lastLesson={number,section};save();')
s=s.replace('openLesson(next.number);window.scrollTo', 'openLesson(next.number,0);window.scrollTo')
s=s.replace('<button data-lesson="${q.number}"><span class="badge">', '<button data-lesson="${q.number}" class="${progress.lessons[q.id]?\'lesson-is-complete\':\'\'}"><span class="badge">')
s=s.replace('<span aria-label="${progress.lessons[q.id]?\'Completed\':\'Not completed\'}">${progress.lessons[q.id]?\'✓\':\'→\'}</span>', '<span class="lesson-state ${progress.lessons[q.id]?\'is-complete\':\'\'}">${progress.lessons[q.id]?\'✓ Completed\':Object.hasOwn(progress.lessonSteps||{},q.id)?\'Resume · Step \'+(savedLessonStep(q)+1)+\' of 3\':\'Not started →\'}</span>')
s=s.replace('</div>`+sections.map(s=>', '</div>`+learningResumeCard()+sections.map(s=>')
insert=s.index("document.addEventListener('click'")
s=s[:insert]+(Path(__file__).parent/'learning_progress.js').read_text(encoding='utf-8')+'\n'+s[insert:]
# Every lesson link shares the same persisted status, across all study views.
def lesson_link_status(match):
 opening,value,body,closing=match.groups()
 if 'lesson-state' in body or 'Resume this lesson' in body:return match.group(0)
 expression=value[2:-1] if value.startswith('${') and value.endswith('}') else value
 return opening+body+' ${lessonProgressBadge('+expression+')}'+closing
s=re.sub(r'(<button\b[^>]*data-lesson="([^"]+)"[^>]*>)(.*?)(</button>)',lesson_link_status,s,flags=re.S)
s=s.replace("heading('Start from zero','Build the vocabulary first, then follow one connected route through the midterm.')+", "heading('Start from zero','Build the vocabulary first, then follow one connected route through the midterm.')+learningResumeCard(D.beginnerRoute)+")
(p/'cis425.js').write_text(s,encoding='utf-8')
h=(p/'cis304.html').read_text(encoding='utf-8')
h=h.replace('CIS 304 · Recall Lab','CIS 425 · Recall Lab').replace('CIS 304 Module I: all 51 study-guide prompts, beginner lessons, flashcards, process practice and exams.','CIS 425 defensive cybersecurity midterm: answered guide, lessons, labs, flashcards and exam rehearsal.')
h=h.replace('CIS 304 / MODULE I','CIS 425 / MIDTERM').replace('href="cis304.html" class="brand"','href="cis425.html" class="brand"').replace('CIS 304 progress','CIS 425 progress').replace('Loading CIS 304','Loading CIS 425').replace('cis304.js?v=6a55889e690e','cis425.js')
h=h.replace('href="cis304.html" aria-current="page"','href="cis304.html"')
h=h.replace('class="cis304"','class="cis304 cis425"').replace('</head>','<link rel="stylesheet" href="cis425.css"></head>')
h=h.replace('<nav id="nav"','<button id="study-menu" aria-controls="nav" aria-expanded="false">Study menu</button><nav id="nav"')
h=re.sub(r'<a href="cis425.html"[^>]*>CIS 425 <small>Defensive cybersecurity</small></a>','',h)
nav='<a href="cis425.html" aria-current="page">CIS 425 <small>Defensive cybersecurity</small></a>'
h=h.replace('</nav><div id="stats">',nav+'</nav><div id="stats">')
(p/'cis425.html').write_text(h,encoding='utf-8')
for name in ['index.html','cis304.html','cis464.html']:
 f=p/name;t=f.read_text(encoding='utf-8')
 if 'href="cis425.html"' not in t:t=t.replace('</nav><div id="stats">','<a href="cis425.html">CIS 425 <small>Defensive cybersecurity</small></a></nav><div id="stats">')
 f.write_text(t,encoding='utf-8')
f=p/'classes.html';t=f.read_text(encoding='utf-8').replace('THREE SEPARATE CLASSES','FOUR SEPARATE CLASSES')
if 'href="cis425.html"' not in t:t=t.replace('</div></main>','<a class="class-entry" href="cis425.html"><span class="c-tag">DEFENSIVE CYBERSECURITY</span><strong>CIS 425</strong><h2>Prepare for the midterm</h2><span>Answered professor guide, security concepts, lab scenarios, cryptography and exam practice.</span><span>Open class →</span></a></div></main>')
f.write_text(t,encoding='utf-8')
f=p/'classes.html';t=f.read_text(encoding='utf-8')
card=re.search(r'<a class="class-entry" href="cis425.html">.*?</a>',t).group(0)
t=t.replace(card,'').replace('</div><div class="c-note">',card+'</div><div class="c-note">')
f.write_text(t,encoding='utf-8')
for asset in list(p.glob('*.js'))+list(p.glob('*.css')):
 asset.write_text(asset.read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
for f in p.glob('*.html'):
 t=f.read_text(encoding='utf-8')
 for match in list(re.finditer(r'(?:src|href)="([\w.-]+\.(?:js|css))(?:\?v=[a-f0-9]+)?"',t)):
  asset=match.group(1);digest=hashlib.sha256((p/asset).read_bytes()).hexdigest()[:12]
  t=re.sub(re.escape(asset)+r'(?:\?v=[a-f0-9]+)?',asset+'?v='+digest,t)
 f.write_text(t,encoding='utf-8')
print('CIS 425 page and class navigation built')
