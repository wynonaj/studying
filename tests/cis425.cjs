const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),read=p=>fs.readFileSync(path.join(root,p),'utf8');
const D=JSON.parse(read('dist/cis425-content.json'));
assert.equal(D.questions.length,84);assert.equal(D.sources.length,19);
assert.deepEqual(D.sources.map(x=>x.id),Array.from({length:19},(_,i)=>i+1));
assert.equal(D.sources.find(x=>x.id===3).units,786);
assert.equal(D.sources.find(x=>x.id===10).name,'CIS 425 - 827.pdf');
assert.equal(D.questions.filter(q=>q.sample).length,21);
for(const term of ['Plaintext','Ciphertext','Checksum','Data packet','Header','Payload / body','Symmetric cryptography','Asymmetric cryptography','Public key','Private key','Digital signature','Non-repudiation','SHA-256','Hard fork','Soft fork','Keylogger','Phishing','Metasploit','SET','Credential harvester','C2 server','Credential dumping','Process hollowing','Privilege escalation','EDR','SOC','TCP reverse shell','DoS','DDoS','SQLi','Buffer overflow','XSS','OS hardening','Least privilege','Firewall','ACL','Proxy server','IDS','IPS','Application allowlisting','Defense in depth','MFA','Attack chain'])assert.ok(D.vocab.some(v=>v.term===term),'Missing requested term: '+term);
assert.equal(D.checks.filter(x=>x.id.startsWith('425-scope-check-')).length,12);
assert.ok(D.coverage.some(x=>x.id==='requested-core'));
assert.match(D.questions[28].answer,/buffer overflow/i);
assert.match(D.questions[24].answer,/castle analogy/i);
assert.match(D.questions[41].answer,/not the smallest/i);
assert.equal(D.questions.filter(q=>q.uncertain).length,0);
for(const phrase of ['likely classroom intention','instructor-dependent','grading needs clarification','supplied wording does not establish'])assert.ok(!JSON.stringify(D).toLowerCase().includes(phrase),phrase);
assert.equal(D.questions[5].correct,'Security administrator');
for(const q of D.questions){assert.ok(q.answer.length>100,q.id);assert.ok(q.teach.length>50,q.id);assert.ok(q.example.length>50,q.id);assert.ok(q.refs.length);for(const [id,where] of q.refs){assert.ok(D.sources.some(s=>s.id===id),q.id);assert.ok(where)}}
const all=[...D.questions,...D.vocab,...D.checks,...D.cloze,...D.trueFalse];assert.equal(new Set(all.map(x=>x.id)).size,all.length);
for(const x of all){assert.match(x.id,/^425-/);assert.equal(new Set([x.correct,...x.distractors]).size,x.distractors.length+1,x.id);assert.ok(x.distractors.length===3||x.format==='tf',x.id);assert.ok(D.sections.some(s=>s.id===x.section),x.id);if(x.source)assert.ok(D.questions.some(q=>q.number===x.source&&q.section===x.section),x.id)}
for(const s of D.sorts){assert.ok(D.questions.some(q=>q.number===s.source));assert.equal(new Set(s.items).size,s.items.length)}
const elements=new Map();function element(s){if(!elements.has(s))elements.set(s,{innerHTML:'',textContent:'',value:'',disabled:false,dataset:{},focus(){},setAttribute(){},insertAdjacentHTML(_,s){this.innerHTML+=s},classList:{add(){}}});return elements.get(s)}
const saved=new Map([['cis320-v1','untouched-320'],['cis304-module1-v1','untouched-304'],['cis464-chapters-v1','untouched-464']]);
const ctx=vm.createContext({console,Date,Math,JSON,Set,BigInt,TextEncoder,Uint8Array,crypto:crypto.webcrypto,document:{querySelector:element,querySelectorAll:()=>[]},window:{scrollTo(){}},localStorage:{getItem:k=>saved.get(k)||null,setItem:(k,v)=>saved.set(k,v),removeItem:k=>saved.delete(k)},INPUT:D});
vm.runInContext(read('dist/cis425.js').split("document.addEventListener('click'")[0],ctx);const run=s=>vm.runInContext(s,ctx);run('D=INPUT');
assert.equal(D.foundations.length,D.vocab.length);
assert.equal(D.learningOrder.length,84);assert.equal(new Set(D.learningOrder).size,84);
run('section=0');assert.equal(run('nextLearningLesson(22).number'),47);assert.equal(run('nextLearningLesson(1).number'),37);
const seenDependencies=new Set(),activeDependencies=new Set();
function checkDependencies(id){assert.ok(!activeDependencies.has(id),'Circular prerequisite '+id);if(seenDependencies.has(id))return;activeDependencies.add(id);for(const dep of D.prerequisites[id]||[])checkDependencies(dep);activeDependencies.delete(id);seenDependencies.add(id)}
for(const id of Object.keys(D.prerequisites))checkDependencies(id);
const coreIds=D.basicRoute;
run('start("practice",[D.questions[19]])');
assert.equal(D.orientation.length,42);
const orientationIds=D.orientation.map(x=>x.id);
assert.ok(orientationIds.indexOf('425-introduction-encryption')<orientationIds.indexOf('425-context-5'));
assert.ok(orientationIds.indexOf('425-introduction-key')<orientationIds.indexOf('425-context-8'));
assert.ok(orientationIds.indexOf('425-introduction-hash')<orientationIds.indexOf('425-context-21'));
assert.match(D.orientation.find(x=>x.id==='425-context-18').teach,/HTTPS \(Hypertext Transfer Protocol Secure\).*TLS \(Transport Layer Security\)/);
for(const pool of ['questions','checks','vocab','foundations','orientation','topicOrientation'])for(const x of D[pool])for(const field of ['answer','teach','example']){
 const prose=x[field]||'';
 for(const acronym of ['TLS','HTTPS','IDS','IPS','EDR','SOC']){
  const re=new RegExp('\\b'+acronym+'\\b','g');let match;
  while((match=re.exec(prose)))assert.ok(prose.slice(match.index+acronym.length).startsWith(' ('+D.abbreviationExpansions[acronym]+')'),x.id+' expands '+acronym);
 }
}
assert.deepEqual(JSON.parse(run('JSON.stringify(session.items.slice(0,D.orientation.length).map(x=>x.id))')),D.orientation.map(x=>x.id));
assert.deepEqual(JSON.parse(run('JSON.stringify(session.items.slice(D.orientation.length,D.orientation.length+D.basicRoute.length).map(x=>x.id))')),coreIds);
for(const x of D.orientation){assert.equal(new Set([x.correct,...x.distractors]).size,4,x.id);assert.ok(x.foundation&&x.orientation);assert.ok(x.teach.length>50)}
run('start("practice",[D.questions[36]])');assert.equal(run('session.items[0].id'),'425-context-1');assert.match(element('#app').innerHTML,/saved report/);
assert.match(run('computerSetting(D.questions[36])'),/document/i);assert.match(run('computerSetting(D.questions[0])'),/storage drive/);
assert.equal(Object.keys(D.topicContexts).length,84);
for(const pool of ['questions','checks','vocab','foundations','trueFalse','cloze','sorts','discussions'])for(const x of D[pool]){
 assert.ok(x.setting,pool+' '+x.id);
 for(const field of ['object','location','purpose','action','example'])assert.ok(x.setting[field]?.length>20,pool+' '+x.id+' '+field);
 assert.ok(D.topicOrientation.some(t=>t.id===x.topicIntroId),x.id+' concrete introduction');
 assert.match(run('computerSetting('+JSON.stringify(x)+')'),/Situation:/);
}
for(const x of D.topicOrientation){assert.equal(new Set([x.correct,...x.distractors]).size,4,x.id);assert.ok(x.setting.location);}
assert.match(run('computerSetting(D.questions[83])'),/provider/);
assert.match(run('computerSetting(D.questions[7])'),/phone call/);
assert.match(run('computerSetting(D.questions[28])'),/database/);
assert.match(run('computerSetting(D.questions[34])'),/guest/);
assert.ok(D.foundations.find(x=>x.id===coreIds[7]).term==='Cryptographic key');
assert.match(element('#app').innerHTML,/Preparing for:/);
run('startLearningModule("core")');assert.equal(run('session.items.filter(x=>x.id.startsWith("425-first-check-")).length'),10);
run('startLearningModule("crypto")');assert.match(element('#app').innerHTML,/Computer context/);
assert.match(run('computerSetting(D.foundations.find(x=>x.term==="Cryptographic key"))'),/key value handled by software/);
assert.match(run('computerSetting(D.foundations.find(x=>x.term==="Hash function"))'),/downloaded/);
for(const group of [['IDS','IPS','Firewall','Proxy server','Application allowlisting'],['PCAP','Flow record'],['Confidentiality','Integrity','Availability'],['Security administrator','Security technician','Security manager','CISO']]){
 const situations=group.map(term=>D.foundations.find(x=>x.term===term).setting.object);
 assert.equal(new Set(situations).size,group.length,'Term-specific situations: '+group.join(', '));
}
for(const term of ['IDS','IPS','Firewall','Proxy server','Scalability','Endpoint','Keylogger']){const x=D.foundations.find(x=>x.term===term);assert.ok(x.setting.focus.includes(term));assert.match(run('computerSetting('+JSON.stringify(x)+')'),/Current focus:/);}
const earlyCases=D.orientation.filter(x=>x.id.startsWith('425-context-')).map(x=>x.context);assert.equal(new Set(earlyCases).size,earlyCases.length,'Continuing cases identify the new focus');
for(const term of ['Choke point','Visibility','Scalability','Endpoint','Asset','Threat','Risk','Mitigate','Vishing','VoIP','Flow record','Full packet capture','Reputation label','Manual analysis','Automated analysis','Cryptographic key','Double-spending problem','Byte stream','Datagram','Routing','Best-effort delivery','Stream cipher','Block cipher','Sponge construction','One-time pad'])assert.ok(D.foundations.some(x=>x.term===term),'Missing beginner definition '+term);
for(const x of D.foundations){assert.equal(new Set([x.correct,...x.distractors]).size,4,x.id);assert.ok(x.example.length>20,x.id)}
const foundationalIds=new Set([...D.vocab,...D.foundations].map(x=>x.id));
for(const ids of Object.values(D.prerequisites))for(const id of ids)assert.ok(foundationalIds.has(id),'Unknown prerequisite '+id);
for(const q of D.questions){
 const ids=JSON.parse(run(`JSON.stringify(foundationSequence([D.questions[${q.number-1}]]).map(x=>x.id))`));
 assert.equal(ids.at(-1),q.id);assert.equal(new Set(ids).size,ids.length);
 for(const id of D.prerequisites[q.id])assert.ok(ids.indexOf(id)>=0&&ids.indexOf(id)<ids.indexOf(q.id),'Definition before '+q.id);
 assert.ok(ids.indexOf(q.topicIntroId)>=0&&ids.indexOf(q.topicIntroId)<ids.indexOf(q.id),'Concrete situation before '+q.id);
}
run('start("practice",[D.questions[7]])');
assert.ok(run('session.items.findIndex(x=>x.term==="Vishing"&&x.foundation)<session.items.findIndex(x=>x.id===D.questions[7].id)'));
assert.equal(run('session.items[0].foundation'),true);
const firstDefinition=run('session.items[0].id');run('grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items[session.index].id'),firstDefinition);
run('grade(session.items[session.index],true,session.items[session.index].correct);advance()');assert.ok(run('session.cleared.has('+JSON.stringify(firstDefinition)+')'));
run('start("practice",[D.questions[7]])');assert.equal(run('session.items[0].id'),firstDefinition,'Each session includes definitions again');
run('start("practice",D.questions)');assert.equal(run('session.items.filter(x=>D.questions.some(q=>q.id===x.id)).length'),84,'Every original lesson remains');
assert.match(D.questions[1].teach,/CC means credit card/);assert.match(D.questions[1].teach,/# symbol means number/);
assert.match(D.questions[72].q,/manual analysis, automated analysis, static analysis, and dynamic analysis/i);
assert.match(D.questions[55].q,/stream cipher, a block cipher, a sponge construction, and a one-time pad/i);
for(const q of D.questions)assert.ok(!/^(Match |Tune detection using evidence|Structure and correct key use both matter)/.test(q.correct),q.id+' needs a concrete answer');
for(let section=0;section<=8;section++){run('section='+section);for(const v of ['beginner','samples','coverage','teach','practice','flash','map','exam','apply','sort','abbrev','math','discussion','terms','guide','readings']){run(`navigate('${v}')`);assert.ok(element('#app').innerHTML.length>100,v)}}
run('section=0');for(const q of D.questions){for(let step=0;step<3;step++)run(`openLesson(${q.number},${step})`)}
run('examHome()');element('#mock-exam').onclick();assert.equal(run('session.total'),45);
assert.equal(run('session.items.filter(x=>x.format==="tf").length'),15);assert.equal(run('session.items.filter(x=>x.format==="fill").length'),10);
assert.equal(run('session.items.filter(x=>x.uncertain).length'),0);assert.equal(run('new Set(session.items.map(x=>x.id)).size'),45);
run('grade(session.items[0],false,"wrong");advance()');assert.equal(run('session.items.length'),45);assert.equal(run('session.right'),0);
run('start("practice",D.questions.slice(4,9));session.index=session.items.findIndex(x=>x.id===D.questions[4].id);renderSession()');const beforeRetry=run('session.items.length'),retryIndex=run('session.index');run('grade(session.items[session.index],false,"wrong");advance()');assert.equal(run('session.items.length'),beforeRetry+1);assert.equal(run(`session.items[Math.min(${retryIndex}+4,${beforeRetry})].id`),D.questions[4].id);
run('start("flash",[D.questions[5]]);session.index=session.items.findIndex(x=>x.id===D.questions[5].id);renderSession()');element('#flip').onclick();assert.match(element('#flip').innerHTML,/Security administrator/);element('#remembered').onclick();assert.ok(run('progress.cards[D.questions[5].id].completed'));
for(const name of ['defense','keys','chain'])run(`mapHome('${name}')`);
for(let i=0;i<3;i++){run('rsaCase='+i);assert.equal(run('rsaResult(rsaCases[rsaCase]).plain'),run('rsaCases[rsaCase].m'));assert.equal(run('(rsaCases[rsaCase].e*rsaCases[rsaCase].d)%rsaResult(rsaCases[rsaCase]).phi'),1)}
assert.equal(run('modPow(7,3,55)'),13);
run('mathHome()');for(let i=0;i<5;i++)element('#rsa-step').onclick();assert.equal(element('#rsa-step').disabled,true);
for(const [key,value] of [['cis320-v1','untouched-320'],['cis304-module1-v1','untouched-304'],['cis464-chapters-v1','untouched-464']])assert.equal(saved.get(key),value);
assert.ok(saved.has('cis425-midterm-v1'));assert.ok(!read('dist/cis425.js').includes('Enterprise Resource Planning'));
run('section=0;progress.lessons={};progress.lessonSteps={};progress.lastLesson=null;openLesson(7,1);navigate("teach")');
assert.match(element('#app').innerHTML,/Resume · Step 2 of 3/);
assert.match(element('#app').innerHTML,/YOUR SAVED PLACE/);
run('openLesson(7)');assert.equal(run('lesson.step'),1);
assert.equal(JSON.parse(saved.get('cis425-midterm-v1')).lastLesson.number,7);
run('openLesson(7,2)');element('#lesson-complete').onclick();run('navigate("teach")');
assert.match(element('#app').innerHTML,/lesson-is-complete/);assert.match(element('#app').innerHTML,/✓ Completed/);
run('progress=JSON.parse(localStorage.getItem(KEY425));openLesson(7)');assert.equal(run('lesson.step'),2);assert.equal(run('progress.lessons[D.questions[6].id]'),true);
run('progress.lessonSteps[D.questions[6].id]=99;openLesson(7)');assert.equal(run('lesson.step'),0);
run('progress.lessons[D.questions[21].id]=true;progress.lessonSteps[D.questions[46].id]=1;progress.lastLesson={number:47,section:1};beginnerHome()');
assert.match(element('#app').innerHTML,/YOUR SAVED PLACE/);
assert.match(element('#app').innerHTML,/✓ Completed/);
assert.match(element('#app').innerHTML,/Resume · Step 2 of 3/);
for(const fn of ['samplesHome','coverageHome','guideHome','discussionHome']){run('section=0;'+fn+'()');assert.match(element('#app').innerHTML,/lesson-state/,fn);}
run('termsHome()');assert.match(element('#terms').innerHTML,/lesson-state/);
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
run('practiceHome()');element('#recall-blanks').onclick();assert.equal(run('session.mode'),'flash');assert.ok(run('session.total')>=D.cloze.length);assert.equal(run('session.items.filter(x=>D.cloze.some(c=>c.id===x.id)).length'),D.cloze.length);
console.log('PASS CIS 425: 21 exact professor examples, 19 source records, 84 lessons, chapter/lecture coverage, beginner route, 5/7 discussions, isolated progress, exam scoring, retries, flashcards, blank recall, navigation, and RSA.');
run('start("practice",[D.questions[7]]);grade(session.items[0],true,session.items[0].correct);advance();grade(session.items[session.index],false,"wrong")');
const savedIndex=run('session.index'),savedCard=run('session.items[session.index].id'),savedXP=run('progress.xp'),savedTotal=run('session.total');
run('session=null;navigate("teach")');assert.match(element('#app').innerHTML,/Continue where you left off/);assert.match(element('#app').innerHTML,/Restart this session/);
run('resumeSavedSession()');assert.equal(run('session.index'),savedIndex);assert.equal(run('session.items[session.index].id'),savedCard);assert.equal(run('session.graded'),true);assert.equal(run('progress.xp'),savedXP);assert.equal(run('session.cleared.size'),1);
const retainedLessons=run('JSON.stringify(progress.lessons)');run('resumeSavedSession(true)');assert.equal(run('session.index'),0);assert.equal(run('session.total'),savedTotal);assert.equal(run('session.items.length'),savedTotal);assert.equal(run('session.cleared.size'),0);assert.equal(run('progress.xp'),savedXP);assert.equal(run('JSON.stringify(progress.lessons)'),retainedLessons);
run('start("flash",[D.questions[5]])');element('#flip').onclick();run('session=null;resumeSavedSession()');assert.equal(run('session.revealed'),true);
run('start("exam",D.trueFalse.slice(0,2));grade(session.items[0],true,session.items[0].correct);advance();session=null;resumeSavedSession()');assert.equal(run('session.mode'),'exam');assert.equal(run('session.index'),1);assert.equal(run('session.right'),1);
run('session.index=session.items.length;finish()');assert.equal(run('readActiveSession()'),null);
run('start("practice",D.questions)');assert.ok(saved.get('cis425-midterm-v1-active-session').length<2000000,'Compact session storage');
assert.match(read('dist/cis425.js'),/fn\(\);showSavedSession\(\)/);
console.log('PASS CIS 425 session restore: exact position, graded feedback, no duplicate XP, restart retains overall progress, flash reveal, exam score, completed-session cleanup, and compact storage.');
for(const pool of ['questions','checks','vocab','foundations','orientation','topicOrientation','trueFalse','cloze','sorts','discussions'])for(const x of D[pool]){
 assert.ok(x.purpose?.length>30,pool+' '+x.id+' purpose');
 assert.match(run('purposeBlock('+JSON.stringify(x)+')'),/<h3>Purpose<\/h3>/);
 for(const key of ['starting','operation','result','use'])assert.ok(x.walkthrough?.[key]?.length>25,pool+' '+x.id+' '+key);
 assert.match(run('resultWalkthrough('+JSON.stringify(x)+')'),/How the result is used/);
 assert.ok(x.timeline?.length>=4,pool+' '+x.id+' timeline');
 for(const step of x.timeline)for(const field of ['when','who','event'])assert.ok(step[field]?.length>4,x.id+' '+field);
}
assert.ok(D.vocab.some(x=>x.term==='Hash value'));
for(const name of ['reference','start','two','later','deterministic'])assert.ok(D.orientation.some(x=>x.id==='425-timeline-check-'+name));
const downloadTimeline=D.hashTimeline.map(x=>x.event).join(' ');
assert.match(downloadTimeline,/does not imply/);assert.match(downloadTimeline,/not comparing the file with itself/);assert.match(downloadTimeline,/earlier baseline/);
assert.match(run('hashResultExplanation("original","edited","111","222")'),/supplied contents differ/);
assert.match(run('hashResultExplanation("same","same","111","111")'),/values match/);
run('mathHome()');assert.match(element('#app').innerHTML,/Reference contents/);assert.match(element('#app').innerHTML,/who does what and when/);
run('start("practice",[D.orientation.find(x=>x.id==="425-context-23")])');
assert.match(run('feedback(D.orientation.find(x=>x.id==="425-context-23"),true)'),/Purpose/);
assert.match(D.orientation.find(x=>x.id==='425-context-23').purpose,/trusted reference/);
const hashWalkthrough=D.orientation.find(x=>x.id==='425-context-24').walkthrough;
for(const text of ['Amount: 10','Amount: 90'])assert.ok(hashWalkthrough.workedExample.includes(crypto.createHash('sha256').update(text,'utf8').digest('hex')),'Worked hash value '+text);
assert.match(hashWalkthrough.use,/compares the computed digest with the trusted reference/);
for(const suffix of ['compare','alone','mismatch'])assert.ok(D.orientation.some(x=>x.id==='425-result-check-'+suffix));
assert.match(D.foundations.find(x=>x.term==='IDS').purpose,/notify defenders/);
assert.match(D.foundations.find(x=>x.term==='Checksum').purpose,/accidental corruption/);
run('start("flash",[D.questions[5]])');element('#flip').onclick();assert.match(element('#flip').innerHTML,/<h3>Purpose<\/h3>/);
run('progress.completedSessions=[];session={mode:"practice",items:D.questions.slice(0,6).map(prepare),index:0,total:6,cleared:new Set(),first:{},right:0,graded:false,revealed:false,lessonNumber:null};session.initial=session.items.map(describeSessionItem);renderSession()');
for(let i=0;i<6;i++){run('grade(session.items[session.index],true,session.items[session.index].correct)');if(i<5)run('advance()')}
assert.match(element('#feedback').innerHTML,/✓ Completed/);assert.equal(run('progress.completedSessions.length'),1);assert.equal(run('progress.completedSessions[0].total'),6);
const completeKey=run('progress.completedSessions[0].key'),completeXP=run('progress.xp');
run('resumeSavedSession(true)');assert.equal(run('session.index'),0);assert.equal(run('progress.completedSessions.length'),1);assert.equal(run('progress.xp'),completeXP);
run('restoreBeforeRestart()');assert.equal(run('session.index'),5);assert.equal(run('session.cleared.size'),6);assert.match(element('#feedback').innerHTML,/✓ Completed/);assert.equal(run('progress.completedSessions[0].attempts'),1);
run('progress=JSON.parse(localStorage.getItem(KEY425));session=null;navigate("practice")');assert.match(element('#app').innerHTML,/Saved completions/);
run('viewCompletedSession('+JSON.stringify(completeKey)+')');assert.match(element('#app').innerHTML,/completed all 6 items/);assert.equal(run('progress.xp'),completeXP);
run('reviewCompletedSession('+JSON.stringify(completeKey)+')');assert.equal(run('progress.completedSessions.length'),1);
console.log('PASS CIS 425 completion: green saved completion before leaving the last answer, persistence across reload and restart, previous-place restoration, no duplicate attempts/XP, and completed-result review.');
