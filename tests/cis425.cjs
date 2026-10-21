const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const D=JSON.parse(read('dist/cis425-content.json'));
assert.equal(D.questions.length,84);assert.equal(D.sources.length,19);
assert.deepEqual(D.sources.map(x=>x.id),Array.from({length:19},(_,i)=>i+1));
assert.equal(D.sources.find(x=>x.id===3).units,786);
assert.equal(D.sources.find(x=>x.id===10).name,'CIS 425 - 827.pdf');
assert.equal(D.questions.filter(q=>q.sample).length,21);
assert.deepEqual(D.questions.filter(q=>q.uncertain).map(q=>q.number),[3,4,10,13]);
assert.equal(D.questions[5].correct,'Security administrator');
for(const q of D.questions){assert.ok(q.answer.length>100,q.id);assert.ok(q.teach.length>50,q.id);assert.ok(q.example.length>50,q.id);assert.ok(q.refs.length);for(const [id,where] of q.refs){assert.ok(D.sources.some(s=>s.id===id),q.id);assert.ok(where)}}
const all=[...D.questions,...D.vocab,...D.checks,...D.cloze,...D.trueFalse];assert.equal(new Set(all.map(x=>x.id)).size,all.length);
for(const x of all){assert.match(x.id,/^425-/);assert.equal(new Set([x.correct,...x.distractors]).size,x.distractors.length+1,x.id);assert.ok(x.distractors.length===3||x.format==='tf',x.id);assert.ok(D.sections.some(s=>s.id===x.section),x.id);if(x.source)assert.ok(D.questions.some(q=>q.number===x.source&&q.section===x.section),x.id)}
for(const s of D.sorts){assert.ok(D.questions.some(q=>q.number===s.source));assert.equal(new Set(s.items).size,s.items.length)}
const elements=new Map();function element(s){if(!elements.has(s))elements.set(s,{innerHTML:'',textContent:'',value:'',disabled:false,dataset:{},focus(){},setAttribute(){},insertAdjacentHTML(_,s){this.innerHTML+=s},classList:{add(){}}});return elements.get(s)}
const saved=new Map([['cis320-v1','untouched-320'],['cis304-module1-v1','untouched-304'],['cis464-chapters-v1','untouched-464']]);
const ctx=vm.createContext({console,Date,Math,JSON,Set,BigInt,TextEncoder,Uint8Array,crypto:crypto.webcrypto,document:{querySelector:element,querySelectorAll:()=>[]},window:{scrollTo(){}},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)},INPUT:D});
vm.runInContext(read('dist/cis425.js').split("document.addEventListener('click'")[0],ctx);const run=s=>vm.runInContext(s,ctx);run('D=INPUT');
for(let section=0;section<=8;section++){run('section='+section);for(const v of ['beginner','samples','coverage','teach','practice','flash','map','exam','apply','sort','abbrev','math','discussion','terms','guide','readings']){run(`navigate('${v}')`);assert.ok(element('#app').innerHTML.length>100,v)}}
run('section=0');for(const q of D.questions){for(let step=0;step<3;step++)run(`openLesson(${q.number},${step})`)}
run('examHome()');element('#mock-exam').onclick();assert.equal(run('session.total'),45);
assert.equal(run('session.items.filter(x=>x.format==="tf").length'),15);assert.equal(run('session.items.filter(x=>x.format==="fill").length'),10);
assert.equal(run('session.items.filter(x=>x.uncertain).length'),0);assert.equal(run('new Set(session.items.map(x=>x.id)).size'),45);
run('grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items.length'),45);assert.equal(run('session.right'),0);
run('start("practice",D.questions.slice(4,9));grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items.length'),6);assert.equal(run('session.items[4].id'),D.questions[4].id);
run('start("flash",[D.questions[5]])');element('#flip').onclick();assert.match(element('#flip').innerHTML,/Security administrator/);element('#remembered').onclick();assert.ok(run('progress.cards[D.questions[5].id].completed'));
for(const name of ['defense','keys','chain'])run(`mapHome('${name}')`);
for(let i=0;i<3;i++){run('rsaCase='+i);assert.equal(run('rsaResult(rsaCases[rsaCase]).plain'),run('rsaCases[rsaCase].m'));assert.equal(run('(rsaCases[rsaCase].e*rsaCases[rsaCase].d)%rsaResult(rsaCases[rsaCase]).phi'),1)}
assert.equal(run('modPow(7,3,55)'),13);
run('mathHome()');for(let i=0;i<5;i++)element('#rsa-step').onclick();assert.equal(element('#rsa-step').disabled,true);
for(const [key,value] of [['cis320-v1','untouched-320'],['cis304-module1-v1','untouched-304'],['cis464-chapters-v1','untouched-464']])assert.equal(saved.get(key),value);
assert.ok(saved.has('cis425-midterm-v1'));assert.ok(!read('dist/cis425.js').includes('Enterprise Resource Planning'));
for(const page of ['index.html','cis304.html','cis464.html','cis425.html','classes.html'])assert.ok(read('dist/'+page).includes('href="cis425.html"'),page);
const html=read('dist/cis425.html');assert.match(html,/cis425\.js\?v=/);assert.equal((html.match(/aria-current="page"/g)||[]).length,2);
for(const match of html.matchAll(/(?:src|href)="([^"?]+)\?v=([a-f0-9]+)"/g))assert.equal(match[2],crypto.createHash('sha256').update(read('dist/'+match[1])).digest('hex').slice(0,12),match[1]);
run('section=0;readingsHome()');assert.match(element('#app').innerHTML,/19 source/);assert.match(element('#app').innerHTML,/786/);
assert.equal(D.samples.length,21);assert.deepEqual(['True/False','Multiple choice','Fill in the blank','Discussion'].map(t=>D.samples.filter(x=>x.type===t).length),[5,6,4,6]);
assert.deepEqual(D.samples.filter(x=>x.type==='Multiple choice').map(x=>x.options.length),[4,4,4,5,5,5]);
assert.equal(D.discussions.length,7);assert.equal(D.beginnerRoute.length,new Set(D.beginnerRoute).size);
for(const n of D.beginnerRoute)assert.ok(D.questions.some(q=>q.number===n));
for(const entry of D.coverage){assert.ok(entry.topics.length,entry.id);for(const [title,numbers] of entry.topics){assert.ok(title);for(const n of numbers)assert.ok(D.questions.some(q=>q.number===n),entry.id+' '+n)}assert.ok(run(`coveragePool(D.coverage.find(x=>x.id==='${entry.id}')).length`)>0,entry.id)}
for(let n=1;n<=8;n++){const entry=D.coverage.find(x=>x.id==='lecture'+n);assert.ok(entry);assert.ok(D.sources.find(x=>x.id===11+n).chars>4000);for(const [title,nums] of entry.topics)for(const num of nums)assert.ok(D.questions[num-1].refs.some(r=>r[0]===11+n))}
for(const source of D.sources)assert.ok(D.questions.some(q=>q.refs.some(r=>r[0]===source.id)),'Unused source '+source.id);
for(const q of D.questions.slice(45)){assert.ok(D.checks.filter(x=>x.source===q.number).length>=2,q.id);assert.ok(q.goal);assert.ok(q.pitfall)}
for(let round=0;round<100;round++){const items=JSON.parse(run('JSON.stringify(buildMidtermItems())')),mc=items.filter(x=>!['tf','fill'].includes(x.format));assert.equal(items.length,45);assert.equal(mc.length,20);assert.equal(new Set(mc.map(x=>x.number||x.source)).size,20);for(const section of D.sections)assert.ok(mc.filter(x=>x.section===section.id).length>=2)}
run('section=0;discussionHome()');element('#discussion-five').onclick();assert.equal((element('#app').innerHTML.match(/Reveal model answer and checklist/g)||[]).length,5);element('#discussion-seven').onclick();assert.equal((element('#app').innerHTML.match(/Reveal model answer and checklist/g)||[]).length,7);
run('section=0;samplesHome()');assert.match(element('#app').innerHTML,/Email Header/);assert.match(element('#app').innerHTML,/OpenSSL/);
run('practiceHome()');element('#recall-blanks').onclick();assert.equal(run('session.mode'),'flash');assert.equal(run('session.total'),D.cloze.length);
console.log('PASS CIS 425: 21 exact professor examples, 19 source records, 84 lessons, chapter/lecture coverage, beginner route, 5/7 discussions, isolated progress, exam scoring, retries, flashcards, blank recall, navigation, and RSA.');
