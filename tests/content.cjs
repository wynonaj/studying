const fs=require('fs'),vm=require('vm'),assert=require('assert');
const context=vm.createContext({localStorage:{getItem:()=>null},console});
vm.runInContext(fs.readFileSync('dist/vocab.js','utf8'),context);
vm.runInContext(fs.readFileSync('dist/teaching.js','utf8').split("document.addEventListener('click'")[0],context);
vm.runInContext(fs.readFileSync('dist/subnet.js','utf8'),context);
vm.runInContext(fs.readFileSync('dist/numbers.js','utf8'),context);
let app=fs.readFileSync('dist/app.js','utf8');vm.runInContext(app.split("document.addEventListener('click'")[0],context);
context.data=JSON.parse(fs.readFileSync('dist/content.json'));
vm.runInContext('DATA=data',context);
let result=vm.runInContext(`(()=>{let banks=[...all(),...DATA.understanding,...labItems(),...conversionCards()];for(let x of banks){let mc=makeMC(x);if(mc.options.length!==4||new Set(mc.options).size!==4||mc.options.filter(a=>a===mc.answer).length!==1)throw Error('Bad options: '+x.id);if(!explanationHTML(mc,mc.answer).includes('Correct'))throw Error('Missing explanation '+x.id)}let counts=[];for(let c of DATA.chapters){let pool=learnPool().filter(x=>x.ch===c.id);for(let i=0;i<100;i++){let sample=mixedReview(pool);if(sample.length!==10||new Set(sample.map(x=>x.id)).size!==10||sample.some(x=>x.ch!==c.id))throw Error('Bad chapter mixture');for(let kind of new Set(pool.map(x=>x.kind)))if(!sample.some(x=>x.kind===kind))throw Error('Missing '+kind);if(sample.some(x=>x.kind==='understanding'))throw Error('Separate bank leaked')}counts.push({chapter:c.id,count:pool.length,types:[...new Set(pool.map(x=>x.kind))]})}if(DATA.understanding.length!==54)throw Error('Coverage');for(let x of DATA.understanding){let source=DATA.questions.find(q=>q.id===x.sourceId);if(!source||source.ch!==x.ch)throw Error('Invalid source');if(!explanationHTML(x,x.answer).includes('Study-guide topic'))throw Error('Source not displayed')}return {banksTested:banks.length,counts}})()`,context);
assert.equal(context.data.questions.length,54);assert.equal(new Set(context.data.questions.map(q=>q.id)).size,54);assert.equal(new Set(context.data.understanding.map(q=>q.sourceId)).size,54);
assert(!app.includes('id="response"')&&!app.includes('<textarea'));
console.log(JSON.stringify(result,null,2));console.log('PASS: 54 original prompts present, authored choices unique, sources valid, 500 chapter mixtures correctly scoped, no typed answers.');
vm.runInContext(`
const originalRecord=record;record=()=>{};renderSession=()=>{};
function check(value,message){if(!value)throw Error(message)}
const cards=[1,2,3,4].map(id=>({id:'test-'+id,answer:'yes',options:['yes','no']}));
session={mode:'mixed',items:cards,index:0,total:4,cleared:new Set(),attempts:0,right:0,missed:[]};
advance(false);
check(session.items.length===5&&session.items[4].id==='test-1','Missed card must return after intervening cards');
advance(true);advance(true);advance(true);
check(session.cleared.size===3&&session.index<session.items.length,'Cannot finish with unresolved card');
advance(false);
check(session.index<session.items.length,'Repeated miss must return again');
advance(true);
check(session.cleared.size===4&&session.index===session.items.length,'Finish only after all answered correctly');
check(session.attempts===6&&session.missed.length===1,'Attempts and unique misses');
const network=makeMC(VOCAB.find(x=>x.term==='Network layer'));
const feedback=explanationHTML(network,network.answer);
check(feedback.includes('destination IP address')&&!feedback.includes('Match a layer to the scope'),'Network explanation must explain the specific answer');
check(layerJobCards().length===7,'All OSI layer jobs covered');
check(readableText('One idea. Another idea.').match(/<p>/g).length===2,'Separate ideas visually');
check(readableText('Value 1.5 Gbps. Next idea.').includes('1.5'),'Do not split decimal values');
`,Object.assign(context,{window:{scrollTo(){}}}));
console.log('PASS: delayed retries, repeated misses, completion gate, contextual explanations and layer matching.');
vm.runInContext(`
modelBuild={slots:{osi:[...modelLayers('osi')],tcpip:[...modelLayers('tcpip')]}};
check(modelIsCorrect('osi')&&modelIsCorrect('tcpip'),'Both correct stacks accepted');
modelBuild.slots.tcpip[1]='Presentation';
check(!modelIsCorrect('tcpip'),'Reject separate Presentation layer in course TCP/IP model');
modelBuild.slots.osi[0]=null;
check(!modelIsCorrect('osi'),'Reject incomplete model');
const physical=makeMC(VOCAB.find(x=>x.term==='Physical layer'));
check(explanationHTML(physical,physical.answer).toLowerCase().includes('copper carries electrical signals'),'Physical answer has a concrete explanation');
check(!explanationHTML(physical,physical.answer).includes('Match a layer to the scope'),'No generic layer paragraph in Physical feedback');
`,context);
assert(!app.includes("$('#export')")&&!app.includes("$('#import')"));
assert(!/id="(?:export|import|file)"/.test(fs.readFileSync('dist/index.html','utf8')));
console.log('PASS: model comparison grading, physical explanation, and removal of import/export.');
vm.runInContext(`
for(const original of [...ORDERS.map(x=>x.items),...wordBankCards(VOCAB).map(x=>x.exp.split(/\\s+/))]){
 let prior=null;
 for(let attempt=0;attempt<20;attempt++){
  const order=shuffledOrder(original);
  check(JSON.stringify([...order].sort())===JSON.stringify([...original].sort()),'Shuffle preserves all pieces');
  check(JSON.stringify(order)!==JSON.stringify(original),'Exercise must begin jumbled');
  if(new Set(original).size>=3)check(JSON.stringify(order)!==prior,'Avoid identical consecutive starting orders');
  prior=JSON.stringify(order);
 }
}
for(const card of [...wordBankCards(VOCAB),...clozeCards()]){
 let x=prepareWordBank(card);
 for(const word of x.words){let index=x.bank.findIndex((v,i)=>v===word&&!x.picked.includes(i));check(index>=0,'Every required token exists');x.picked.push(index)}
 check(wordBankAnswer(x)===card.answer,'Reconstructed answer grades correctly');
 check(prepareWordBank(x).picked.length===0,'Retry clears selected words');
 if(card.cloze)check(card.q.split('____').length-1===card.tokens.length,'Blank count matches answers');
}
check(clozeCards().some(x=>x.tokens.join('|')==='IEEE|IETF'),'IEEE/IETF sentence included');
check(new Set(clozeCards().map(x=>x.ch)).size===5,'Sentences cover all chapters');
`,context);
console.log('PASS: fresh jumbled orders, complete word banks, repeated words, blank counts and chapter coverage.');
vm.runInContext(`
check(DATA.notes.length===33&&DATA.notesQuestions.length===49,'Added material coverage');
check(!JSON.stringify(DATA.notes).includes('Summary Checklist'),'Checklist excluded');
for(const q of DATA.questions){check(q.remember.startsWith('Remember:'),'Beginner reminder '+q.id);check(DATA.notes.some(n=>n.id===q.lessonId&&n.ch===q.ch),'Guide lesson link '+q.id)}
for(const q of DATA.notesQuestions){const mc=makeMC(q);check(new Set(mc.options).size===4&&mc.options.includes(mc.answer),'Notes answer options');check(DATA.notes.some(n=>n.id===q.lessonId&&n.ch===q.ch),'Notes lesson link');check(explanationHTML(mc,mc.options.find(a=>a!==mc.answer)).includes('Let’s make it simple'),'Wrong-answer reminder');check(!all().some(x=>x.id===q.id)&&!learnPool().some(x=>x.id===q.id),'Separate notes bank')}
check(!noteMarkdown('<script>alert(1)</script>').includes('<script>'),'Escape note HTML');
check(noteMarkdown('| A | B |\\n| --- | --- |\\n| 1 | 2 |').includes('<table>'),'Render readable tables');
check(DATA.notes.every(n=>!/[{}\\\\]/.test(n.body)),'No damaged pasted formulas');
`,context);
console.log('PASS: complete notes sections, beginner reminders, lesson links, separate banks and safe readable rendering.');
vm.runInContext(`
const sample=dissectCIDR('73.5.0.0/17');
check(sample.host===15&&sample.total===32768&&sample.usable===32766,'Guide subnet arithmetic');
check(numberIP(sample.mask)==='255.255.128.0'&&numberIP(sample.last)==='73.5.127.255','Mask and broadcast');
check(dissectCIDR('01001001.00000101.00000000.00000000 /17').value===sample.value,'Binary input');
check(numberIP(dissectCIDR('192.168.12.34/24').network)==='192.168.12.0','Normalize host input');
for(let prefix=0;prefix<=32;prefix++){
 const d=dissectCIDR('255.255.255.255/'+prefix);
 check(d.total===2**(32-prefix)&&d.network+d.total-1===d.last,'Unsigned block arithmetic');
 check(d.bits.slice(0,prefix)===d.networkBits.slice(0,prefix),'Network prefix unchanged');
 check(d.networkBits.slice(prefix).split('').every(b=>b==='0'),'Network clears host bits');
 check(d.lastBits.slice(prefix).split('').every(b=>b==='1'),'Last address sets host bits');
 for(const q of subnetQuestions(d))check(new Set(q.options).size===4&&q.options.includes(q.answer),'Generated unique answers /'+prefix);
}
check(dissectCIDR('10.0.0.0/31').usable===2&&dissectCIDR('10.0.0.1/32').usable===1,'Special usable counts');
for(const input of ['1.2.3.4/33','256.1.2.3/24','1.2.3/24','-1.2.3.4/8','1.2.3.4/-1','1.2.3.4/2.5','hello']){let threw=false;try{dissectCIDR(input)}catch(e){threw=true}check(threw,'Reject bad input '+input)}
let prev='';for(let i=0;i<100;i++){const text=randomSubnet(),d=dissectCIDR(text);check(text!==prev&&d.value===d.network&&d.octets[0]===10,'Random canonical private subnet');prev=text}
for(const n of DATA.notes){const teaching=DATA.teaching[n.id];check(teaching&&teaching.context&&teaching.analogy&&teaching.example,'Teaching coverage '+n.id);for(const term of teaching.terms)check(JARGON[term],'Plain definition '+term)}
check(JARGON['Working group'].includes('people')&&JARGON['End-user'].includes('person'),'Human terms explained');
check(preTeachHTML({ch:4,term:'RIR'}).includes('Allocation'),'Registry question explains allocation');
check(questionContext({ch:12,term:'Core layer'}).includes('campus'),'Campus context distinct from OSI');
record=originalRecord;save=()=>{};stats=()=>{};
progress={cards:{},xp:0,days:[]};record({id:'completion-test'},true);
check(completedOnce({id:'completion-test'}),'First correct response completes item');
const first=progress.cards['completion-test'].firstCorrectAt;record({id:'completion-test'},false);
check(completedOnce({id:'completion-test'})&&progress.cards['completion-test'].firstCorrectAt===first,'Later mistakes preserve completion');
check(progress.cards['completion-test'].level===0&&progress.xp===12,'Spaced review and XP unchanged');
`,context);
console.log('PASS: /0–/32 math, binary input, validation, random practice, teaching coverage and once-complete progress.');

// Numbers lab must launch even after studying a chapter with no number drills.
const labContext=vm.createContext({localStorage:{getItem:()=>null},console});
vm.runInContext(app.split("document.addEventListener('click'")[0],labContext);
vm.runInContext(fs.readFileSync('dist/subnet.js','utf8'),labContext);
vm.runInContext(fs.readFileSync('dist/numbers.js','utf8'),labContext);
labContext.data=context.data;
vm.runInContext(`
DATA=data;
const elements=new Map();
const document={querySelector:s=>{if(!elements.has(s))elements.set(s,{});return elements.get(s)}};
renderLab=()=>{};
for(const previousChapter of [0,1,2,3,4,12]){
 chapter=previousChapter;numbersChapter=0;numbersHome();
 if($('#app').innerHTML.includes('id="chapter"'))throw Error('Global chapter filter leaked into Numbers lab');
 for(const selection of [0,3,4]){
  $('#numbers-chapter').onchange({target:{value:String(selection)}});
  $('#addressstart').onclick();
  if(!lab.items.length||lab.items.some(x=>selection&&x.ch!==selection))throw Error('Numbers lab cannot launch selected drills');
  if(chapter!==previousChapter)throw Error('Numbers lab changed the study chapter');
 }
}
`,labContext);
console.log('PASS: Numbers lab launches for every prior chapter and keeps its drill filter independent.');

// Every selectable diagram part must resolve to an existing explanation/lesson.
vm.runInContext(fs.readFileSync('dist/map.js','utf8'),context);
vm.runInContext(`
for(const [key,[title,body,lesson]] of Object.entries(MAP_PARTS)){
 if(!title||!body||!DATA.notes.some(n=>n.id===lesson))throw Error('Broken map lesson '+key);
}
const mapElements=new Map();
const document={querySelector:s=>{if(!mapElements.has(s))mapElements.set(s,{innerHTML:'',scrollIntoView(){}});return mapElements.get(s)},querySelectorAll:()=>[]};
for(let tab=0;tab<6;tab++){
 mapState.tab=tab;visualMapHome();
 for(const match of $('#map-scene').innerHTML.matchAll(/data-map-part="([^"]+)"/g)){
  if(!MAP_PARTS[match[1]])throw Error('Unknown map target '+match[1]);
  showMapPart(match[1]);
 }
}
for(let step=0;step<6;step++){
 mapState.wrap=step;renderMapWrap();
 const html=$('#map-scene').innerHTML.split('class="doll-wrap"')[1];
 if(!html.includes('Application data · your message'))throw Error('Message lost');
 if(step>=3&&!(html.indexOf('Ethernet header')<html.indexOf('IP header')&&html.indexOf('IP header')<html.indexOf('TCP header')&&html.indexOf('TCP header')<html.indexOf('Application data')&&html.indexOf('FCS trailer')>html.indexOf('Application data')))throw Error('Incorrect encapsulation order');
}
`,context);
console.log('PASS: six map views render, explanations link to lessons, and wrappers preserve header/payload/trailer order.');

vm.runInContext(`
let previousDisplay='';
for(let i=0;i<300;i++){
 const cards=freshDetectiveItems();
 if(cards.length!==17)throw Error('Missing detective skill');
 for(const x of cards)if(x.options.length!==4||new Set(x.options).size!==4||!x.options.includes(x.answer))throw Error('Bad generated choices '+x.id);
 const prefix=cards.find(x=>x.id==='cidr-prefix');
 if(prefix.display===previousDisplay)throw Error('Repeated subnet');previousDisplay=prefix.display;
 const total=cards.find(x=>x.id==='cidr-total');
 const host=cards.find(x=>x.id==='cidr-host');
 if(Number(total.answer.replaceAll(',',''))!==2**Number(host.answer))throw Error('Generated math mismatch');
}
`,context);
console.log('PASS: 300 fresh detective rounds retain all skills, distinct choices and correct subnet math.');
vm.runInContext(`
lab={items:freshDetectiveItems(),index:17,right:17};
renderLab();
if(!$('#app').innerHTML.includes('New round · fresh numbers'))throw Error('Missing next round');
$('#fresh-round').onclick();
if(lab.index!==0||lab.items.length!==17||!$('#app').innerHTML.includes('Numbers memory sheet'))throw Error('New round did not start');
`,context);

vm.runInContext(`
const normalizeFeedback=s=>String(s||'').replace(/^Remember:\\s*/i,'').replace(/[^a-z0-9]/gi,'').toLowerCase();
for(const v of VOCAB){
 const f=DATA.vocabFeedback[v.term];
 check(f&&f.why.length>75&&f.hint.length>35,'Missing authored vocabulary feedback '+v.term);
 check(normalizeFeedback(f.why)!==normalizeFeedback(v.a),'Definition repeated as explanation '+v.term);
 check(normalizeFeedback(f.why)!==normalizeFeedback(f.hint),'Duplicate easy and detailed feedback '+v.term);
 for(const x of [makeMC(v),...wordBankCards([v])]){
  check(feedbackReason(x)===f.why,'Authored feedback bypassed '+v.term);
  const html=explanationHTML(x,'wrong');
  check(html.includes(esc(f.why.split('. ')[0])),'Wrong feedback omits reasoning '+v.term);
 }
}
for(const x of [...DATA.questions,...DATA.understanding,...DATA.notesQuestions,...clozeCards(),...labItems(),...conversionCards(),...layerJobCards()]){
 check(feedbackReason(x)&&normalizeFeedback(feedbackReason(x))!==normalizeFeedback(x.answer||x.quizAnswer),'Answer-only feedback '+x.id);
 const hint=beginnerReminder(x);
 if(hint)check(normalizeFeedback(hint)!==normalizeFeedback(feedbackReason(x)),'Repeated feedback '+x.id);
}
check(DATA.notesQuestions.find(x=>x.id==='notes-quiz-28').explain.includes('spine'),'Spine-leaf explanation');
check(!DATA.notesQuestions.find(x=>x.id==='notes-quiz-28').explain.includes('Distribution'),'Unrelated campus tiers leaked');
check(!beginnerReminder(DATA.understanding.find(x=>x.id==='u190')).includes('/17'),'Unrelated source example leaked');
const savedXP=progress.xp;let resumed=0;
showNumberReminder(()=>resumed++,0);
check($('#app').innerHTML.includes('256 − 2 = 254'),'Reminder demonstrates usable count');
check($('#app').innerHTML.includes('Host bits')&&$('#app').innerHTML.includes('Total addresses'),'Reminder distinguishes units');
$('#reminder-continue').onclick();
check(resumed===1&&progress.xp===savedXP,'Reminder must resume without scoring');
`,context);
console.log('PASS: all vocabulary and question feedback has reasoning; no duplicate hints or inherited wrong-number examples; reminders are unscored.');
vm.runInContext(`
for(const item of [labItems().find(x=>x.id==='labels10'),...freshDetectiveItems().filter(x=>x.id.startsWith('labels')),learnPool().find(x=>x.id==='lab-labels10')]){
 const html=preTeachHTML(item);
 check(html.includes('exponent')&&!html.includes('MAC address'),'Counting labels must teach powers of two');
 check(lessonFor(item)==='notes-number-labels','Counting labels must link to correct lesson');
 check(explanationHTML(item,item.answer).includes('data-lesson="notes-number-labels"'),'Feedback link must match rule');
}
session={mode:'flash',items:[VOCAB.find(x=>x.term==='IEEE')],index:0,total:1,cleared:new Set(),revealed:false};
renderFlashCard();
check(!$('#app').innerHTML.includes('Institute of Electrical'),'Front must not reveal expansion');
$('#flip-card').onclick();
check($('#app').innerHTML.includes('Institute of Electrical and Electronics Engineers'),'Back must show full name');
check($('#app').innerHTML.includes('Still learning'),'Back must provide recall ratings');
$('#flip-card').onclick();
check(!$('#app').innerHTML.includes('Institute of Electrical'),'Flip back must hide answer');
renderStudyNav();
check($('#nav').innerHTML.includes('Focused practice')&&$('#nav').innerHTML.includes('Reference library'),'Group navigation');
`,context);
console.log('PASS: label rules and lesson links match; flashcards flip in both directions without leaking answers.');
vm.runInContext(`
const hopLesson=DATA.teaching['notes-hop-delivery'];
check(hopLesson.steps.some(s=>s.body.includes('NAT')),'Explain translation exception');
check(hopLesson.steps.some(s=>s.body.includes('hop-by-hop forwarding')),'IP routing still uses hops');
check(hopLesson.steps.some(s=>s.body.includes('switch')&&s.body.includes('without changing')),'Switch versus router distinction');
for(let i=0;i<3;i++)check(hopDetail(i).includes('client port 51000 → service port 443')&&hopDetail(i).includes('laptop → server'),'Endpoint labels remain fixed');
check(hopDetail(0).includes('Laptop NIC')&&hopDetail(1).includes('Router A · outgoing')&&hopDetail(2).includes('Server NIC'),'Local interface labels change');
check(DATA.notesQuestions.filter(q=>q.lessonId==='notes-hop-delivery').length===4,'Delivery comprehension checks');
`,context);
console.log('PASS: delivery lesson distinguishes local switching, IP routing and translation; visual endpoint labels stay consistent.');
