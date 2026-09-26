const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const data=JSON.parse(read('dist/cis304-content.json')),prompts=JSON.parse(read('scripts/review/cis304/guide-prompts.json'));
assert.equal(data.questions.length,51);assert.deepEqual(data.questions.map(q=>q.q),prompts);
assert.deepEqual(data.sections.map(s=>data.questions.filter(q=>q.section===s.id).length),[10,16,11,14]);
const all=[...data.questions,...data.vocab,...data.checks,...data.cloze];
assert.equal(new Set(all.map(x=>x.id)).size,all.length);
for(const x of all){assert.equal(x.distractors.length,3,x.id);assert.equal(new Set([x.correct,...x.distractors]).size,4,x.id);assert.ok(x.teach.length>40,x.id);assert.notEqual(x.teach,x.correct);assert.ok(data.sections.some(s=>s.id===x.section));if(x.source)assert.ok(data.questions.some(q=>q.number===x.source))}
for(const q of data.questions){assert.ok(q.answer.length>90);assert.ok(q.example.length>65);assert.ok(q.title);assert.ok(q.slides.every(s=>s>=1&&s<=54))}
for(const v of data.vocab.filter(v=>v.exp)){assert.equal(data.abbreviationDistractors[v.term].length,3);assert.equal(new Set([v.exp,...data.abbreviationDistractors[v.term]]).size,4)}
assert.equal(data.readings.length,40);assert.deepEqual([1,2,3].map(n=>data.readings.filter(r=>r.set===n).length),[18,13,9]);for(const r of data.readings)assert.match(r.url,/^https:\/\//);
assert.equal(data.questions[14].correct,'PI / AI');assert.equal(data.questions[15].correct,'AO / PO');assert.equal(data.questions[16].correct,'AO / AI');
assert.match(data.questions[18].answer,/Procurement:[\s\S]*Production:[\s\S]*Fulfillment:[\s\S]*Accounting:/);
assert.match(data.questions[31].answer,/on premises or in the cloud/);
assert.match(data.questions[27].answer,/does not supply a separate fixed list/);
const elements=new Map();function element(s){if(!elements.has(s))elements.set(s,{innerHTML:'',textContent:'',value:'',disabled:false,dataset:{},focus(){},setAttribute(){},insertAdjacentHTML(_,s){this.innerHTML+=s},classList:{add(){}}});return elements.get(s)}
const saved=new Map([['cis320-v1','untouched-320-progress']]);
const ctx=vm.createContext({console,Date,Math,JSON,Set,document:{querySelector:element,querySelectorAll:()=>[]},window:{scrollTo(){}},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)},INPUT:data});
vm.runInContext(read('dist/cis304.js').split("document.addEventListener('click'")[0],ctx);const run=s=>vm.runInContext(s,ctx);run('D=INPUT');
for(const v of ['teach','practice','flash','map','exam','apply','sort','abbrev','math','terms','guide','readings']){run(`navigate('${v}')`);assert.ok(element('#app').innerHTML.length>100,v)}
for(const q of data.questions){run(`openLesson(${q.number},0);openLesson(${q.number},1);openLesson(${q.number},2)`);assert.ok(element('#app').innerHTML.includes('Try this topic'))}
for(let i=0;i<300;i++){const result=JSON.parse(run(`JSON.stringify((()=>{const c=generateMath();return {c,next:generateMath(c),qs:mathQuestions(c)}})())`));assert.notDeepEqual(result.c,result.next);for(const q of result.qs){assert.equal(new Set([q.correct,...q.distractors]).size,4);assert.ok(q.example.includes(String(result.c.ao)))}assert.equal(result.qs[1].correct,run(`fmt(${result.c.pi/result.c.ai*100})`)+ '%');assert.equal(result.qs[2].correct,run(`fmt(${result.c.ao/result.c.po*100})`)+ '%');assert.equal(result.qs[3].correct,run(`fmt(${result.c.ao/result.c.ai})`)+ ' orders per hour')}
for(const x of data.sorts){ctx.SORT=x;for(let i=0;i<30;i++)assert.notEqual(run('JSON.stringify(shuffledOrder(SORT.items))'),JSON.stringify(x.items))}
run('section=0;start("practice",D.questions.slice(0,5));grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items[4].id'),'304-q01');assert.equal(run('session.cleared.size'),0);
run('while(session.index<session.items.length){grade(session.items[session.index],true,"correct");advance()}');assert.equal(run('session.cleared.size'),5);assert.equal(run('session.right'),4);assert.equal(saved.get('cis320-v1'),'untouched-320-progress');assert.ok(saved.has('cis304-module1-v1'));assert.equal(run('completed(D.questions[0])'),true);
run('start("exam",D.questions.slice(0,1));grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items.length'),1);assert.equal(run('session.right'),0);
run('start("flash",[D.questions[0]])');assert.ok(!element('#flip').innerHTML.includes('Data are individual facts'));element('#flip').onclick();assert.ok(element('#flip').innerHTML.includes('Data are individual facts'));element('#flip').onclick();assert.ok(!element('#flip').innerHTML.includes('Data are individual facts'));
run('start("practice",[{...D.sorts[0],kind:"sort"}])');assert.ok(element('#app').innerHTML.includes('Check order'));
run('start("practice",[{...D.vocab.find(v=>v.term==="ERP"),kind:"wordbank"}])');assert.equal(run('session.items[0].bank.length'),3);assert.ok(element('#app').innerHTML.includes('Check name'));
run('section=3');assert.ok(run('filtered(mixedPool()).every(x=>x.section===3)'));
const page320=read('dist/index.html'),page304=read('dist/cis304.html');assert.match(page320,/href="cis304.html"/);assert.match(page304,/href="index.html"/);assert.ok(!page304.includes('src="app.js'));assert.ok(!read('dist/cis304.js').includes("setItem('cis320"));
for(const page of [page320,page304])for(const match of page.matchAll(/(?:src|href)="([\w.-]+\.(?:js|css))\?v=([a-f0-9]+)"/g)){assert.equal(require('node:crypto').createHash('sha256').update(read('dist/'+match[1])).digest('hex').slice(0,12),match[2],match[1]+' cache hash')}
console.log('PASS: all 51 original prompts, 64 terms, 31 checks, 11 cloze cards, 40 links, source coverage, distinct choices, 300 formula rounds, shuffled sorts, all views/lessons, retry completion, exam scoring, flash flips, and isolated class progress.');
