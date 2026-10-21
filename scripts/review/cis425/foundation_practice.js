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
 return setting?`<section class="card computer-setting"><p><b>Situation:</b> ${esc(setting.object)}</p><p><b>Location:</b> ${esc(setting.location)}</p>${x.topicOrientation?'':`<p><b>Security task:</b> ${esc(setting.purpose)}</p>`}${setting.example?`<p><b>Concrete example:</b> ${esc(setting.example)}</p>`:''}<details><summary>What happens and why it matters</summary><p>${esc(setting.action)}</p></details></section>`:'';
}
function examSetting(x){
 const setting=x.setting||D.topicContexts[String(x.number||x.source)];
 return setting?`<details class="card computer-setting"><summary>Scenario context</summary><p><b>Situation:</b> ${esc(setting.object)}</p><p><b>Location:</b> ${esc(setting.location)}</p></details>`:'';
}
function practiceDefinitions(x){
 const lookup=new Map([...D.vocab,...D.foundations].map(v=>[v.id,v]));
 const defs=prerequisiteIds(x).map(id=>lookup.get(id)).filter(v=>v?.foundation);
 return defs.length?`<details class="card practice-glossary"><summary>Words in this question · ${defs.length} definitions</summary><dl>${defs.map(v=>`<dt><b>${esc(v.term)}</b>${v.exp?' · '+esc(v.exp):''}</dt><dd>${esc(v.answer)}</dd>`).join('')}</dl></details>`:'';
}
