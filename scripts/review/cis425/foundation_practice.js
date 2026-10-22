function prerequisiteIds(x){return D.prerequisites[x.id]||D.prerequisites[x.id.replace(/-build$/,'')]||D.prerequisites[source(x)?.id]||[]}
function foundationSequence(items){
 const lookup=new Map([...D.vocab,...D.foundations,...D.orientation,...D.topicOrientation].map(x=>[x.id,x]));
 const scheduled=new Set(),visiting=new Set(),result=[];
 function add(x,context){
  if(scheduled.has(x.id)||visiting.has(x.id))return;
  visiting.add(x.id);
  if(!x.foundation&&!x.term&&x.topicIntroId){const intro=lookup.get(x.topicIntroId);if(intro)add(intro,context)}
  for(const id of prerequisiteIds(x)){const prerequisite=lookup.get(id);if(prerequisite)add({...prerequisite,foundation:true},context)}
  visiting.delete(x.id);
  if(!scheduled.has(x.id)){scheduled.add(x.id);result.push(x.term?{...x,foundation:true,preparingFor:context}:x.orientation?{...x,preparingFor:context}:x)}
 }
 for(const x of D.orientation)add(x,'Files, messages, encryption, and file comparison');
 for(const id of D.basicRoute||[]){const x=lookup.get(id);if(x)add(x,'Computer and cryptography basics')}
 const rank=new Map((D.learningOrder||[]).map((n,i)=>[n,i]));
 const ordered=[...items].sort((a,b)=>(rank.get(a.number||a.source)??999)-(rank.get(b.number||b.source)??999));
 for(const x of ordered)add(x,source(x)?.title||x.term||'This topic');
 return result;
}
function practiceLocation(x){
 const topic=source(x),module=D.learningModules?.find(m=>m.lessons.includes(topic?.number));
 return `<section class="practice-location"><p><b>${x.orientation?'Computer context':x.foundation?'Learning a term':'Applying the concept'}:</b> ${esc(x.orientation?'Files, messages, encryption, and file comparison':x.term||topic?.title||'Midterm practice')}</p><p>${x.foundation?'Preparing for: '+esc(x.preparingFor||topic?.title||'Core vocabulary'):esc(module?.title||'Midterm review')}</p></section>`+computerSetting(x);
}
function computerSetting(x){
 if(x.orientation)return `<section class="card computer-setting"><p>${esc(x.context)}</p></section>`;
 const setting=x.setting||D.topicContexts[String(x.number||x.source)]||D.practicalContexts[x.contextKey||source(x)?.contextKey];
 return setting?`<section class="card computer-setting">${setting.focus?`<p><b>Current focus:</b> ${esc(setting.focus)}</p>`:''}<p><b>Situation:</b> ${esc(setting.object)}</p><p><b>Location:</b> ${esc(setting.location)}</p>${x.topicOrientation?'':`<p><b>Security task:</b> ${esc(setting.purpose)}</p>`}${setting.example&&setting.example!==setting.object?`<p><b>Concrete example:</b> ${esc(setting.example)}</p>`:''}<details><summary>What happens and why it matters</summary><p>${esc(setting.action)}</p></details></section>`:'';
}
function examSetting(x){
 const setting=x.setting||D.topicContexts[String(x.number||x.source)];
 return setting?`<details class="card computer-setting"><summary>Scenario context</summary><p><b>Situation:</b> ${esc(setting.object)}</p><p><b>Location:</b> ${esc(setting.location)}</p></details>`:'';
}
function purposeBlock(x){
 const purpose=x.purpose||source(x)?.purpose;
 return purpose?`<section class="concept-purpose"><h3>Purpose</h3>${paragraphs(purpose)}${resultWalkthrough(x)}</section>`:'';
}
function resultWalkthrough(x){
 const flow=x.walkthrough||source(x)?.walkthrough;if(!flow)return '';
 return `<dl class="result-walkthrough">${[['Starting point','starting'],['What happens','operation'],['Result','result'],['How the result is used','use']].map(([label,key])=>`<dt><b>${label}</b></dt><dd>${esc(flow[key])}</dd>`).join('')}</dl>${timelineBlock(x)}${flow.workedExample?`<details class="worked-result"><summary>Worked example with actual values</summary><p>${esc(flow.workedExample)}</p></details>`:''}`;
}
function timelineBlock(x){
 const steps=x.timeline||source(x)?.timeline;
 return steps?.length?`<details class="concept-timeline" open><summary>Timeline: who does what and when</summary><ol>${steps.map(step=>`<li><b>${esc(step.when)}</b><p><strong>${esc(step.who)}:</strong> ${esc(step.event)}</p></li>`).join('')}</ol></details>`:'';
}
function hashResultExplanation(a,b,ha,hb){
 return `<h3>1. Reference calculation</h3><p>The program read the reference text: <b>${esc(a)}</b>.</p><p>Calculated hash value: <code>${esc(ha)}</code></p><h3>2. Download calculation</h3><p>The program read your simulated downloaded text: <b>${esc(b)}</b>.</p><p>Calculated hash value: <code>${esc(hb)}</code></p><h3>3. Compare the two calculated values</h3><p>${ha===hb?'The values match. In this example, the comparison supports matching contents.':'The values differ. The supplied contents differ; the simulated copy does not match the reference.'}</p><h3>4. Use the result</h3><p>${ha===hb?'For a real download, also establish that the reference comes from a trusted source for the exact release. A hash match alone does not certify that software is harmless.':'For a real download, investigate or obtain the correct file before relying on it. A mismatch does not say whether the cause was an error, a legitimate different version, or an attacker.'}</p><p>These calculations did not encrypt, repair, or replace either text. This is a text simulation; a file-checking tool reads the actual file’s bytes.</p>`;
}
function practiceDefinitions(x){
 const lookup=new Map([...D.vocab,...D.foundations].map(v=>[v.id,v]));
 const defs=prerequisiteIds(x).map(id=>lookup.get(id)).filter(v=>v?.foundation);
 return defs.length?`<details class="card practice-glossary"><summary>Words in this question · ${defs.length} definitions</summary><dl>${defs.map(v=>`<dt><b>${esc(v.term)}</b>${v.exp?' · '+esc(v.exp):''}</dt><dd>${esc(v.answer)}</dd>`).join('')}</dl></details>`:'';
}
