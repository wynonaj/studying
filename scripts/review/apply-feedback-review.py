import json
from pathlib import Path
p=Path('dist/content.json');d=json.loads(p.read_text())
feedback={}
for line in Path('scripts/review/vocabulary-feedback.txt').read_text().splitlines():
 term,why,hint=line.split('|');feedback[term]={'why':why,'hint':'Remember: '+hint}
assert set(feedback)==set(d['vocabExplanations']),set(d['vocabExplanations'])-set(feedback)
d['vocabFeedback']=feedback
d['vocabExplanations']={k:v['why'] for k,v in feedback.items()}
# Question-specific reasoning for the original added-notes bank.
notes={
0:('The browser still makes the same application-level request. Ethernet and Wi-Fi provide different local delivery methods underneath it, so the browser does not need a new web protocol when the link changes.','Separate the message a program wants to send from the local technology carrying it.'),
1:(feedback['Transport layer']['why'],'An IP address helps reach the device; a port helps reach the program on that device.'),
2:(feedback['Presentation layer']['why'],'Representation means the format of information. Session means managing the conversation.'),
3:('A link-layer wrapper only serves the current local delivery. At a router, that delivery ends; the router processes the IP packet and creates the appropriate frame for the outgoing link.','The packet can continue toward the same final IP destination while its next local MAC destination changes.'),
4:(feedback['IEEE']['why'],feedback['IEEE']['hint']),
5:('The naming system needs coordinated top-level rules and unique identifiers so the same domain name is not delegated inconsistently. ICANN coordinates that global system; ordinary DNS servers answer day-to-day lookups.','Coordinating the naming system is different from personally answering every DNS request.'),
6:('Shared Internet identifiers need coordinated registries. IANA maintains protocol-parameter registries and coordinates global number resources, including allocations to regional registries.','A registry is an organized record of assigned identifiers; it prevents incompatible assignments.'),
7:('Building wiring must be installed and organized consistently so links can be tested and maintained. TIA cabling standards address that infrastructure rather than Internet packet-routing rules.','Match the organization to its job: building cabling points to TIA.'),
8:('ITU is a United Nations specialized agency for information and communication technologies; its standardization work helps telecommunications systems operate consistently internationally.','The United Nations agency clue distinguishes ITU from IEEE and IETF.'),
9:(feedback['Physical layer']['why'],'The receiver can measure voltage or light; it cannot directly measure the abstract idea of a 0.'),
10:('Twisting changes how each conductor is exposed to nearby interference along the cable, helping reduce unwanted coupling and noise in the received differential signal. It does not make copper completely immune to interference.','The twists help the receiver distinguish the intended signal from unwanted electrical effects.'),
11:('In this traditional cabling comparison, broadband divides the available frequency range into separate channels. Different channels can carry signals simultaneously rather than all users taking turns in one channel.','Here broadband refers to frequency-channel sharing, not just the everyday phrase fast Internet.'),
12:(feedback['Multimode fiber']['why'],'A larger core allows multiple modes, whose different arrival times can spread a pulse.'),
13:(feedback['QAM']['why'],'Amplitude is strength; phase is position relative to a reference wave. QAM varies both.'),
14:('Shannon’s B is the width of the available frequency band, measured in hertz. Multiplying it by log₂(1 + S/N) produces the theoretical capacity C in bits per second.','B is the frequency space available; C is the resulting theoretical data-rate limit. They have different units.'),
15:('With B fixed, increasing S/N increases 1 + S/N and therefore its logarithm. The theoretical capacity C rises because a cleaner signal allows information states to be distinguished more reliably.','Keep bandwidth fixed and improve signal relative to noise: the theoretical limit goes up, not necessarily the actual application speed.'),
16:(feedback['Frame']['why'],'The local wrapper is a frame; the IP wrapper inside it is a packet.'),
17:('CSMA/CD solves simultaneous transmissions on a shared half-duplex Ethernet medium. A switched full-duplex link has separate simultaneous send/receive operation, so this collision procedure is unnecessary.','Look for shared and half-duplex before choosing collision detection.'),
18:('The receiver recomputes the CRC and compares it with the received FCS. A match means that check detected no corruption; some error patterns can go undetected, so it is not proof that every bit is correct.','An error detector can fail to detect an error. Passing is not the same as repairing or guaranteeing.'),
19:('Read the eight positions as 128, 64, 32, 16, 8, 4, 2, 1. In 10101101 the 1s select 128, 32, 8, 4 and 1. Add in steps: 128 + 32 = 160; +8 = 168; +4 = 172; +1 = 173.','A 1 includes its place value; a 0 skips it. Do not count the number of 1s.'),
20:('Without a destination entry, the switch cannot choose one correct output port. It floods eligible ports in that VLAN except the incoming port, so the destination has a chance to receive the frame.','The frame is still addressed to one recipient. Flooding an unknown unicast does not turn it into a broadcast address.'),
21:('MAC identifies the next local frame delivery; IP gives routers a destination across networks. Routers can replace local frames along the path without requiring the application to choose every link address.','IP is the routed destination; MAC is the local delivery label.'),
22:('IPv4 has 32 bit positions. /17 reserves the first 17 for the network. Subtract 32 − 17 = 15 remaining host bits. Counting address combinations would be the next step, 2¹⁵.','The question asks for bits, not addresses. Stop after subtraction.'),
23:(feedback['Zero compression']['why'],'Count the written groups; the one missing stretch fills the count back up to eight.'),
24:('Traceroute depends on routers replying to probes. A router may filter or limit those replies while continuing to forward normal traffic, so a missing reply alone cannot prove a broken path.','Silence in a diagnostic test is evidence to investigate, not a guaranteed outage.'),
25:(feedback['Physical design']['why'],'Choosing a cable or placing a switch is physical design; assigning subnet ranges is logical design.'),
26:('The service connection crosses a responsibility boundary between provider and customer. Identifying that point helps determine which side must investigate or repair a problem.','Demarcation is a boundary of responsibility, not automatically a firewall or a router.'),
27:('An MDF is the main distribution location. IDFs serve additional areas and link back through backbone cabling, reducing the need to run every work-area cable to one faraway room.','Main location → backbone → intermediate location → nearby work areas.'),
28:(feedback['Spine-leaf']['why'],feedback['Spine-leaf']['hint']),
29:('A GET request names a managed object whose value the manager wants to read. The device agent returns the result if supported and permitted; GET does not request a configuration change.','GET reads; SET requests a change; a trap reports an event.'),
30:('A SET request asks the agent to assign a value to a writable managed object. The agent checks support, permissions and validity before accepting it, so not every value can be changed.','Being able to read a gauge does not imply permission to change its setting.'),
31:('IETF working groups use rough consensus: participants discuss technical issues and address substantial objections. It is not simply a majority vote or an instruction from one vendor.','These are people reviewing technical proposals. The goal is broad technical agreement, not counting devices or votes.')}
for q in d['notesQuestions']:
 if q['id'].startswith('notes-quiz-'):
  why,hint=notes[int(q['id'].split('-')[-1])];q['explain']=why;q['remember']=hint if hint.startswith('Remember:') else 'Remember: '+hint
# Specific corrections/improvements in original and applied banks.
updates={
'q227':('A public IP address is an Internet-facing address that must be uniquely assigned for routing to work reliably. Allocation means assigning a block of addresses to an organization. RIRs coordinate these assignments within regions as part of the global registry system.','Imagine two unrelated towns receiving the same complete mailing addresses: deliveries become ambiguous. Registries coordinate assignments to avoid that conflict.'),
'u227':('Allocations are assigned blocks of IP addresses. Regional registries coordinate and record these assignments so unrelated public networks are not given conflicting address space. They administer resources rather than forwarding packets.','A registry is an organized record, and allocation means assigning resources. Public addresses need global coordination.'),
'q251':(feedback['Core layer']['why'],feedback['Core layer']['hint']),
'u251':(feedback['Core layer']['why'],feedback['Core layer']['hint']),
'q259':(feedback['Distribution layer']['why']+' The placement of firewalls and authentication services depends on the particular design.',feedback['Distribution layer']['hint']),
'u259':(feedback['Distribution layer']['why'],feedback['Distribution layer']['hint']),
'q260':(feedback['Access layer']['why'],feedback['Access layer']['hint']),
'u260':(feedback['Access layer']['why'],feedback['Access layer']['hint']),
'q266':(feedback['MIB']['why'],feedback['MIB']['hint']),
'u266':(feedback['MIB']['why'],feedback['MIB']['hint']),
'u246':(feedback['Data center topology']['why'],feedback['Spine-leaf']['hint']),
'u180':('A local MAC address does not tell routers which remote network to use. IP prefixes support routing across networks, while each link can use its own local delivery addresses.','A local delivery label and the final routed destination solve different parts of the trip.'),
'u185':('In 192.168.5.10/24 and 192.168.5.20/24, the first 24 bits name the same subnet. The last eight bits differ, selecting different interface addresses within that subnet.','The shared part names the neighborhood; the changing part distinguishes its addresses.'),
'q190':('First find the host-bit count: IPv4 has 32 bits, so 32 − 17 = 15. Each host bit has two choices, giving 2¹⁵ = 32,768 total addresses. For this ordinary subnet, reserve one network address and one broadcast address: 32,768 − 2 = 32,766 usable host addresses.','Bits are positions; addresses are combinations. Subtract to count bits, raise 2 to that count for all addresses, then subtract 2 only when asked for usable hosts.'),
'u190':('For /20, first subtract: 32 − 20 = 12 host bits. Then count combinations: 2¹² = 4,096 total addresses. Only a usable-host question would subtract the two reserved addresses and give 4,094.','Total includes every address. Usable excludes network and broadcast in an ordinary IPv4 subnet.')}
# Applied questions with previously definition-only feedback get the mechanism behind it.
for ident,term in {
'u2':'Layering','u25':'OSI','u29':'Presentation layer','u44':'Physical layer',
'u47':'Physical medium','u60':'Fiber-optic cable','u73':'Total internal reflection',
'u77':'Single-mode fiber','u96':'QAM','u111':'Frame','u118':'NIC','u122':'Broadcast',
'u125':'CSMA/CD','u136':'FCS','u144':'OUI','u161':'Switch','u166':'STP',
'u177':'Routing table','u208':'Classful addressing','u222':'Traceroute',
'u233':'Requirements analysis','u235':'Logical design','u239':'Physical design',
'u241':'Building network','u249':'Campus network','u261':'Enterprise network',
'u263':'Network maintenance','u264':'SNMP','u267':'Standard','u268':'Working group'
}.items():
 updates[ident]=(feedback[term]['why'],feedback[term]['hint'])
for bank in ['questions','understanding']:
 for q in d[bank]:
  if q['id'] in updates:
   why,hint=updates[q['id']];q['explain']=why;q['remember']=hint if hint.startswith('Remember:') else 'Remember: '+hint
# Use a question's own reasoning, never a source question's unrelated numeric example.
for q in d['understanding']:
 q.setdefault('remember','')
# Keep detailed worked conversion solutions, with a separate short method cue.
for q in d['notesQuestions']:
 if q['id'].startswith('teach-convert-'):
  key=q['lessonId'].replace('teach-convert-','')
  hints={'binary-decimal':'Line up the place values. Add a value only where the bit is 1.','decimal-binary':'Work from largest value to smallest. If it fits, write 1 and subtract; otherwise write 0.','hex-binary':'Convert each hex digit into exactly four bits and join in the original order.','binary-hex':'Group bits into fours from the right; convert each group using 8, 4, 2, 1.','hex-decimal':'Multiply each digit by its position value, then add. The rightmost positions are 1 and 16.','decimal-hex':'For a byte, find full groups of 16 and the leftover. Translate 10–15 into A–F.'}
  q['remember']='Remember: '+hints[key]
  q['explain']=q['explain'].removeprefix('Remember: ')
d['feedbackSources']=[
 {'title':'IEEE: Ethernet and wireless LAN standards','url':'https://standards.ieee.org/featured/ieee-802/'},
 {'title':'IANA: number resources and regional registries','url':'https://www.iana.org/numbers'},
 {'title':'IETF: working groups and rough consensus','url':'https://www.ietf.org/process/wgs/'},
 {'title':'RFC 3416: SNMP requests and managed objects','url':'https://www.rfc-editor.org/rfc/rfc3416'},
 {'title':'RFC 4291: IPv6 representation','url':'https://www.rfc-editor.org/rfc/rfc4291'},
 {'title':'RFC 3021: /31 point-to-point exception','url':'https://www.rfc-editor.org/rfc/rfc3021'},
 {'title':'Cisco: spine–leaf connections','url':'https://www.cisco.com/c/en/us/td/docs/dcn/whitepapers/cisco-application-centric-infrastructure-design-guide.html'}]
d['clozeFeedback']=json.loads(Path('scripts/review/cloze-feedback.json').read_text())
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
