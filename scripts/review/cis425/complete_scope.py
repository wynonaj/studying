"""Explicit term and application coverage for the requested final topic checklist."""

def complete_scope(D):
 Q=D['questions']
 additions={
  25:'The castle analogy illustrates defense in depth: a gate, walls, guards, and internal locks protect different boundaries. In a business, filtering, MFA, least privilege, application allowlisting, EDR, monitoring, and recovery provide complementary layers. If a phishing message passes the filter, other layers can still restrict execution, account access, lateral movement, and damage.',
  29:'A buffer overflow occurs when a program writes beyond a buffer’s allocated boundary. It can corrupt adjacent memory, crash the program, or enable code execution. Prevent it through bounds checking, memory-safe programming, and patching; DEP/NX, ASLR, and stack protections add mitigation. SQL injection instead changes a database command through unsafe input; XSS executes injected content in a victim browser. These are different interpreters and require different defenses.',
  32:'Phishing is an important delivery route in the lab context: a deceptive attachment or download may install a software keylogger. Other routes include compromised software, exploitation, and physical installation of hardware. A cloned login page captures submitted credentials directly and does not require a keylogger. Physical access controls address hardware capture; endpoint controls address malicious software.',
  33:'Use a standard non-administrator account for routine work and elevate only for approved tasks. Maintain an asset inventory, remove unnecessary software, disable unneeded services, restrict exposed ports, configure host firewalls, keep antivirus/EDR current, and enable appropriate automatic updates. Test and stage changes where needed, verify installation, and monitor failures. An antivirus detects known or suspicious malicious content; EDR adds investigation telemetry and response capabilities.',
  34:'For a business explanation, connect the sequence to impact: initial access may expose accounts; privilege escalation expands access; credential dumping can enable impersonation; process hollowing can conceal execution; C2 carries remote instructions; exfiltration removes data. Correlate identity, process, file, and network evidence. The SOC investigates and coordinates containment; EDR can expose process ancestry and support endpoint isolation. A penetration test demonstrates a weakness and its potential consequences; it does not by itself prove a real breach occurred.',
  42:'A network packet is a unit of data handled at the network layer, not the smallest possible unit of transmission. Its header contains addressing and control fields; its payload (body) carries the data, including higher-layer headers. Bits, link-layer frames, IP packets, and TCP segments name different units. A TCP reverse shell uses TCP for the outbound shell connection; TCP reliability does not make that connection trustworthy.',
  31:'MFA combines distinct factor categories: something you know, have, or are. A password plus another password is not MFA. MFA is a major defense against stolen passwords; phishing-resistant methods such as FIDO/WebAuthn resist deceptive-site authentication. Account monitoring, session revocation, least privilege, and endpoint security remain necessary alongside MFA.',
 }
 for n,extra in additions.items():
  Q[n-1]['answer']+=' '+extra
  for x in D['checks']:
   if x.get('source')==n and x['id'].startswith('425-check-'):
    x['answer']=Q[n-1]['answer']
 terms=[
 ('Checksum',15,'An error-detection value recalculated by a receiver and compared with the transmitted value to detect corruption; an ordinary checksum does not authenticate a sender.','A secret signing key|Encryption that hides packet content|Proof against deliberate attacker recomputation'),
 ('False positive',12,'An alert that incorrectly labels benign activity as malicious or suspicious.','A missed real attack|A correctly blocked attack|A successful key exchange'),
 ('Authentication',18,'Checking a claimed identity or message origin using appropriate evidence and trusted mechanisms.','Hiding every message automatically|Granting every verified user administrator rights|Only making code hard to read'),
 ('Obfuscation',18,'Making information or code harder to understand; it does not by itself establish strong confidentiality or authenticity.','Proof of who sent a message|An automatic replacement for encryption|A network routing guarantee'),
 ('Firewall',26,'A control that permits or blocks network traffic according to configured policy and inspection capabilities.','A guarantee all permitted traffic is harmless|A keylogger|Only a passive log archive'),
 ('Antivirus',33,'Software that detects, blocks, or removes malicious code using signatures and other analysis techniques.','A guarantee every threat is detected|A replacement for patching|A protocol for Bitcoin consensus'),
 ('Bot',13,'A remotely controlled program on a compromised system that can receive instructions through command and control.','Every dormant routine regardless of purpose|A public signature verification key|A packet error check'),
 ('Adware',17,'Software characterized by unwanted advertising and sometimes associated tracking or browser redirection.','Always a self-spreading network worm|Only hardware that records keystrokes|A legitimate transaction signature'),
 ('Plaintext',1,'Readable, unencrypted data before encryption or after decryption.','The encrypted output|A public-key fingerprint only|A packet error counter'),
 ('Ciphertext',1,'The encrypted representation of plaintext, recovered using the appropriate decryption method and key.','A readable original message|A reversible SHA-256 digest|A firewall rule'),
 ('Encryption',1,'Transforming plaintext into ciphertext using a cryptographic algorithm and key.','Computing an ordinary packet checksum|Deleting all copies of a file|Proving every claim is true'),
 ('Decryption',1,'Recovering plaintext from ciphertext using the appropriate algorithm and key.','Reversing every cryptographic hash|Generating a firewall alert|Changing a network port'),
 ('Data packet',42,'A network-layer unit containing a header and payload; the payload can include higher-layer headers and application data.','The smallest possible physical transmission unit|Only a readable application message|An entire Internet connection'),
 ('Header',42,'Control information preceding carried data, such as IP addressing or TCP sequence fields at the relevant layer.','Always the complete application file|A secret private key|The same thing as every payload'),
 ('Payload / body',42,'The content carried by a protocol unit; at a lower layer it can include another layer’s header and data.','Always malware|Only the destination address|A guarantee of encrypted content'),
 ('Symmetric cryptography',38,'Encryption and decryption use a shared secret key; secure distribution and protection of that key are essential.','Everyone publishes the decryption key|A hash with a reverse operation|Only a signature verification method'),
 ('Asymmetric cryptography',38,'Cryptography using a related public/private key pair, with different operations for encryption or signatures.','Encryption with the same shared secret only|A method without any keys|A checksum that identifies every sender'),
 ('Public key',38,'The shareable member of a key pair, used for signature verification or encryption to its owner as the scheme permits.','The secret signing key everyone must share|An ordinary password|A private key copied into a URL'),
 ('Private key',38,'The secret member of a key pair, used for signing or decryption as the scheme permits; keep it protected.','A public directory of all users|A packet checksum|The recipient’s freely shared verification key'),
 ('Non-repudiation',61,'Evidence supporting attribution of a signed action, relying on trusted identity binding and protected signing keys.','Automatic secrecy of every signed message|Proof that signed content is true|A guarantee a key can never be stolen'),
 ('SHA-256',19,'A cryptographic hash producing a 256-bit digest, displayed as 64 hexadecimal characters.','A reversible encryption cipher|A 256-character password generator|The secret key for all Bitcoin users'),
 ('Hard fork',14,'An incompatible consensus-rule change that can split a blockchain when participants continue following different rules.','A temporary collision between network cables|A guaranteed permanent split after every update|A method for decrypting a hash'),
 ('Soft fork',76,'A consensus-rule tightening whose accepted blocks remain valid under the older rules; older nodes do not enforce every new restriction.','An incompatible expansion of accepted blocks|A private-key backup|A replacement for transaction signatures'),
 ('Phishing',9,'Deceptive messages or sites that impersonate a trusted source to obtain information or induce harmful actions.','Every unsolicited advertisement|A cryptographic signature|Only attacks conducted by phone'),
 ('Metasploit',31,'A modular penetration-testing framework for validating vulnerabilities and demonstrating their potential impact in authorized tests.','A cryptographic digest|Another name for every SET feature|A guarantee a real breach occurred'),
 ('Credential harvester',31,'A mechanism that collects submitted login information, often through a deceptive form or cloned login page.','A tool that always decrypts TLS|A synonym for patch management|A hardware firewall'),
 ('C2 server',13,'A command-and-control system that sends instructions to compromised programs and receives their communications.','A server that automatically patches all clients|A public checksum directory|A required component of every macro virus'),
 ('TCP reverse shell',4,'A command interface whose TCP connection is initiated from the compromised host toward a controller.','An inbound-only connection from an attacker|A secure channel merely because it uses TCP|A guarantee every proxy is bypassed'),
 ('DoS',28,'Denial of service: exhausting or disrupting resources so legitimate users cannot obtain a service.','Only stealing passwords|Only changing grades|A form of digital signature'),
 ('Buffer overflow',29,'Writing beyond an allocated memory buffer, potentially corrupting memory, crashing a program, or enabling execution.','Changing a SQL query through unsafe input|Executing script in a browser by definition|An ordinary retransmitted TCP segment'),
 ('OS hardening',33,'Reducing an operating system’s attack surface through secure configuration, updates, restricted privileges, and protective controls.','Disabling every production firewall|Giving all users administrator access|Installing every optional service'),
 ('Least privilege',33,'Giving an account or process only the permissions needed for its legitimate task.','Giving every employee local administrator rights|Removing all audit logs|Trusting all internal traffic'),
 ('ACL',66,'An access control list specifying which identities or traffic are permitted or denied under defined rules.','An automatic proof a site is safe|An encryption algorithm|A packet payload capture'),
 ('Proxy server',66,'An intermediary that handles client requests and can enforce destination, category, authentication, and application policies.','A guarantee every malicious site is blocked|Only a passive packet recording|A tool that approves every executable'),
 ('Defense in depth',25,'Using complementary security layers so a failure of one control does not leave the organization wholly exposed.','Depending on one secret product|Adding identical alerts without response|Removing internal access controls'),
 ('Attack chain',34,'A connected sequence of attacker activity, from entry and execution through access expansion and possible data theft or disruption.','Proof every alert is an actual breach|A blockchain mining rule|A list of unrelated tools without timing'),
 ]
 existing={x['term'].casefold() for x in D['vocab']}
 for term,n,meaning,wrong in terms:
  if term.casefold() in existing:continue
  q=Q[n-1]
  D['vocab'].append(dict(id=f'425-scope-term-{n}-{len(D["vocab"])}',source=n,section=q['section'],term=term,exp='',q=f'What is {term}?',correct=meaning,answer=meaning,teach=meaning+' '+q['teach'],example=q['example'],distractors=wrong.split('|')))
 cases=[
 (42,'An IP packet contains a TCP header and application data. Which part of the IP packet carries them?','The IP payload','Only the IP source address|Only the link preamble|The private signing key','Encapsulation places higher-layer headers and data inside the lower layer’s payload.'),
 (32,'A fake login page captures a typed password. Must a keylogger have been installed?','No; the form itself can send the submitted credentials to the attacker','Yes; every phishing page installs keyboard hardware|Yes; HTTPS only works with keyloggers|No; passwords cannot be captured','Credential harvesting and keystroke logging are different capture mechanisms.'),
 (29,'A program writes past the end of a memory array and corrupts adjacent memory. What is the flaw?','Buffer overflow','SQL injection by definition|Cross-site scripting by definition|A collision in SHA-256','A memory boundary is exceeded; SQLi and XSS involve different interpreters.'),
 (66,'A company wants to block employee access to known malicious website categories. Which course device fits best?','A filtering proxy or secure web gateway','A passive IDS with no enforcement|A keyboard logger|A plain packet checksum','The intermediary can enforce URL, destination, and category policies.'),
 (66,'Which control most directly prevents an unapproved executable from running?','Application allowlisting','A passive network IDS alone|A larger Internet connection|A digital signature typed into email','Execution policy belongs to application control; observing network traffic is not the same operation.'),
 (25,'A phishing email passes filtering. Why can defense in depth still reduce damage?','Other layers can restrict authentication, execution, privileges, and outbound activity','All layers automatically fail together|A castle analogy replaces endpoint controls|Only a stronger password matters','Layers protect different boundaries and actions rather than relying on one perfect filter.'),
 (31,'A user enters a password and then a second password. Is that MFA?','No; both are the same knowledge-factor category','Yes; two prompts always mean two factors|Yes; any longer password is MFA|No; MFA requires exactly three factors','MFA requires distinct factor categories, such as knowledge and possession.'),
 (34,'Why does a SOC need a timeline linking identity, endpoint, and network evidence?','To connect activity, assess scope and impact, and choose containment actions','To assume every alert proves complete theft|To avoid investigating host processes|To replace all preventive controls','A connected sequence supports better decisions than an isolated alert.'),
 (33,'Why use a non-admin account for everyday work?','To limit what ordinary activity or a compromised process can change','To make phishing messages impossible|To remove the need for patching|To guarantee all files are encrypted','Least privilege reduces authority and potential impact; it complements other controls.'),
 (20,'Does hashing alone make a blockchain impossible to alter?','No; hash links reveal changes, while validation and consensus protect the accepted history','Yes; any SHA-256 hash permanently freezes all computers|Yes; signatures are unnecessary|No; blocks contain no hashes','Tamper evidence and agreement on history are separate but complementary mechanisms.'),
 (61,'A valid digital signature is attached to a readable document. What does it provide?','Origin/integrity evidence under the trusted key, without automatically hiding the document','Automatic secrecy of the document|Proof every statement is true|Proof the private key was never compromised','Signatures and encryption protect different goals; attribution depends on key custody and trust.'),
 (34,'A test reverse shell reaches an outside controller from an employee workstation. What business risk does it demonstrate?','Remote command access could enable disruption, further access, or data theft within the process’s permissions','That every customer record has already been stolen|That TCP itself supplies authorization|That the host needs no recovery assessment','Connect the demonstrated capability to potential consequences without inventing evidence of actual losses.'),
 ]
 for i,(n,prompt,right,wrong,why) in enumerate(cases,1):
  q=Q[n-1]
  D['checks'].append(dict(id=f'425-scope-check-{i}',source=n,section=q['section'],q=prompt,correct=right,distractors=wrong.split('|'),answer=why,teach=why,example=q['example'],format='mc'))
 D['coverage'].append(dict(id='requested-core',title='Core topic checklist',basis='Definitions, explanations, and application practice for every topic in the requested review list',topics=[
 ['Exam format; Chapters 1 and 3; Lectures 1–8; Labs 0–2',[16,17,18,19,20,21,31,32,35]],
 ['Plaintext, ciphertext, checksums, packets, headers and payloads',[1,15,42,77]],
 ['Symmetric/asymmetric keys, signatures, authenticity and non-repudiation',[18,38,59,60,61]],
 ['SHA-256, hash links, blockchain, Bitcoin, hard and soft forks',[14,19,20,21,75,76]],
 ['Keyloggers, phishing, Metasploit, SET and credential harvesting',[9,31,32]],
 ['C2, credential dumping, process hollowing, privilege escalation, EDR and SOC',[13,34,82]],
 ['TCP reverse shells, DoS/DDoS, SQLi, buffer overflow and XSS',[4,28,29]],
 ['Hardening, patches, standard accounts, services/ports, updates and host protection',[16,33,71,72]],
 ['Firewalls, ACLs, proxy filtering, IDS/IPS and application allowlisting',[26,27,66,78]],
 ['Castle analogy, layered controls, MFA and least privilege',[24,25,31,33]],
 ['Business impact, attack-chain visibility and discussion answers',[16,17,18,19,20,21,31,34]],
 ]))
 D['references'] += [dict(title=t,url=u,questions=[]) for t,u in [
 ('Rapid7 · Metasploit Framework','https://help.rapid7.com/metasploit/Content/getting-started/about-msf.html'),
 ('MITRE ATT&CK · Process hollowing','https://attack.mitre.org/techniques/T1055/012/')]]
 D['counts']={k:len(D[k]) for k in ['questions','checks','vocab','cloze','sorts','trueFalse','sources']}
