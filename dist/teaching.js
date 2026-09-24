'use strict';
const TEACH_CHAPTERS={1:'Introduction, layering & authorities',2:'Physical layer, cabling, modulation & Shannon’s law',3:'Data Link, Ethernet, MAC addresses & switching',4:'Network layer, IP addresses, CIDR & bits',12:'Network design, structured cabling & campus architecture'};
const JARGON={
'IPv6':'Internet Protocol version 6. Its addresses contain 128 bits, normally written as eight groups of hexadecimal digits. It provides far more possible addresses than 32-bit IPv4.',
'End-user':'A person who actually uses a system—for example, a student using a laptop or an employee opening email. They do not have to be the person who built or manages the network.',
'Allocation':'Giving an organization a resource to manage or distribute. For IP addresses, an allocation is a block of addresses given to an organization such as an Internet service provider. It is like giving an office a numbered set of tickets to distribute.',
'Public IP':'An IP address from globally coordinated address space intended for Internet use, rather than a private address reused inside local networks. Public does not mean anyone can access the device; firewalls and routing still matter.',
'RIR':'Regional Internet Registry: an organization that manages and registers Internet-number resources in a geographic service region. ARIN is one example. RIRs coordinate public address blocks; they are not routers inside buildings.',
'Working group':'A group of real people, such as engineers and technical experts, developing and reviewing a technical proposal. In Chapter 12, they help write network standards. This does not mean a group of computers.',
'Standard':'A shared written set of technical requirements. Manufacturers can follow the same requirements so their products work together.',
'Specification':'A document describing exactly how something should behave or be built. A standard is a specification approved through a standards process.',
'Interoperability':'The ability of separately built products or systems to work together—for example, equipment from different vendors communicating using the same standard.',
'Layer':'One set of responsibilities in a model. Always ask which model: OSI/TCP/IP communication layers are different from Access/Distribution/Core campus design layers.',
'Protocol':'Agreed rules for communication: what messages look like and how participants respond.',
'Packet':'A unit of data handled by the Network layer. An IP packet includes addressing information used for routing.',
'Frame':'A Data Link layer package used for delivery across a local link. An Ethernet frame includes MAC addresses, payload and an error check.',
'Session':'An ongoing communication conversation. The OSI Session layer describes starting, managing and ending sessions.',
'Encapsulation':'Adding headers, and sometimes trailers, around data. Think of adding delivery labels or wrapping.',
'Header':'Control information placed before carried data. It may contain addresses or other instructions for the receiving layer.',
'IEEE':'Institute of Electrical and Electronics Engineers. It develops standards including Ethernet and Wi-Fi.',
'IETF':'Internet Engineering Task Force. Its participants develop Internet protocol standards.',
'OSI':'Open Systems Interconnection: a seven-layer reference model for describing networking functions.',
'Bit':'One binary digit: either 0 or 1. Eight bits together make a byte.',
'Byte':'Eight bits. One IPv4 octet is eight bits and can represent a decimal value from 0 through 255.',
'Octet':'A group of exactly eight bits. An IPv4 address contains four octets separated by dots when written in decimal.',
'Binary':'A number system with only two digits, 0 and 1. From right to left, positions have values 1, 2, 4, 8, 16, 32, 64 and 128 in an eight-bit group.',
'Hexadecimal':'A base-16 number system: 0–9 and A–F, where A=10 through F=15. One hexadecimal digit represents four bits.',
'Hextet':'One 16-bit group in an IPv6 address, written using up to four hexadecimal digits.',
'Subnet':'A group of IP addresses sharing the same starting network-prefix bits. The other bits distinguish positions within that group.',
'Prefix':'The starting network portion of an IP address. In /17, the first 17 bits are network bits; the slash number is a bit count, not an octet value.',
'Host':'A device or network endpoint, such as a computer or server. In subnet calculations, host bits are the positions left after the network prefix.',
'Network address':'The first address of an IPv4 block, found by keeping network bits and setting all host bits to 0. It names the subnet in traditional subnetting.',
'Broadcast address':'In a traditional IPv4 subnet, the address with all host bits set to 1. It is used to address all hosts on that subnet. /31 point-to-point links and /32 host routes are special cases.',
'Subnet mask':'Thirty-two bits with 1s for the network-prefix positions and 0s for host positions. /17 becomes 255.255.128.0.',
'IP address':'A logical network address used to identify an interface and route packets. IPv4 addresses contain 32 bits; IPv6 addresses contain 128.',
'MAC address':'A link-layer interface address used for local delivery. Traditional Ethernet MAC addresses contain 48 bits. They can be factory-assigned or set in software.',
'Router':'A device that forwards IP packets between networks using routing information.',
'ISP':'Internet service provider: an organization that supplies Internet connectivity to customers.',
'Medium':'The path carrying a signal, such as copper cable, optical fiber or radio through space.',
'Signal':'A physical change that carries information, such as electrical voltage, light or a radio wave.',
'UTP':'Unshielded Twisted Pair: copper wire pairs twisted to help reduce interference, without shielding.',
'Interference':'Unwanted signals or noise that make the intended signal harder to distinguish.',
'Gbps':'Gigabits per second: billions of bits transmitted per second. Lowercase b means bits; bytes contain eight bits.',
'Core (fiber)':'The inner light-guiding part of an optical fiber. This is different from the Core layer of a campus network.',
'Single-mode':'Fiber with a small core supporting one propagation mode at the operating wavelength; commonly used for longer links.',
'Multimode':'Fiber with a larger core supporting several propagation modes; commonly used for shorter links.',
'Amplitude':'A wave’s strength or size—often drawn as its height.',
'Frequency':'How many cycles of a wave occur each second, measured in hertz (Hz).',
'Phase':'A wave’s position within its repeating cycle, often expressed as an angle.',
'Bandwidth':'In signal theory, a range of frequencies measured in hertz. In casual networking language it often means data capacity; check which meaning the question uses.',
'Multiplexing':'Combining several channels so they can share a physical medium.',
'Signal-to-noise ratio':'Signal power compared with noise power. A larger ratio means the intended signal is stronger relative to the noise.',
'Payload':'The data carried inside a package, excluding that package’s own header and trailer.',
'FCS':'Frame Check Sequence: an error-detection value carried at the end of an Ethernet frame.',
'OUI':'Organizationally Unique Identifier: the manufacturer-allocation portion in the traditional universally assigned MAC format.',
'Half-duplex':'Communication can go in either direction, but not both directions at the same time.',
'Collision':'Overlapping transmissions on a shared Ethernet medium that prevent normal reception.',
'Backoff':'Waiting before retrying. Random delays help devices avoid colliding again together.',
'Switch':'A device that normally learns MAC-address-to-port mappings and forwards local frames.',
'Port':'Context matters: a physical switch port is a connection socket; a Transport port number identifies an application endpoint.',
'Topology':'The arrangement of network connections, such as star, bus, ring or mesh.',
'Campus':'A group of nearby buildings whose networks are connected—for example, a university or company site.',
'Core layer':'In Chapter 12 campus design, the fast backbone linking major network regions. This is not an OSI layer or a fiber’s glass core.',
'Distribution layer':'In campus design, the tier grouping access networks and commonly handling routing and policy.',
'Access layer':'In campus design, where end-user devices connect through switch ports or wireless access points.',
'Backbone':'The main high-capacity connections linking major parts of a network—like its main highway.',
'Logical design':'The plan for network organization, addressing, connections and services.',
'Physical design':'The equipment, media and installation choices that implement the plan.',
'Demarc':'Demarcation point: the boundary between a provider’s network and the customer’s network.',
'MDF':'Main Distribution Frame: a main telecommunications distribution point or facility.',
'IDF':'Intermediate Distribution Frame: a secondary distribution point serving a floor or area and connected to the main distribution system.',
'SNMP':'Simple Network Management Protocol: lets management software read device information and request supported, authorized changes.',
'Agent':'For SNMP, software on a managed device that answers management requests. It is not a human assistant.',
'MIB':'Management Information Base: the definitions and organization of managed objects. Agents expose the actual values described by these objects.',
'Polling':'Repeatedly asking for updated information, such as querying a device’s interface counter.'
};
let teachingState=null;
const completedOnce=x=>Boolean(progress.cards[x.id]?.firstCorrectAt||progress.cards[x.id]?.level>0);
function renderModeBar(){let host=$('#modebar');if(!host)return;const teaching=['teach','decoder'].includes(view);host.innerHTML=`<button data-nav="teach" class="${teaching?'active':''}" aria-pressed="${teaching}">Learn First</button><button data-nav="learn" class="${!teaching?'active':''}" aria-pressed="${!teaching}">Practice Quiz</button><button data-jargon="">Jargon translator</button>`}
function jargonChips(terms){return `<div class="jargon-chips">${terms.map(t=>`<button data-jargon="${esc(t)}">${esc(t)} <span aria-hidden="true">?</span></button>`).join('')}</div>`}
function showJargon(term){const dialog=document.createElement('dialog');dialog.className='lesson-dialog';dialog.innerHTML=`<button class="close-lesson">Close glossary</button><h2>Jargon translator</h2><label>Find a word <input type="search" class="jargon-search" placeholder="Try allocation, end-user or working group" value="${esc(term||'')}"></label><div class="jargon-results"></div>`;document.body.append(dialog);const update=()=>{const q=dialog.querySelector('input').value.trim().toLowerCase();dialog.querySelector('.jargon-results').innerHTML=Object.entries(JARGON).filter(([k,v])=>(k+' '+v).toLowerCase().includes(q)).map(([k,v])=>`<article><h3>${esc(k)}</h3><p>${esc(v)}</p></article>`).join('')||'<p>No match. Try a shorter word.</p>'};dialog.querySelector('input').oninput=update;dialog.querySelector('button').onclick=()=>dialog.close();dialog.onclose=()=>dialog.remove();update();dialog.showModal()}
function lessonFor(x){if(x.lessonId)return x.lessonId;if(x.sourceId){const q=DATA.questions.find(q=>q.id===x.sourceId);if(q?.lessonId)return q.lessonId}const term=x.term||'';if(['RIR','ARIN','RIPE NCC','APNIC','LACNIC','AFRINIC','Allocation','Public IP'].includes(term))return 'notes-4-4';if(['Core layer','Distribution layer','Access layer','Campus network','Backbone'].includes(term))return 'notes-12-3';if(['Working group','Standard','Interoperability'].includes(term))return 'notes-12-5';if(x.ch===4&&(x.kind==='number'||x.id?.startsWith('subnet-')||/CIDR|Prefix|Host|Network address|Broadcast address|Subnet/.test(term)))return 'notes-4-2';if(x.id==='sort-campus')return 'notes-12-3';if(x.kind==='sort'&&x.ch===1)return x.orderId==='osi'?'notes-1-3':'notes-1-2';const found=DATA.notes.find(n=>n.ch===x.ch&&term&&n.body.toLowerCase().includes(term.toLowerCase()));return found?.id||DATA.notes.find(n=>n.ch===x.ch&&n.id!=='notes-big-picture')?.id}
function questionContext(x){const t=DATA.teaching?.[lessonFor(x)];return `Chapter ${x.ch} · ${t?.title||TEACH_CHAPTERS[x.ch]||'Networking practice'}`}
function preTeachHTML(x){const id=lessonFor(x),t=DATA.teaching?.[id];if(!t)return '';return `<details class="teach-before"><summary>Show Explanation & Rule · Teach me first</summary><span class="tag">${esc(questionContext(x))}</span><p>${esc(t.context)}</p><p><b>Picture it:</b> ${esc(t.analogy)}</p>${jargonChips(t.terms)}${id==='notes-4-2'?'<button data-open-decoder>Dissect an address step by step</button>':''}<button data-lesson="${esc(id)}">Read the full explanation</button></details>`}
function teachHome(){const done=progress.lessons||{};$('#app').innerHTML=heading('Learn first. Then try it.','Start with what the words mean, see an example, then answer a question.')+`<section class="card"><h2>Start from zero</h2><p>You do not need to know the vocabulary first. Each topic explains where it fits, defines the words, walks through an example, then lets you try.</p><div class="actions"><button class="primary" data-teach="notes-big-picture">How a network works</button><button data-nav="decoder">Explore IPv4 bits & subnet math</button><button data-teach="teach-convert-binary-decimal">Learn binary, decimal & hex from zero</button></div></section><div class="notes-list">${DATA.chapters.filter(c=>!chapter||c.id===chapter).map(c=>{const lessons=DATA.notes.filter(n=>n.ch===c.id&&n.id!=='notes-big-picture'),count=lessons.filter(n=>done[n.id]).length;return `<section class="card"><span class="tag">Chapter ${c.id}</span><h2>${esc(TEACH_CHAPTERS[c.id])}</h2><p>${count} / ${lessons.length} lessons complete</p><div class="bar"><span style="width:${100*count/lessons.length}%"></span></div><div class="lesson-buttons">${lessons.map(n=>`<button data-teach="${n.id}">${done[n.id]?'✓ ':''}${esc(DATA.teaching[n.id].title)}${done[n.id]?' · Complete':''}</button>`).join('')}</div></section>`}).join('')}</div>`;document.querySelectorAll('[data-teach]').forEach(b=>b.onclick=()=>{teachingState={id:b.dataset.teach,step:0};renderTeaching()})}
function renderTeaching(){view='teach';renderModeBar();const st=teachingState,n=DATA.notes.find(n=>n.id===st.id),t=DATA.teaching[st.id],labels=t.steps?[...t.steps.map(s=>s.title),'Your turn']:['Where this fits','Words you need','Picture it','Worked example','Your turn'];const questions=DATA.notesQuestions.filter(q=>q.lessonId===n.id);const fallback=DATA.questions.filter(q=>q.lessonId===n.id);let checks=questions.length?questions:fallback;
 if(n.id==='notes-big-picture')checks=[DATA.questions[0]];
 const bodies=[`<p class="teach-copy">${esc(t.context)}</p>`,`<div class="jargon-results">${t.terms.map(term=>`<article><h3>${esc(term)}</h3><p>${esc(JARGON[term]||VOCAB.find(v=>v.term===term)?.a||'See the glossary for this term.')}</p></article>`).join('')}</div>`,`<p class="teach-copy">${esc(t.analogy)}</p><p class="muted">This is a memory aid. The networking rule is:</p><p>${esc(t.context)}</p>`,`<p class="teach-copy">${esc(t.example)}</p>${n.id==='notes-4-2'?'<button data-open-decoder class="primary">Walk through the bits and calculations</button>':''}`,`<p>You’ve seen the idea, the vocabulary and an example. Now try ${checks.length} short question${checks.length===1?'':'s'}. You can reopen the rule, and missed questions return for another try.</p><button id="lesson-quiz" class="primary">Try it now</button>`];
 if(t.steps)bodies.splice(0,bodies.length,...t.steps.map(s=>readableText(s.body)),bodies[4]);
 $('#app').innerHTML=`<div class="study"><button data-nav="teach">← All lessons</button><p class="tag">Chapter ${n.ch} · ${esc(TEACH_CHAPTERS[n.ch])}</p><h1>${esc(t.title)}</h1><p>Step ${st.step+1} of ${labels.length} · ${labels[st.step]}</p><div class="bar"><span style="width:${100*(st.step+1)/labels.length}%"></span></div><section class="card teaching-card"><h2>${labels[st.step]}</h2>${bodies[st.step]}</section><div class="row spread actions"><button id="teach-prev" ${st.step===0?'disabled':''}>← Previous</button><button id="teach-next" class="primary" ${st.step===labels.length-1?'disabled':''}>Next step →</button></div><details class="teach-before"><summary>Full chapter notes and references</summary>${lessonBody(n)}</details></div>`;$('#teach-prev').onclick=()=>{st.step--;renderTeaching()};$('#teach-next').onclick=()=>{st.step++;renderTeaching();window.scrollTo(0,0)};if($('#lesson-quiz'))$('#lesson-quiz').onclick=()=>{start('taught',shuffle(checks));session.lessonId=n.id;renderModeBar()}}
