"""Explicit purpose statements accompany definitions, answers, and explanations."""
def add_purposes(D):
 by_term={}
 groups=[
 ('Data|Input|Output|Algorithm','Identify the information being processed and the procedure working on it. For example, a program reads a report as input and produces a result as output; knowing the actual task helps distinguish hiding contents from checking contents.'),
 ('Hash function|Digest|Hash comparison|SHA|SHA-256|Collision|Birthday attack','Compute or evaluate a summary of contents so it can be compared with a trusted reference. For a downloaded file, the purpose is to check whether its contents match the original; this does not hide the file or by itself prove who published it.'),
 ('Encryption|Ciphertext|Plaintext|Decryption|Symmetric cryptography|AES|DES|3DES|RC4|Blowfish|Twofish|IDEA|Stream cipher|Block cipher|One-time pad','Protect the confidentiality of information such as a saved report or a message. Encryption makes the contents unreadable without appropriate recovery; decryption lets an authorized recipient recover the readable contents.'),
 ('Cryptographic key|Public key|Private key|Key management|Key exchange|Diffie-Hellman|Hybrid encryption|RSA|ECC','Supply or establish the key material that controls a cryptographic operation. In file encryption, keys enable the intended transformation and recovery; in signing, the private/public roles support creation and verification of a signature. Protect secret keys so unauthorized people cannot use their capabilities.'),
 ('Digital signature|Non-repudiation','Let a recipient check that specific content was authorized by a trusted signing key and has not changed since signing. For example, verify a publisher’s signed software release. A signature does not itself hide the content or prove every claim in it is true.'),
 ('HMAC','Check message integrity and origin between parties that share a secret key. Unlike a plain digest, an attacker without that secret cannot simply make a valid authentication value for changed content under the scheme’s security assumptions.'),
 ('Checksum','Detect accidental corruption during transmission. The receiver compares its recalculated value with the transmitted value; an ordinary checksum is not protection against an attacker who can alter both data and checksum.'),
 ('Confidentiality','Keep private information, such as medical records or a report, from being read by people who lack permission.'),
 ('Integrity','Protect information from unauthorized changes, such as someone changing a grade or payment amount.'),
 ('Availability','Keep information and services usable by authorized people when they need them, such as a working registration website.'),
 ('Authentication','Check a claimed identity or message origin before relying on it. For example, verify an account login rather than trusting a displayed name.'),
 ('Authorization|Permission|Least privilege|Limiting','Restrict what a user or program may do. For example, let an employee read necessary records without giving permission to alter every system setting.'),
 ('MFA','Make account access depend on distinct types of authentication evidence, reducing reliance on a stolen password alone. Phishing-resistant methods further reduce common deceptive-site risks.'),
 ('Firewall|ACL|Packet-filtering firewall|Stateful firewall|Circuit gateway|Application gateway','Permit necessary communication and restrict unwanted connections according to policy. Choose inspection and rules that fit the traffic and application being controlled.'),
 ('Proxy server','Handle requests on behalf of a client and enforce application policies, such as blocking known malicious websites or recording web requests.'),
 ('IDS','Detect suspicious activity and notify defenders so they can investigate. An alert alone does not necessarily stop the activity.'),
 ('IPS|HIPS','Detect and actively block or interrupt suspicious activity at the relevant network or host boundary, while avoiding unnecessary disruption of legitimate work.'),
 ('EDR','Collect endpoint evidence and support investigation and response, such as linking suspicious process activity to connections and isolating an affected device.'),
 ('SOC','Organize the people and operational work that monitor alerts, investigate incidents, and coordinate a response.'),
 ('PCAP|Full packet capture','Preserve observed packet bytes for detailed investigation, such as examining headers and captured content. Recording encrypted bytes does not automatically reveal their readable contents.'),
 ('Flow record','Summarize which endpoints communicated, when, and how much data moved, without normally storing all message contents.'),
 ('Application allowlisting','Prevent unapproved software from running by permitting approved applications. This directly controls execution rather than merely recording network traffic.'),
 ('Endpoint|Host and guest|Operating system|Application|Process','Identify where information is stored or processed and where actions actually execute, so the appropriate permissions, monitoring, and recovery controls can be applied.'),
 ('Log|Telemetry|Correlation|Visibility|Attack chain|Log retention','Provide and connect evidence about what happened, where, and when. For example, relate a suspicious login to a program launch and an outbound connection rather than relying on one isolated alert.'),
 ('Signature detection|Anomaly detection|Baseline|Detection tuning|False positive|False negative','Distinguish genuine attacks from legitimate activity and improve detection decisions. The practical aim is to catch harmful activity without wasting investigation time or blocking ordinary business unnecessarily.'),
 ('Asset|Threat|Threat actor|Vulnerability|Risk|Attack vector|Attack surface|Business impact','Describe what has value, what could go wrong, how it could happen, and how serious it would be, so the organization can choose appropriate protections.'),
 ('Mitigate|Risk mitigation','Reduce the likelihood or impact of harm. For example, installing a patch reduces exposure to the repaired weakness; it does not guarantee that all risk disappears.'),
 ('Risk acceptance|Risk avoidance|Risk transfer','Choose how the business handles an understood risk: knowingly retain it, stop the risky activity, or shift some consequences through arrangements such as insurance.'),
 ('OS hardening|Patch|Antivirus|Service','Reduce exposure or detect harmful code on a computer so staff can use required functions with fewer unnecessary weaknesses and privileges.'),
 ('Phishing|Spear phishing|Smishing|Vishing|Social engineering|419 scam','The attacker’s purpose is to manipulate a person into revealing information, sending money, or performing a harmful action. Recognizing the channel and request helps the recipient verify independently instead of complying.'),
 ('Caller-ID spoofing|VoIP','In the vishing scenario, understand how a call can appear to come from a trusted organization. Voice calling is a legitimate capability; caller-ID spoofing misuses displayed identity to support deception.'),
 ('SET|Credential harvester','In an authorized test, demonstrate how a deceptive login form collects submitted credentials. In an attack, the same mechanism can expose account access without requiring an operating-system exploit.'),
 ('Metasploit|WebGoat|Sandbox','Provide a controlled way to study vulnerabilities or suspicious behavior and assess defenses. The practical goal is to understand the weakness and its impact in an authorized environment.'),
 ('Keylogger|Spyware','The malicious use is to covertly collect information, such as typed passwords or user activity. Recognizing where capture occurs explains why transport encryption alone cannot secure an already compromised device.'),
 ('Virus|Program virus|Macro virus|Worm|Trojan|Malware','Identify how malicious code reaches, runs on, or spreads between systems so defenses address the actual entry, execution, and propagation mechanism.'),
 ('Armored virus|Polymorphic virus|Metamorphic virus|Oligomorphic virus|Swiss cheese infection|Split infection|Process hollowing','The attacker uses concealment or code variation to make malicious activity harder to detect or examine. Recognizing the technique helps explain the limits of simple pattern matching.'),
 ('Backdoor|Reverse shell|TCP reverse shell|C2|C2 server|Bot','The malicious purpose is to maintain access or direct actions on a compromised computer. For example, an infected workstation receives remote instructions or provides a command interface.'),
 ('Credential dumping|Privilege escalation|Infiltration|Exfiltration','Recognize a specific step in unauthorized access: extracting stored credentials, gaining more rights, entering a system, or moving information out. Each step suggests different evidence and containment actions.'),
 ('DoS|DDoS|SYN flood|Slowloris|Resource exhaustion','The attacker’s purpose is to make a service unavailable to legitimate users by consuming or disrupting limited resources. Defenses must address the resource actually being exhausted.'),
 ('SQL|SQLi|Parameterized query','Keep database requests performing their intended task. Parameterized queries separate user values from command structure so input cannot simply become unintended SQL instructions.'),
 ('XSS|Output encoding|JavaScript|HTML','Distinguish intended page behavior from attacker-controlled content being interpreted as browser instructions. Safe output handling prevents data from becoming executable content in its output context.'),
 ('Buffer overflow','Recognize writes beyond allocated memory that can corrupt a program or enable execution. Bounds checking, safe programming, patching, and mitigations address that memory boundary.'),
 ('Reputation label|Manual analysis|Automated analysis|Static analysis|Dynamic analysis|JSUnpack|Firebug|McAfee Advisor|Norton SafeWeb','Gather and interpret evidence about a file or website: inspect contents, observe behavior, or examine earlier ratings. The purpose is to judge the evidence rather than assuming a familiar label guarantees safety.'),
 ('Data packet|Header|Payload / body|Bit|Byte|Port|IP address|Network|Protocol|Routing|TCP|UDP|IP|Byte stream|Datagram|Best-effort delivery|Reliable delivery|TCP handshake','Explain how computers organize and deliver information. Knowing the layer and its guarantees helps distinguish addressing, forwarding, ordering, error recovery, and application behavior.'),
 ('DNS|DNSSEC','Find network name records and, for DNSSEC, validate signed DNS data. DNSSEC adds authenticity and integrity checks; it does not encrypt ordinary name queries.'),
 ('SNMP|ICMP|NTP|NTS','Support network operation through device management, diagnostics, or clock synchronization, with protection appropriate to the selected protocol and configuration.'),
 ('FTP|FTPS|SFTP|SSH|HTTP|HTTPS|TLS|S/MIME|SRTP','Provide the required application communication and, where configured, its protection. For example, HTTPS uses TLS to protect browser-to-server traffic; file transfer and email use different mechanisms.'),
 ('Blockchain|Block|Ledger|Transaction|Bitcoin|Consensus|Validation|Double-spending problem|Unspent output','Maintain and check a shared history of transfers so spending is authorized and conflicting spends are not both accepted. Signatures, validation, and agreement on history solve different parts of that task.'),
 ('Nonce|Proof of work|Miner|Block header|Confirmation|Block subsidy|Transaction fee','Support and incentivize block production and evaluate accumulated valid work. These mechanisms help establish accepted history; they do not let miners spend other users’ funds.'),
 ('Merkle root|Merkle proof|Previous-block hash|Tamper evidence','Summarize included records or link earlier history so changes can be detected and inclusion can be checked. Hash commitments do not prove that every real-world claim in a record is true.'),
 ('Hard fork|Soft fork','Understand how participants change consensus rules and whether different versions can continue accepting the same history.'),
 ('TPM|HSM|Full-disk encryption|Self-encrypting drive','Protect specified stored data, cryptographic keys, or key operations at the relevant hardware or storage boundary. This does not automatically prevent all attacks on an unlocked running application.'),
 ('VM|Hypervisor|Type I hypervisor|Type II hypervisor|Container|VDI|Snapshot|NAT|VM sprawl','Provide or manage isolated computing environments and controlled connectivity. In the lab, the aim is reproducible testing without treating deliberately weakened guests as production recommendations.'),
 ('Cloud computing|SaaS|PaaS|IaaS|Shared responsibility|Public cloud|Private cloud|Hybrid cloud|Community cloud|CASB','Understand which computing service is provided and who must secure each part. Hosted services do not remove the customer’s duties for access, information, and configuration.'),
 ]
 for names,purpose in groups:
  for name in names.split('|'):by_term[name.casefold()]=purpose
 for pool in ['questions','checks','vocab','foundations','orientation','topicOrientation','trueFalse','cloze','sorts','discussions']:
  for x in D[pool]:
   term=x.get('term','').casefold()
   setting=x.get('setting') or D['topicContexts'][str(x.get('number',x.get('source')))]
   x['purpose']=by_term.get(term,setting['purpose']+' '+setting['action'])
   # The initial file-hashing questions predate named term cards.
   if x['id'] in ['425-context-'+str(i) for i in range(21,28)] or x['id'] in ['425-introduction-hash','425-introduction-digest']:
    x['purpose']=by_term['digest']
   elif x['id'] in ['425-introduction-encryption','425-introduction-decryption']:
    x['purpose']=by_term['encryption']
   elif x['id']=='425-introduction-key':x['purpose']='Control how software transforms a report’s contents during encryption and enables appropriate recovery. Keeping a secret encryption key protected helps prevent someone without permission from reading the protected contents.'
