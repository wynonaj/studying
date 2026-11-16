const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const D=JSON.parse(read('dist/cis464-test2-content.json'));
assert.equal(D.sections.length,4);assert.deepEqual(D.sections.map(x=>x.id),[4,5,6,7]);
const objectives=D.lessons.filter(x=>x.kind==='objective');
assert.equal(objectives.length,33,'all stated chapter objectives');
assert.deepEqual(D.sections.map(s=>objectives.filter(x=>x.section===s.id).length),[5,15,6,7]);
assert.equal(D.lessons.length,72,'objective, overview, and additional lessons');
assert.equal(D.questions.length,D.lessons.length,'one core question per lesson');
assert.ok(D.vocab.length>=350,'extensive study-guide term and comparison coverage');
assert.equal(D.sourceSummary.sourceLines,read('scripts/review/cis464-test2/study-guide.md').split(/\r?\n/).length);
assert.equal(D.sourceText,read('scripts/review/cis464-test2/study-guide.md'));
for(const phrase of ['Objective 5: Explain how to control scope creep','Cost objective 6: Conduct earned value management analysis','Objective 3: Explain how resource leveling works','Objective 7: Minimize the negative effects of conflict'])assert.ok(objectives.some(x=>x.title===phrase),phrase);
for(const phrase of ['MoSCoW prioritization','Critical distinctions','Risk management plan','Communication barriers','Psychological safety'])assert.ok(D.sourceText.includes(phrase),phrase);
for(const x of [...D.questions,...D.vocab,...D.checks]){assert.equal(x.distractors.length,3,x.id);assert.equal(new Set([x.correct,...x.distractors]).size,4,x.id);assert.ok(x.teach);assert.ok(x.answer);}
for(const x of D.lessons){assert.ok(x.html.length>20,x.title);assert.ok(x.summary.length>20,x.title);assert.ok(x.objective);}
assert.match(D.reviewHtml,/Every calculation you should practice/);
assert.ok(D.checks.some(x=>x.q.includes('communication channels')));assert.ok(D.checks.some(x=>x.q.includes('PERT')));assert.ok(D.checks.some(x=>x.q.includes('EMV')));
assert.ok(D.sorts.some(x=>x.title.includes('Tuckman')));assert.ok(D.cloze.some(x=>x.q.includes('RACI')));

const elements=new Map();function el(s){if(!elements.has(s))elements.set(s,{innerHTML:'',textContent:'',value:'0',disabled:false,dataset:{},focus(){},setAttribute(){},insertAdjacentHTML(_,v){this.innerHTML+=v},classList:{add(){}}});return elements.get(s)}
const saved=new Map([['cis464-chapters-v1','exam-one'],['cis320-test2-v1','networking']]);
const ctx=vm.createContext({console,Date,Math,JSON,Set,Intl,document:{querySelector:el,querySelectorAll:()=>[],addEventListener(){}},window:{scrollTo(){},CIS464_EXAM2_CONTENT:null},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)},INPUT:D});
const source=read('dist/cis464-test2.js').split("document.addEventListener('click'")[0];vm.runInContext(source,ctx);const run=s=>vm.runInContext(s,ctx);run('D=INPUT');
for(const view of ['teach','objectives','practice','flash','exam','apply','sort','cloze','terms','guide','sources']){run(`navigate('${view}')`);assert.ok(el('#app').innerHTML.length>100,view)}
for(const lesson of D.lessons){for(let step=0;step<3;step++)run(`openLesson(${lesson.number},${step})`);assert.match(el('#app').innerHTML,/Practice this lesson/)}
run('start("practice",D.questions.slice(0,3));grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items[4-1].id'),D.questions[0].id,'missed item returns after other items');
run('while(session.index<session.items.length){grade(session.items[session.index],true,session.items[session.index].correct);advance()}');assert.ok(saved.has('cis464-exam2-v1'));assert.equal(saved.get('cis464-chapters-v1'),'exam-one');
run('start("flash",[D.questions[0]])');assert.ok(!el('#app').innerHTML.includes(D.questions[0].correct));el('#flip').onclick();assert.ok(el('#app').innerHTML.includes(D.questions[0].correct));
run('start("practice",[{...D.sorts[0],kind:"sort"}])');assert.match(el('#app').innerHTML,/Check order/);
run('start("practice",[D.cloze[0]])');assert.match(el('#app').innerHTML,/Check sentence/);

const html=read('dist/cis464-test2.html'),exam1=read('dist/cis464.html'),classes=read('dist/classes.html');
assert.match(html,/cis464-test2-content\.js/);assert.match(html,/cis464\.html/);assert.match(exam1,/cis464-test2\.html/);assert.match(classes,/Exam 1 and Exam 2/);
assert.match(read('dist/cis464-test2-content.js'),/^window\.CIS464_EXAM2_CONTENT=/);
for(const page of fs.readdirSync(path.join(root,'dist')).filter(x=>x.endsWith('.html')).map(x=>read('dist/'+x)))for(const m of page.matchAll(/(?:src|href)="([^"?]+\.(?:js|css))\?v=([a-f0-9]+)"/g))assert.equal(m[2],crypto.createHash('sha256').update(read('dist/'+m[1])).digest('hex').slice(0,12),m[1]);
console.log(`PASS CIS 464 Exam 2: ${objectives.length} objectives, ${D.lessons.length} lessons, ${D.vocab.length} terms/comparisons, complete ${D.sourceSummary.sourceLines}-line guide, separate progress, retries, flashcards, blanks, sorts, and exams.`);
