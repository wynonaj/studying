"""Derive CIS 425 interactions from the proven no-typing class study engine."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
s = (ROOT / 'dist' / 'cis304.js').read_text()
s = s.replace('CIS 304', 'CIS 425').replace('cis304', 'cis425').replace('KEY304', 'KEY425')
s = s.replace('304-', '425-').replace('module1-v1', 'lectures-v1')
s = s.replace('ENTERPRISE ARCHITECTURE', 'DEFENSIVE CYBERSECURITY').replace('Module I', 'Lectures 1–8')
s = s.replace("const label=x=>`Lectures 1–8 · ${sec(x.section).title}`;", "const label=x=>`Lecture ${x.section} · ${sec(x.section).title}`;")
s = s.replace('Lectures 1–8 topic <select', 'Lecture <select')
s = s.replace("const navs=[['teach','☀','Learn First'],['practice','◈','Practice'],['flash','▤','Flashcards'],['map','▧','See the connections'],['exam','✓','Practice exam']];",
              "const navs=[['teach','☀','Learn First'],['practice','◈','Practice'],['flash','▤','Flashcards'],['exam','✓','Practice exam']];")
s = s.replace("const focused=[['apply','◎','Apply your knowledge'],['sort','≋','Sorting & sequences'],['abbrev','⌁','Abbreviations'],['math','#','Formula lab']];",
              "const focused=[['apply','◎','Apply your knowledge'],['sort','≋','Sorting & sequences'],['abbrev','⌁','Abbreviations']];")
s = s.replace("const reference=[['terms','Aa','Terms & definitions'],['guide','☷','Full answered guide'],['readings','↗','Assigned readings']];",
              "const reference=[['terms','Aa','Terms & definitions'],['guide','☷','Complete lecture reference']];")
s = s.replace("const fn={teach:teachHome,practice:practiceHome,flash:flashHome,map:mapHome,exam:examHome,apply:applyHome,sort:sortHome,abbrev:abbrevHome,math:mathHome,terms:termsHome,guide:guideHome,readings:readingsHome}[view];",
              "const fn={teach:teachHome,practice:practiceHome,flash:flashHome,exam:examHome,apply:applyHome,sort:sortHome,abbrev:abbrevHome,terms:termsHome,guide:guideHome}[view];")
s = s.replace('Guide ${q.number} / 51', 'Lesson ${q.number} / ${D.questions.length}')
s = s.replace('${s.id}. ${esc(s.title)}', 'Lecture ${s.id} · ${esc(s.title)}')
s = s.replace('${[15,16,17].includes(number)?\'<p><button data-view="math">Open the step-by-step formula lab</button></p>\':\'\'}', '')
s = s.replace('${x.number&&({24:1,25:1,26:1,46:1,48:1})[x.number]?`<p class="tiny muted">${esc(({24:"Comparing BPM, BPI, and BPR",25:"Comparing BPM, BPI, and BPR",26:"Choosing BPI or BPR",46:"FAIS and EIS",48:"Enterprise Resource Planning"})[x.number])}</p>`:""}', '')
s = s.replace('${["PI","AI","PO","AO"].includes(x.term)?"In the process-measurement formulas, build":"Build"}', 'Build')
s = s.replace('${["PI","AI","PO","AO"].includes(v.term)?"In the process-measurement formulas, build":"Build"}', 'Build')
s = s.replace('${["PI","AI","PO","AO"].includes(v.term)?"In the process-measurement formulas":"In this CIS 425 course"}', 'In this CIS 425 course')

def replace_function(name, replacement):
    global s
    lines = s.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f'function {name}('):
            lines[i] = replacement
            s = '\n'.join(lines) + '\n'
            return
    raise RuntimeError(f'Function {name} not found')


replace_function('sources', '''function sources(x){const q=source(x);if(!q)return '';return `<details class="question-source"><summary>Lecture source</summary><p>Lecture ${q.section}, slide${q.slides.length===1?'':'s'} ${q.slides.join(', ')}.</p><p class="source-note">The supplied lecture decks define the topic. The plain-language explanation and practice are study aids, not an instructor-issued answer key.</p></details>`}''')
replace_function('teachHome', '''function teachHome(){const sections=section?D.sections.filter(s=>s.id===section):D.sections;$('#app').innerHTML=heading('Understand the defense before you memorize the term.','Every lesson defines the words, explains the actual action, and connects back to the supplied lecture slides.')+`<div class="notice">All eight supplied lecture decks set the scope. ${D.questions.length} lessons cover the lecture concepts, while focused questions break devices, attacks, protocols, and defenses into smaller pieces.</div>`+sections.map(s=>{const qs=D.questions.filter(q=>q.section===s.id),done=qs.filter(q=>progress.lessons[q.id]).length;return `<section class="card" style="margin-top:22px"><span class="tag">${esc(s.reading)}</span><h2>Lecture ${s.id} · ${esc(s.title)}</h2><p>${esc(s.intro)}</p><div class="bar"><span style="width:${100*done/qs.length}%"></span></div><p class="tiny">${done} / ${qs.length} lessons completed</p><div class="lesson-list">${qs.map(q=>`<button data-lesson="${q.number}"><span class="badge">${q.number}</span><span class="lesson-label">${esc(q.title)}<small>${esc(q.q)}</small></span><span aria-label="${progress.lessons[q.id]?'Completed':'Not completed'}">${progress.lessons[q.id]?'✓':'→'}</span></button>`).join('')}</div></section>`}).join('')}''')
replace_function('guideHome', '''function guideHome(){$('#app').innerHTML=heading('Complete lecture reference','Review each topic with its answer, beginner explanation, example, and exact lecture-slide source.')+`<div class="notice">${filtered(D.questions).length} of ${D.questions.length} lesson topics shown. Lecture-slide wording that reflects older products or practices is explained in its course context; use current organizational policy for real security work.</div><div class="lesson-list">${filtered(D.questions).map(q=>`<article class="card"><span class="tag">${label(q)} · Slide${q.slides.length===1?'':'s'} ${q.slides.join(', ')}</span><h3>${esc(q.title)}</h3><details><summary>${esc(q.q)}</summary><div class="lesson-copy">${paragraphs(q.answer)}<h3>Let’s make it simple</h3>${paragraphs(q.teach)}<h3>Picture the action</h3>${paragraphs(q.example)}</div>${sources(q)}<div class="actions"><button data-lesson="${q.number}">Teach me step by step</button><button data-question="${q.number}">Practice this topic</button></div></details></article>`).join('')}</div>`}''')

# Remove reference functions that belong only to CIS 304.
s = '\n'.join(line for line in s.splitlines() if not line.startswith(('function readingsHome(', 'function readingLink('))) + '\n'

# Drop the CIS 304 formula engine and enterprise-architecture map.
start = s.index('let mathCase=null')
end = s.index("document.addEventListener('click'")
s = s[:start] + s[end:]

# Include every direct term check in chapter practice; missed items still return later.
s = s.replace('function sectionCards(){', "function lecturePracticePool(){return [...D.questions,...D.vocab]}\nfunction sectionCards(){")
s = s.replace('const qs=D.questions.filter(q=>q.section===s.id),done=qs.filter(completed).length',
              'const qs=lecturePracticePool().filter(q=>q.section===s.id),done=qs.filter(completed).length')
s = s.replace('function practiceHome(){const pool=filtered(D.questions)',
              'function practiceHome(){const pool=filtered(lecturePracticePool())')
s = s.replace("view='practice';start('practice',shuffle(filtered(D.questions)))",
              "view='practice';start('practice',shuffle(filtered(lecturePracticePool())))")
s = s.replace('guide prompts answered correctly', 'lesson and term questions answered correctly')
s = s.replace('guide prompts completed', 'lesson and term questions completed')
s = s.replace('One correct answer fills that prompt’s completion credit. Extra practice and vocabulary are tracked separately.',
              'Direct questions on every vocabulary term are included. Missed items return later until you answer them correctly.')
s = s.replace('The full answer after each question covers all parts of the original prompt.',
              'The explanation after each answer connects the choice to the relevant defensive action.')
s = s.replace('Practice the study guide', 'Practice the lectures')
s = s.replace('Original study-guide prompts', 'Lecture lesson questions')
s = s.replace('Guide + detailed understanding checks', 'Lessons + detailed understanding checks')
s = s.replace('Study guide cards', 'Lecture cards').replace('Study-guide flashcards', 'Lecture flashcards')
s = s.replace('same guide topics', 'same lecture topics').replace('guide topics', 'lecture topics')
s = s.replace('guide prompts', 'lesson questions').replace('original guide prompt', 'lecture topic')
s = s.replace('study-guide answer', 'lecture explanation').replace('study-guide connection', 'lecture connection')
s = s.replace('All 51 prompts. Fully answered.', 'All lecture topics, fully explained.')
s = s.replace("fetch('cis425-content.json',{cache:'no-store'}).then", "fetch('cis425-content.json',{cache:'no-store'}).then")
s = s.replace('CIS 425 needs cis425-content.json alongside this page.', 'CIS 425 needs cis425-content.json alongside this page.')

(ROOT / 'dist' / 'cis425.js').write_text(s)
print('Built dist/cis425.js')

