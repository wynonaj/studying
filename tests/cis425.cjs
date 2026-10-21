const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const D=JSON.parse(read('dist/cis425-content.json'));
assert.equal(D.questions.length,45);assert.equal(D.sources.length,11);
assert.deepEqual(D.sources.map(x=>x.id),Array.from({length:11},(_,i)=>i+1));
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
for(let section=0;section<=8;section++){run('section='+section);for(const v of ['teach','practice','flash','map','exam','apply','sort','abbrev','math','discussion','terms','guide','readings']){run(`navigate('${v}')`);assert.ok(element('#app').innerHTML.length>100,v)}}
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
run('section=0;readingsHome()');assert.match(element('#app').innerHTML,/11 sources/);assert.match(element('#app').innerHTML,/786/);
console.log('PASS CIS 425: all 21 samples, 11 sources, 45 lessons, isolated progress, exam composition, scoring, retries, flashcards, sources, navigation, and RSA examples.');
