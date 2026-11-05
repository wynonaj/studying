const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const D=JSON.parse(read('dist/cis320-test2-content.json'));

assert.equal(D.questions.length,57,'all completed-guide topics');
assert.deepEqual(D.sections.map(s=>D.questions.filter(q=>q.section===s.id).length),[9,8,11,8,9,12]);
assert.equal(D.exercises.length,20,'all supplied subnet exercises');
assert.deepEqual(D.exercises.map(x=>x.exerciseNumber),Array.from({length:20},(_,i)=>i+1));
assert.equal(D.sources.filter(s=>s.kind==='slides').reduce((n,s)=>n+s.count,0),189);
assert.deepEqual(D.sourceSummary,{lectureSlides:189,guideTopics:57,exactExercises:20,providedPastedNotes:11,uniquePastedNotes:3});
assert.ok(D.vocab.length>=90,'wide direct-definition coverage');
assert.ok(D.checks.length>=20);assert.ok(D.cloze.length>=12);assert.ok(D.sorts.length>=12);
const banks=['questions','vocab','checks','cloze','sorts','exercises','connections'];
const ids=banks.flatMap(k=>D[k].map(x=>x.id));assert.equal(new Set(ids).size,ids.length,'stable unique IDs');
for(const key of ['questions','vocab','checks','exercises'])for(const x of D[key]){
  assert.equal(x.distractors.length,3,`${key} ${x.id} choice count`);
  assert.equal(new Set([x.correct,...x.distractors]).size,4,`${key} ${x.id} distinct choices`);
  assert.ok(x.teach.length>55,`${key} ${x.id} specific explanation`);
  assert.notEqual(x.teach.trim(),x.correct.trim(),`${key} ${x.id} does not merely repeat answer`);
  assert.ok(x.answer.length>45,`${key} ${x.id} complete answer`);
  assert.ok(x.example.length>35,`${key} ${x.id} concrete example`);
  assert.ok(D.sections.some(s=>s.id===x.section),x.id);
}
for(const q of D.questions){assert.ok(q.title);assert.ok(q.sourceLabel);assert.ok(Array.isArray(q.slides));}
for(const x of D.cloze){assert.equal((x.q.match(/____/g)||[]).length,x.correct.split('; ').length,x.id);assert.ok(x.distractors.length>=3);}
for(const x of D.sorts){assert.ok(x.items.length>=3);assert.equal(new Set(x.items).size,x.items.length);assert.ok(x.teach.length>50);}
assert.match(D.vocab.find(x=>x.term==='DHCP').answer,/Dynamic Host Configuration Protocol/);
assert.doesNotMatch(D.vocab.find(x=>x.term==='DHCP').answer,/Dynamic Host Control Protocol/);
assert.match(D.questions.find(x=>x.title.includes('/19')||x.q.includes('/19')).answer,/8,190|8190/);
assert.match(D.questions.find(x=>x.title.includes('subnet count')||x.q.toLowerCase().includes('parent prefix'))?.answer||'',/parent/i);
assert.match(D.checks.find(x=>x.q.includes('total addresses and usable')).teach,/network address.*broadcast address/i);
assert.match(D.questions.find(x=>x.q.includes('TCP')&&x.title.toLowerCase().includes('end-to-end')).answer,/routers/i);
assert.match(D.exercises[0].correct,/broadcast address/i);
assert.equal(D.exercises[19].correct,'Router');

const elements=new Map();function element(s){if(!elements.has(s))elements.set(s,{innerHTML:'',textContent:'',value:'0',disabled:false,dataset:{},focus(){},setAttribute(){},insertAdjacentHTML(_,v){this.innerHTML+=v},classList:{add(){}}});return elements.get(s)}
const saved=new Map([['cis320-v1','test-one-progress'],['cis304-module1-v1','cis304-progress']]);
const ctx=vm.createContext({console,Date,Math,JSON,Set,Intl,document:{querySelector:element,querySelectorAll:()=>[],addEventListener(){}},window:{scrollTo(){}},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)},INPUT:D});
const source=read('dist/cis320-test2.js').split("document.addEventListener('click'")[0];vm.runInContext(source,ctx);const run=s=>vm.runInContext(s,ctx);run('D=INPUT');
for(const view of ['teach','practice','flash','connections','subnet','exam','exercises','sort','cloze','abbrev','terms','guide','sources']){run(`navigate('${view}')`);assert.ok(element('#app').innerHTML.length>100,view)}
for(const q of D.questions){for(let step=0;step<3;step++)run(`openLesson(${q.number},${step})`);assert.match(element('#app').innerHTML,/Try this topic/)}
for(const sort of D.sorts){ctx.SORT=sort;for(let i=0;i<20;i++)assert.notEqual(run('JSON.stringify(shuffledOrder(SORT.items))'),JSON.stringify(sort.items));}
for(let p=0;p<=32;p++)for(let n=0;n<40;n++){
  const ip=Math.floor(Math.random()*0x100000000)>>>0;ctx.IP=ip;ctx.P=p;
  const got=JSON.parse(run('JSON.stringify(subnetInfo(IP,P))'));
  const total=2**(32-p),mask=p===0?0:(0xffffffff<<(32-p))>>>0,network=(ip&mask)>>>0,broadcast=network+total-1;
  assert.equal(got.network,network);assert.equal(got.broadcast,broadcast);assert.equal(got.total,total);assert.equal(got.hostBits,32-p);
  assert.equal(got.usable,p===32?1:p===31?2:Math.max(0,total-2));
}
for(let i=0;i<300;i++){
  const pair=JSON.parse(run('JSON.stringify((()=>{const a=randomSubnetCase();return [a,randomSubnetCase(a)]})())'));
  assert.ok(pair[0].value!==pair[1].value||pair[0].prefix!==pair[1].prefix,'fresh subnet case');
  ctx.CASE=pair[0];const qs=JSON.parse(run('JSON.stringify(subnetQuestions(CASE))'));
  assert.equal(qs.length,8);for(const q of qs)assert.equal(new Set([q.correct,...q.distractors]).size,4,q.id);
  const binary=JSON.parse(run('JSON.stringify(binaryQuestions())'));for(const q of binary)assert.equal(new Set([q.correct,...q.distractors]).size,4,q.id);
  const needs=JSON.parse(run('JSON.stringify(requirementQuestions())'));for(const q of needs)assert.equal(new Set([q.correct,...q.distractors]).size,4,q.id);
}
run('section=0;start("practice",D.questions.slice(0,5));grade(session.items[0],false,"wrong");advance()');
assert.equal(run('session.items[4].id'),D.questions[0].id,'missed item returns after three other items');
assert.equal(run('session.cleared.size'),0);
run('while(session.index<session.items.length){grade(session.items[session.index],true,session.items[session.index].correct);advance()}');
assert.equal(run('session.cleared.size'),5);assert.equal(saved.get('cis320-v1'),'test-one-progress');assert.equal(saved.get('cis304-module1-v1'),'cis304-progress');assert.ok(saved.has('cis320-test2-v1'));
run('start("exam",D.questions.slice(0,1));grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items.length'),1);assert.equal(run('session.right'),0);
run('start("flash",[D.questions[0]])');assert.ok(!element('#app').innerHTML.includes(D.questions[0].answer));element('#flip').onclick();assert.ok(element('#app').innerHTML.includes(D.questions[0].answer));
run('start("practice",[{...D.sorts[0],kind:"sort"}])');assert.match(element('#app').innerHTML,/Check order/);
run('start("practice",[D.cloze[0]])');assert.match(element('#app').innerHTML,/Check sentence/);
run('start("practice",[{...D.vocab.find(v=>v.term==="DHCP"),id:"dhcp-build",kind:"wordbank"}])');assert.match(element('#app').innerHTML,/Check phrase/);
run('section=5');assert.ok(run('filtered(mixedPool()).every(x=>x.section===5)'));
run('section=0;progress.lessons={};openLesson(D.questions[0].number,2);continueLearning(D.questions[0].number)');assert.ok(run('lesson.number!==D.questions[0].number'));

const html=read('dist/cis320-test2.html'),index=read('dist/index.html'),classes=read('dist/classes.html');
assert.match(index,/href="cis320-test2.html"/);assert.match(html,/href="index.html"/);assert.match(classes,/Test 1 and Test 2/);
assert.match(html,/cis320-test2-content\.js/,'Test 2 content is bundled with the page');
assert.match(read('dist/cis320-test2-content.js'),/^window\.CIS320_TEST2_CONTENT=/,'bundled content initializes before the app');
assert.match(read('dist/cis320-test2.js'),/if\(window\.CIS320_TEST2_CONTENT\)/,'app uses bundled content without a second network request');
assert.ok(read('dist/cis320-test2.js').includes("fetch('cis320-test2-content.json'"));
const bundledWindow={scrollTo(){},CIS320_TEST2_CONTENT:D};
const bundledCtx=vm.createContext({console,Date,Math,JSON,Set,Intl,document:{querySelector:element,querySelectorAll:()=>[],addEventListener(){}},window:bundledWindow,localStorage:{getItem:()=>null,setItem(){}},fetch(){throw Error('JSON endpoint should not be requested when bundled content is present')}});
vm.runInContext(read('dist/cis320-test2.js'),bundledCtx);
assert.match(element('#app').innerHTML,/Understand Test 2 before you memorize it/,'bundled content renders even when the JSON endpoint is unavailable');
assert.ok(!read('dist/cis320-test2.js').includes("setItem('cis320-v1"));
assert.ok(!read('dist/cis320-test2.js').includes('type="text"'),'no typed quiz answer controls');
assert.match(read('dist/cis320-test2.js'),/0x5D[^<]*0101 1101/,'remembered hexadecimal exam pattern is taught');
for(const page of fs.readdirSync(path.join(root,'dist')).filter(x=>x.endsWith('.html')).map(x=>read('dist/'+x)))for(const match of page.matchAll(/(?:src|href)="([^"?]+\.(?:js|css))\?v=([a-f0-9]+)"/g)){
  assert.equal(match[2],crypto.createHash('sha256').update(read('dist/'+match[1])).digest('hex').slice(0,12),match[1]+' cache hash');
}
console.log(`PASS CIS 320 Test 2: ${D.questions.length} guide topics, ${D.exercises.length} exact exercises, ${D.vocab.length} terms, ${D.checks.length} applications, ${D.cloze.length} blanks, ${D.sorts.length} sorts, 1,300 subnet calculations, retry completion, isolated progress, and navigation.`);
