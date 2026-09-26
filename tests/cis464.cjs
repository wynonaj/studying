const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const data=JSON.parse(read('dist/cis464-content.json')),slides=JSON.parse(read('dist/cis464-slides.json'));
assert.deepEqual(data.sections.map(s=>s.id),[1,2,3,10]);
assert.deepEqual(data.sections.map(s=>data.questions.filter(q=>q.section===s.id).length),[22,16,16,17]);
assert.deepEqual([1,2,3,10].map(n=>slides[n].length),[75,42,34,32]);
for(const [ch,ss] of Object.entries(slides))for(const [i,s] of ss.entries()){assert.equal(s.slide,i+1);for(const image of s.images)assert.ok(fs.existsSync(path.join(root,'dist',image)),image)}
const all=[...data.questions,...data.vocab,...data.checks,...data.cloze];
assert.equal(new Set(all.map(x=>x.id)).size,all.length);
for(const x of all){assert.match(x.id,/^464-/);assert.equal(x.distractors.length,3,x.id);assert.equal(new Set([x.correct,...x.distractors]).size,4,x.id);assert.ok(x.teach.length>40,x.id);assert.notEqual(x.teach,x.correct);assert.ok(data.sections.some(s=>s.id===x.section));if(x.source)assert.ok(data.questions.some(q=>q.number===x.source&&q.section===x.section),x.id)}
for(const q of data.questions){assert.ok(q.answer.length>90,q.id);assert.ok(q.example.length>50,q.id);assert.ok(q.title);assert.ok(q.slides.every(s=>s>=1&&s<=slides[q.section].length),q.id)}
for(const v of data.vocab.filter(v=>v.exp)){assert.equal(data.abbreviationDistractors[v.term].length,3,v.term);assert.equal(new Set([v.exp,...data.abbreviationDistractors[v.term]]).size,4,v.term)}
const elements=new Map();function element(s){if(!elements.has(s))elements.set(s,{innerHTML:'',textContent:'',value:'',disabled:false,dataset:{},focus(){},scrollIntoView(){},setAttribute(){},insertAdjacentHTML(_,s){this.innerHTML+=s},classList:{add(){}}});return elements.get(s)}
const saved=new Map([['cis320-v1','untouched-320'],['cis304-module1-v1','untouched-304']]);
const ctx=vm.createContext({console,Date,Math,JSON,Set,document:{querySelector:element,querySelectorAll:()=>[]},window:{scrollTo(){}},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v)},INPUT:data,SLIDE_INPUT:slides});
vm.runInContext(read('dist/cis464.js').split("document.addEventListener('click'")[0],ctx);const run=s=>vm.runInContext(s,ctx);run('D=INPUT;SLIDES=SLIDE_INPUT');
for(const ch of [0,1,2,3,10]){run('section='+ch);for(const v of ['teach','practice','flash','map','exam','apply','sort','abbrev','math','terms','guide','readings']){run(`navigate('${v}')`);assert.ok(element('#app').innerHTML.length>100,v)}}
for(const q of data.questions){run(`openLesson(${q.number},0);openLesson(${q.number},1);openLesson(${q.number},2)`);assert.ok(element('#app').innerHTML.includes('Try this topic'))}
for(const m of ['constraints','work','documents','ai'])run(`mapHome('${m}')`);
run('stakeholderGrid();weightedLab()');assert.match(element('#weighted-result').textContent,/7.60/);
run('financial=financePreset("figure");mathHome();for(let i=0;i<5;i++)showFinanceStep()');
assert.match(element('#math-work').innerHTML,/272,800.00/);
let result=JSON.parse(run('JSON.stringify(financialResult(financePreset("figure")))'));
assert.equal(result.pvc,243200);assert.equal(result.pvb,516000);assert.equal(result.npv,272800);
result=JSON.parse(run('JSON.stringify(financialResult(financePreset("exercise")))'));
assert.equal(result.rawPayback,null);assert.equal(result.rawROI,-60000/420000);
for(let i=0;i<1500;i++){
 const result=JSON.parse(run('JSON.stringify((()=>{const c=randomFinance();return {c,next:randomFinance(c),r:financialResult(c),qs:financeQuestions(c)}})())'));
 assert.notDeepEqual(result.c,result.next);
 const npv=result.c.costs.reduce((s,c,i)=>s+(result.c.benefits[i]-c)/(1+result.c.rate)**i,0);
 assert.ok(Math.abs(npv-result.r.npv)<.000001);
 for(const q of result.qs)assert.equal(new Set([q.correct,...q.distractors]).size,4,JSON.stringify(result));
 assert.equal(result.qs[1].correct,run(`money(${npv})`));
}
for(const x of data.sorts){ctx.SORT=x;for(let i=0;i<30;i++)assert.notEqual(run('JSON.stringify(shuffledOrder(SORT.items))'),JSON.stringify(x.items))}
run('section=0;start("practice",D.questions.slice(0,5));grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items[4].id'),data.questions[0].id);assert.equal(run('session.cleared.size'),0);
run('while(session.index<session.items.length){grade(session.items[session.index],true,"correct");advance()}');assert.equal(run('session.cleared.size'),5);assert.equal(run('session.right'),4);assert.equal(run('completed(D.questions[0])'),true);
assert.equal(saved.get('cis320-v1'),'untouched-320');assert.equal(saved.get('cis304-module1-v1'),'untouched-304');assert.ok(saved.has('cis464-chapters-v1'));
run('start("exam",D.questions.slice(0,1));grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items.length'),1);assert.equal(run('session.right'),0);
run('start("flash",[D.questions[0]])');const front=element('#flip').innerHTML;element('#flip').onclick();assert.notEqual(element('#flip').innerHTML,front);element('#flip').onclick();assert.ok(element('#flip').innerHTML.includes(data.questions[0].q));
run('start("practice",[{...D.sorts[0],kind:"sort"}])');assert.ok(element('#app').innerHTML.includes('Check order'));
run('start("practice",[{...D.vocab.find(v=>v.exp),kind:"wordbank"}])');assert.ok(element('#app').innerHTML.includes('Check name'));
for(const ch of [1,2,3,10]){run('section='+ch);assert.ok(run('filtered(mixedPool()).every(x=>x.section===section)'))}
for(const file of ['index.html','cis304.html','cis464.html']){
 const page=read('dist/'+file);
 for(const link of ['index.html','cis304.html','cis464.html'])assert.ok(page.includes('href="'+link+'"'),file+' → '+link);
 for(const match of page.matchAll(/(?:src|href)="([\w.-]+\.(?:js|css))\?v=([a-f0-9]+)"/g))assert.equal(require('node:crypto').createHash('sha256').update(read('dist/'+match[1])).digest('hex').slice(0,12),match[2],match[1]);
}
assert.ok(!read('dist/cis464.js').includes('D.readings'));
console.log('PASS CIS 464: 71 lessons, 183 source slides/assets, choice and chapter integrity, 1,500 financial rounds, all views/lessons, shuffled sorts, retries, exam scoring, flashcards, and three-class progress isolation.');
