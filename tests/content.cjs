const fs=require('fs'),vm=require('vm'),assert=require('assert');
const context=vm.createContext({localStorage:{getItem:()=>null},console});
vm.runInContext(fs.readFileSync('dist/vocab.js','utf8'),context);
let app=fs.readFileSync('dist/app.js','utf8');vm.runInContext(app.split("document.addEventListener('click'")[0],context);
context.data=JSON.parse(fs.readFileSync('dist/content.json'));
vm.runInContext('DATA=data',context);
let result=vm.runInContext(`(()=>{let banks=[...all(),...DATA.understanding,...labItems(),...conversionCards()];for(let x of banks){let mc=makeMC(x);if(mc.options.length!==4||new Set(mc.options).size!==4||mc.options.filter(a=>a===mc.answer).length!==1)throw Error('Bad options: '+x.id);if(!explanationHTML(mc,mc.answer).includes('Correct'))throw Error('Missing explanation '+x.id)}let counts=[];for(let c of DATA.chapters){let pool=learnPool().filter(x=>x.ch===c.id);for(let i=0;i<100;i++){let sample=mixedReview(pool);if(sample.length!==10||new Set(sample.map(x=>x.id)).size!==10||sample.some(x=>x.ch!==c.id))throw Error('Bad chapter mixture');for(let kind of new Set(pool.map(x=>x.kind)))if(!sample.some(x=>x.kind===kind))throw Error('Missing '+kind);if(sample.some(x=>x.kind==='understanding'))throw Error('Separate bank leaked')}counts.push({chapter:c.id,count:pool.length,types:[...new Set(pool.map(x=>x.kind))]})}if(DATA.understanding.length!==54)throw Error('Coverage');for(let x of DATA.understanding){let source=DATA.questions.find(q=>q.id===x.sourceId);if(!source||source.ch!==x.ch)throw Error('Invalid source');if(!explanationHTML(x,x.answer).includes('Study-guide topic'))throw Error('Source not displayed')}return {banksTested:banks.length,counts}})()`,context);
assert.equal(context.data.questions.length,54);assert.equal(new Set(context.data.questions.map(q=>q.id)).size,54);assert.equal(new Set(context.data.understanding.map(q=>q.sourceId)).size,54);
assert(!app.includes('id="response"')&&!app.includes('<textarea'));
console.log(JSON.stringify(result,null,2));console.log('PASS: 54 original prompts present, authored choices unique, sources valid, 500 chapter mixtures correctly scoped, no typed answers.');
vm.runInContext(`
record=()=>{};renderSession=()=>{};
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
check(explanationHTML(physical,physical.answer).includes('copper carries electrical signals'),'Physical answer has a concrete explanation');
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
