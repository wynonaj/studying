const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const data=JSON.parse(read('dist/cis425-content.json'));

assert.equal(data.sections.length,8);
assert.equal(data.questions.length,57);
assert.equal(data.vocab.length,183);
assert.equal(data.checks.length,57);
assert.equal(data.cloze.length,12);
assert.equal(data.sorts.length,7);
assert.deepEqual(data.sections.map(s=>data.questions.filter(q=>q.section===s.id).length),[4,8,6,7,6,5,10,11]);

const slideCounts=[22,25,25,33,30,28,52,60];
const sourceSlides=JSON.parse(read('scripts/review/cis425/source-slides.json'));
assert.deepEqual(sourceSlides.map(d=>d.slides.length),slideCounts);
for(const q of data.questions){
  assert.ok(q.answer.length>120,q.id);assert.ok(q.teach.length>80,q.id);assert.ok(q.example.length>65,q.id);
  assert.equal(q.distractors.length,3,q.id);assert.equal(new Set([q.correct,...q.distractors]).size,4,q.id);
  assert.ok(q.slides.every(n=>n>=1&&n<=slideCounts[q.section-1]),q.id);
}
for(const x of [...data.vocab,...data.checks,...data.cloze]){
  assert.equal(x.distractors.length,3,x.id);assert.equal(new Set([x.correct,...x.distractors]).size,4,x.id);
  assert.ok(data.questions.some(q=>q.number===x.source),x.id);
}
for(const sort of data.sorts){assert.ok(sort.items.length>=3);assert.equal(new Set(sort.items).size,sort.items.length)}

const required=['DDoS','SQL injection','XSS','Phishing','Spear phishing','Hardening','Hash','Symmetric encryption','Asymmetric cryptography','Digital signature','TCP','IP','SNMP','DNSSEC','SIEM','Hypervisor','SaaS'];
const corpus=(data.questions.map(q=>q.title+' '+q.answer).join(' ')+' '+data.vocab.map(v=>v.term+' '+v.answer).join(' ')).toLowerCase();
for(const term of required)assert.ok(corpus.includes(term.toLowerCase()),term);

const elements=new Map();function element(s){if(!elements.has(s))elements.set(s,{innerHTML:'',textContent:'',value:'',disabled:false,dataset:{},focus(){},setAttribute(){},insertAdjacentHTML(_,v){this.innerHTML+=v},scrollIntoView(){},classList:{add(){}}});return elements.get(s)}
const saved=new Map([['cis320-v1','keep-320'],['cis304-module1-v1','keep-304'],['cis464-chapters-v1','keep-464']]);
const ctx=vm.createContext({console,Date,Math,JSON,Set,document:{querySelector:element,querySelectorAll:()=>[],addEventListener(){}},window:{scrollTo(){}},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)}});
vm.runInContext(read('dist/cis425.js').split("document.addEventListener('click'")[0],ctx);
const run=s=>vm.runInContext(s,ctx);run('D='+JSON.stringify(data));
for(const v of ['teach','practice','flash','exam','apply','sort','abbrev','terms','guide']){run(`navigate('${v}')`);assert.ok(element('#app').innerHTML.length>100,v)}
for(const q of data.questions){run(`openLesson(${q.number},0);openLesson(${q.number},1);openLesson(${q.number},2)`);assert.ok(element('#app').innerHTML.includes('Try this topic'),q.id)}
run('section=0;start("practice",[D.questions[0],D.questions[1]]);grade(session.items[0],false,"wrong");advance()');
assert.equal(run('session.items[2].id'),data.questions[0].id);assert.equal(run('session.cleared.size'),0);
run('while(session.index<session.items.length){grade(session.items[session.index],true,"correct");advance()}');
assert.ok(saved.has('cis425-lectures-v1'));assert.equal(saved.get('cis320-v1'),'keep-320');assert.equal(saved.get('cis304-module1-v1'),'keep-304');assert.equal(saved.get('cis464-chapters-v1'),'keep-464');
run('start("practice",[{...D.sorts[0],kind:"sort"}])');assert.ok(element('#app').innerHTML.includes('Check order'));
run('start("practice",[D.cloze[0]])');assert.ok(element('#app').innerHTML.includes('Check sentence'));
run('start("flash",[D.vocab[0]])');const answer=data.vocab[0].answer;assert.ok(!element('#flip').innerHTML.includes(answer));element('#flip').onclick();assert.ok(element('#flip').innerHTML.includes(answer));

for(const page of ['dist/index.html','dist/cis304.html','dist/cis425.html','dist/cis464.html','dist/classes.html']){
  const html=read(page);assert.match(html,/href="cis425\.html"/);
  for(const match of html.matchAll(/(?:src|href)="([\w.-]+\.(?:js|css))\?v=([a-f0-9]+)"/g)){
    const expected=crypto.createHash('sha256').update(read('dist/'+match[1])).digest('hex').slice(0,12);
    assert.equal(match[2],expected,`${page}: ${match[1]}`);
  }
}
assert.match(read('dist/cis425.html'),/CIS 425 \/ DEFENSIVE CYBERSECURITY/);
assert.ok(!read('dist/cis425.js').includes("setItem('cis320"));
console.log('PASS CIS 425: 275 source slides across 8 lectures, 57 lessons, 183 terms, practice views, delayed retries, flashcards, sorting, fill-ins, source references, and isolated progress.');
