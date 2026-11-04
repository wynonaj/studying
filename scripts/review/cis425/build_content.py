"""Build the CIS 425 lecture-based learning and practice bank."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'dist' / 'cis425-content.json'

sections = [
    {'id': i, 'title': title, 'reading': f'Lecture {i}', 'intro': intro}
    for i, title, intro in [
        (1, 'Why defensive cybersecurity matters', 'Understand attacker motives, virtualization, and the goal of defending real systems.'),
        (2, 'Secure network architecture', 'Connect security principles to the devices that monitor, allow, block, and record traffic.'),
        (3, 'Attacks, part I', 'Understand denial of service, web application attacks, defacement, and advance-fee fraud.'),
        (4, 'Attacks, part II', 'Recognize phishing, spear phishing, social engineering, and fake security software.'),
        (5, 'Operating-system hardening', 'Reduce the ways a workstation can be attacked and limit the damage of a compromise.'),
        (6, 'Investigating suspicious websites', 'Compare manual source review, automated reputation tools, and isolated testing.'),
        (7, 'Cryptography and cryptocurrency', 'Separate encryption, hashing, key systems, digital signatures, and blockchain concepts.'),
        (8, 'Secure network administration', 'Use secure protocols, logs, sensors, virtualization, and cloud safeguards.'),
    ]
]

specs = []


def add(lecture, slides, title, q, answer, teach, example, correct, wrong, terms=()):
    specs.append(dict(lecture=lecture, slides=slides, title=title, q=q, answer=answer,
                      teach=teach, example=example, correct=correct, wrong=wrong, terms=terms))


# Lecture 1
add(1,[4,9,10,11],'Why attackers attack','Which motives for cyberattacks appear in Lecture 1?',
    'The lecture groups common motives into financial gain, stealing information, curiosity or fun, and politically motivated disruption called hacktivism. A motive explains the attacker’s goal; it does not identify the exact technique used.',
    'The same phishing technique could support different motives. A criminal may want money, while a state-sponsored group may want confidential research.',
    'A motive describes the result an attacker wants. Defenders use it with other evidence to understand likely targets and behavior.',
    'Money, information theft, curiosity/fun, and hacktivism',['Only hardware failure and weather','Faster software and lower costs','Backups, patching, and encryption'],
    [('Hacktivism','Using hacking or disruption in support of a political or social cause.'),('Threat actor','A person or group capable of carrying out a harmful cyber action.')])
add(1,[12,13],'Stuxnet as a defense lesson','Why is Stuxnet important in a defensive cybersecurity course?',
    'Stuxnet showed that malicious software can cross into an industrial environment, search for a specific target, manipulate physical equipment, and hide the change by presenting normal-looking readings. Defenders must protect operational technology and removable-media paths, not only internet-facing computers.',
    'Stuxnet spread broadly but activated its damaging behavior only when it found the intended Siemens industrial setup. That distinction separates spreading from the final objective.',
    'A USB drive entering an isolated facility can create a path around an internet perimeter. Monitoring hosts and engineering systems still matters.',
    'It linked a computer compromise to manipulated physical equipment',['It was only a website advertisement','It proved isolated systems need no host defenses','It was a password manager for industrial users'],
    [('Stuxnet','Malware designed to target particular industrial control equipment.'),('SCADA','Supervisory Control and Data Acquisition: systems that monitor or control industrial processes.'),('Zero-day vulnerability','A software weakness for which defenders do not yet have an available fix or prior knowledge at the time of use.')])
add(1,[19,20,21],'Virtual machines and safe labs','What does virtualization let a cybersecurity student do?',
    'Virtualization lets one physical computer run multiple simulated computers called virtual machines. A student can build isolated test systems, take snapshots, run controlled experiments, and return a VM to an earlier clean state. Isolation reduces risk but does not make unsafe activity harmless.',
    'A snapshot records a VM state before a lab. After analyzing a sample in an authorized lab, the student can revert instead of rebuilding everything.',
    'The physical computer is the host. Each simulated computer is a guest VM. Network settings decide whether guests can reach the host, each other, or the internet.',
    'Run isolated guest systems and restore earlier snapshots',['Convert every attack into harmless text','Guarantee malware can never leave a guest','Replace the need for backups on production systems'],
    [('Virtual machine (VM)','A software-based computer with its own operating system and applications.'),('Host','The physical computer and operating environment running virtual machines.'),('Snapshot','A saved VM state that can be restored later.'),('VirtualBox','Virtualization software used in the course labs.')])
add(1,[18],'Defense as a process','What is the central goal of defensive cybersecurity?',
    'Defensive cybersecurity reduces the likelihood and impact of attacks by understanding threats, protecting systems, monitoring activity, investigating evidence, and recovering safely. One product cannot perform every part of that job.',
    'A firewall may block an unwanted connection, but a defender still needs host safeguards, logs, user education, and a response plan.',
    'Picture a store: locks reduce entry risk, cameras provide evidence, staff report suspicious behavior, and a recovery plan explains what happens after an incident.',
    'Use several coordinated safeguards to prevent, detect, investigate, and recover',['Purchase one security product and stop monitoring','Focus only on attacks that already succeeded','Remove all users from every computer'],
    [('Defense in depth','Using multiple safeguards so one failure does not expose the entire system.'),('Incident','An event that threatens or harms the confidentiality, integrity, or availability of information or systems.')])

# Lecture 2
add(2,[5,6,23,24],'Defense in depth and risk','Why does secure architecture use more than one safeguard?',
    'Different safeguards cover different failure modes. Perimeter devices can filter traffic, host controls can restrict local actions, monitoring can reveal suspicious behavior, and recovery controls can limit damage. The chosen protection should reflect asset value, risk, and available resources.',
    'If a malicious attachment reaches a laptop, limited privileges and application controls may still stop it after an email filter missed it.',
    'A castle with several walls illustrates the idea: crossing one boundary does not immediately expose everything behind it.',
    'One missed attack can still meet another independent safeguard',['Every safeguard detects exactly the same event','Multiple safeguards eliminate all residual risk','Security budgets do not affect architecture'],
    [('Asset','Something valuable that an organization needs to protect.'),('Risk','The possibility that a threat will exploit a weakness and cause harm.'),('Residual risk','Risk that remains after safeguards are applied.')])
add(2,[7,8],'Choke points and visibility','What are choke points and monitoring visibility?',
    'A choke point is a network location through which important traffic must pass, making consistent inspection possible. Visibility means defenders can observe useful activity at internet gateways and inside the network. Poor placement can leave blind spots.',
    'Monitoring only the internet edge may miss traffic between two compromised internal computers. Internal sensors add another view.',
    'A building with one staffed entrance creates a choke point. Cameras inside provide visibility after someone enters.',
    'They create inspectable paths and useful views of network activity',['They encrypt every stored file automatically','They remove the need for internal monitoring','They make every system use one password'],
    [('Choke point','A controlled path where traffic can be inspected or restricted.'),('Visibility','The ability to observe relevant events and traffic for detection and investigation.')])
add(2,[9],'Availability, scalability, and security','Which design qualities must a secure network balance?',
    'A network should remain available when needed, scale as demand grows, protect its systems and data, interoperate with required technology, stay manageable, and fit financial constraints. Maximizing one quality without considering the others can create an unusable design.',
    'A security appliance that cannot handle peak traffic may become a bottleneck and reduce availability even when its filtering works.',
    'A company plans growth from 100 to 1,000 users. Capacity and administrative effort must grow without discarding essential protections.',
    'Security must work together with availability, growth, management, and cost',['Security is the only design quality that matters','Availability means every user gets administrator rights','Scalability means removing traffic inspection'],
    [('High availability','Designing services to remain usable despite failures.'),('Redundancy','Using additional components or paths so another can continue after a failure.'),('Scalability','The ability to handle growth without unacceptable loss of performance or manageability.')])
add(2,[12,13],'Firewalls and router ACLs','How do firewalls and router access-control lists protect a network?',
    'Both can allow or block traffic according to rules such as source, destination, protocol, and port. Routers primarily connect networks and may apply ACLs. Firewalls specialize in enforcing security policy and may track connection state or inspect more context.',
    'A rule may allow HTTPS from the internet to one public web server while blocking direct access to an internal database.',
    'The rule is like a guest list that names which traffic may enter which door. Broad rules admit more than narrow rules.',
    'They enforce traffic rules at network boundaries',['They guarantee that allowed applications contain no malware','They replace authentication inside every application','They store a complete copy of every packet forever'],
    [('Firewall','A device or program that enforces rules on network traffic.'),('ACL','Access Control List: ordered permit or deny rules applied to traffic or resources.'),('Port','A logical number that helps identify a network service or application endpoint.')])
add(2,[14],'IDS versus IPS','What is the difference between an IDS and an IPS?',
    'An Intrusion Detection System observes activity and alerts when it recognizes a signature or anomaly. An Intrusion Prevention System can sit in the traffic path and block or modify traffic as well as alert. Prevention can stop harm but a mistaken block can interrupt legitimate work.',
    'An IDS reports a suspicious exploit attempt for an analyst. An inline IPS can drop that traffic before it reaches the target.',
    'A burglar alarm resembles detection. A locked gate that refuses entry resembles prevention. Both require accurate rules and review.',
    'An IDS alerts; an IPS can also block traffic',['An IDS encrypts while an IPS performs backups','An IDS runs only on laptops and an IPS only in clouds','An IDS allows all traffic and never records events'],
    [('IDS','Intrusion Detection System: monitors and alerts on suspicious activity.'),('IPS','Intrusion Prevention System: monitors and can automatically block suspicious activity.'),('Signature','A recognizable pattern associated with known activity.'),('Anomaly','Activity that differs from an established or expected pattern.')])
add(2,[15],'Proxy servers','What security job does a web proxy perform?',
    'A proxy acts as an intermediary between a user and a destination service. A web proxy can apply organizational policy, inspect requests, and block categories or known malicious sites before the user connects directly.',
    'When a user requests a known malware domain, the proxy can return a block page instead of retrieving the site.',
    'The browser talks to the proxy; the proxy evaluates the request and, if allowed, communicates with the website on the user’s behalf.',
    'It evaluates and mediates user web requests',['It assigns every computer a permanent MAC address','It proves every unblocked website is safe forever','It replaces disk encryption'],
    [('Proxy server','An intermediary that receives a request and makes the onward request under defined rules.'),('URL filtering','Allowing or blocking web destinations according to addresses, categories, or reputation.')])
add(2,[16,17,20],'Host protection and application allowlisting','How do antivirus, host IPS, and application allowlisting differ?',
    'Antivirus looks for known or suspicious malicious software. Host IPS watches local events and can act on host-specific rules. Application allowlisting permits approved software and blocks unapproved programs by default. Each can miss activity that another catches.',
    'A new unapproved executable may have no antivirus signature. Allowlisting can still prevent it from launching because it is absent from the approved list.',
    'Antivirus asks whether a file appears bad. Allowlisting asks whether the organization approved it to run. Host IPS watches what occurs on the device.',
    'They use different evidence and policies to protect the endpoint',['All three are names for the same firewall rule','All three only inspect traffic at the internet router','All three guarantee no false positives'],
    [('HIPS','Host Intrusion Prevention System: software that monitors and can block suspicious activity on one host.'),('Antivirus','Software that detects and responds to known or suspicious malicious code.'),('Application allowlisting','Allowing approved programs to run while blocking programs outside the approved list.')])
add(2,[18,19],'Full packet capture versus flow data','What is the difference between packet capture and flow data?',
    'Full packet capture can preserve packet contents and headers for detailed investigation, but it needs substantial storage and may contain sensitive data. Flow data summarizes who communicated with whom, when, for how long, and often how much data moved, without preserving the complete conversation.',
    'Flow may show a laptop contacted a server for ten minutes. Packet capture may show the protocol details and unencrypted content exchanged during that connection.',
    'A phone bill resembles flow records. A recording of the call resembles full content capture.',
    'Flow summarizes connections; packet capture can preserve packet-level detail',['Flow contains every file while capture contains only IP addresses','Packet capture cannot support investigations','Flow automatically blocks every listed connection'],
    [('PCAP','Packet capture: recorded network packets for later analysis.'),('Flow data','Summaries of network conversations rather than complete packet contents.')])

# Lecture 3
add(3,[4,6,8,9,10],'DDoS, SYN floods, and Slowloris','How do DDoS attacks interfere with availability?',
    'A Distributed Denial of Service attack uses many sources or requests to exhaust a service or its network so legitimate users cannot receive service. A SYN flood consumes connection-handling resources. Slowloris keeps many incomplete requests open slowly. Defenses depend on the traffic pattern and may involve providers, filtering, capacity, and timeouts.',
    'A SYN flood sends many connection starts without completing the handshake. Slowloris sends enough partial data to keep sessions waiting.',
    'Both attacks occupy limited service capacity, but one can flood quickly while the other holds resources open.',
    'They consume limited network or server capacity needed by real users',['They secretly change database queries without affecting availability','They only work after a user reveals a password','They encrypt backups for confidentiality'],
    [('DDoS','Distributed Denial of Service: many sources overwhelm a service or its network.'),('Botnet','A group of compromised devices controlled to perform coordinated actions.'),('SYN flood','An attack that sends many TCP connection requests without completing them.'),('Slowloris','A denial-of-service technique that holds many web connections open with slow partial requests.')])
add(3,[11,13],'SQL injection','What makes SQL injection possible, and how should developers prevent it?',
    'SQL injection occurs when an application treats untrusted input as part of a database command. The primary defense is to keep data separate from command structure by using parameterized queries, supported by input validation, least privilege, testing, and monitoring. A web application firewall can add protection but does not repair unsafe code.',
    'A login value should become a data parameter. Concatenating it into a SQL command may let crafted text change the command’s meaning.',
    'The database must receive the query structure separately from the user-supplied value so the value cannot become an instruction.',
    'The application mixes untrusted input into a database command',['The database has too many encrypted backups','A router uses a long ACL','A user opens two browser tabs'],
    [('SQL injection','A vulnerability in which crafted input changes a database command.'),('Parameterized query','A query that keeps command structure separate from supplied values.'),('Input validation','Checking whether input meets expected type, length, range, or format rules.')])
add(3,[14,15],'Cross-site scripting','What happens in a cross-site scripting attack?',
    'Cross-site scripting occurs when a web application places untrusted content into a page without the context-appropriate output encoding or other safeguards. A victim’s browser may then execute attacker-controlled script in the trusted site’s context. Defenses include output encoding, safe APIs, content security policy, validation, and secure cookie settings.',
    'A comment field stores attacker-controlled script. When another user views the comment, the browser may run it as part of the site.',
    'SQL injection targets a database command. XSS targets content that the browser interprets. Both start with unsafe handling of untrusted data.',
    'A trusted page causes a browser to execute attacker-controlled script',['A router runs out of cable ports','A disk uses full encryption','A DNS server assigns a local address'],
    [('XSS','Cross-Site Scripting: injection of active content that a victim’s browser runs in a trusted site context.'),('Output encoding','Representing untrusted data so a browser treats it as text in the intended context.')])
add(3,[16,18],'Website defacement','What is website defacement?',
    'Website defacement is an unauthorized change to visible website content, often used for embarrassment, messaging, or notoriety. Attackers may exploit vulnerable software or stolen credentials. Defenders patch systems, protect accounts, restrict write permissions, monitor changes, and maintain recoverable content.',
    'An attacker gains access to a content-management account and replaces the homepage. The visual change is the symptom; the account compromise is the access path.',
    'Restoring the page without fixing the exploited weakness allows the attacker to change it again.',
    'An attacker changes site content without authorization',['A user changes browser zoom','A server compresses an image','A company publishes an approved redesign'],
    [('Website defacement','An unauthorized alteration of a website’s visible content.'),('File integrity monitoring','Detecting unexpected changes to monitored files.')])
add(3,[19,20,21,22,23,24],'Advance-fee and 419 scams','How does an advance-fee scam manipulate a victim?',
    'The scam promises money, a prize, or another benefit, then gradually requests personal information or payment to release it. Attackers may begin with harmless-looking questions to build trust before seeking bank details or fees. Victims should stop contact, preserve evidence, and report through appropriate channels.',
    'A false lottery notice asks for contact information first, then later demands a processing payment. The staged requests lower suspicion.',
    'The key pattern is an unexpected reward combined with a request to pay or disclose information before receiving it.',
    'It promises a benefit and then requests money or sensitive information',['It patches a workstation automatically','It blocks a website category at a proxy','It encrypts a legitimate bank transfer'],
    [('419 scam','A type of advance-fee fraud named after a section of Nigerian law.'),('Advance-fee fraud','A scheme that demands an upfront payment or information for a promised future benefit.')])
add(3,[2,3,25],'Attack, vulnerability, and defense','Why must defenders separate an attack from the weakness it uses?',
    'An attack is the harmful action or attempt. A vulnerability is a weakness that may enable it. A defense reduces likelihood or impact. Naming these separately helps teams choose a control that addresses the actual path instead of the visible symptom alone.',
    'SQL injection is an attack technique. Unsafe query construction is the vulnerability. Parameterized queries address that weakness.',
    'If water enters through a broken window, removing the water handles the result; repairing the window addresses the path.',
    'The weakness determines which safeguard can interrupt the attack path',['Every attack uses the same software weakness','A visible symptom always reveals the root cause','Defenses only matter after data is stolen'],
    [('Vulnerability','A weakness that a threat may exploit.'),('Exploit','Code or a technique that takes advantage of a vulnerability.'),('Mitigation','An action that reduces the likelihood or impact of harm.')])

# Lecture 4
add(4,[5,6,7,8,9],'Phishing, smishing, and vishing','What makes a message a phishing attempt?',
    'Phishing uses a deceptive message to persuade a person to disclose information, open a harmful file, install software, send money, or visit a false site. The channel can be email or instant messaging; smishing uses text messages and vishing uses voice calls.',
    'A message impersonates payroll and links to a false login page. The attacker wants the victim to supply credentials.',
    'The attack targets human trust. A professional logo or familiar name does not prove the sender or destination is legitimate.',
    'It uses deception to make a person take an unsafe action',['It passively records every packet on a switch','It automatically patches a browser','It verifies a digital signature'],
    [('Phishing','A deceptive message intended to trigger disclosure, payment, installation, or another unsafe action.'),('Smishing','Phishing delivered through SMS or text messaging.'),('Vishing','Voice-based phishing or social engineering, often by phone.'),('Social engineering','Manipulating people into actions or disclosures that weaken security.')])
add(4,[13,14,15],'Spear phishing','How is spear phishing different from broad phishing?',
    'Spear phishing targets selected people with details chosen to appear relevant or trustworthy. The attacker may research a person’s role, coworkers, current events, or projects. Broad phishing sends a similar lure to many recipients and waits for someone to respond.',
    'A forged message to one finance employee refers to a real executive and current vendor. The specificity makes the request more believable.',
    '“Spear” describes the narrow target. A convincing message still needs independent verification through a trusted channel.',
    'It is tailored to a specific person or small group',['It can only be delivered by postal mail','It never includes a link or attachment','It is an untargeted message sent identically to everyone'],
    [('Spear phishing','Phishing tailored to a particular person or group.'),('Pretext','A fabricated story used to make a request seem legitimate.')])
add(4,[16,17,18,19],'Email headers and investigation','What can an email header help an investigator determine?',
    'Header fields can show routing hops, timestamps, message identifiers, authentication results, and addresses used during delivery. Analysts compare them with the visible sender and organizational records. Headers provide evidence, but individual fields can be forged or misunderstood.',
    'A display name says “Payroll,” while authentication results and the sending domain point elsewhere. That mismatch supports further investigation.',
    'Read Received lines with time zones and direction in mind. Preserve the original message because forwarding can alter or hide useful header data.',
    'The technical path and authentication evidence associated with delivery',['The sender’s intent with absolute certainty','Every file the sender has ever opened','The recipient’s operating-system password'],
    [('Email header','Metadata describing message addressing, routing, timestamps, and delivery processing.'),('Spoofing','Falsifying an identity or source value to appear trusted.'),('BCC','Blind Carbon Copy: recipients hidden from other recipients.')])
add(4,[20,21,22],'Responding safely to suspicious messages','What is the safest way to verify an unexpected account message?',
    'Avoid the supplied link or phone number. Open the organization’s known app or type its trusted address yourself, or contact the organization using a separately verified number. Report the suspicious message and preserve it according to policy.',
    'A banking message says an account is locked. Open the bank’s known app instead of using the message link.',
    'Verification needs an independent path. Contact information inside the suspicious message remains under the sender’s control.',
    'Use a trusted channel obtained independently of the message',['Reply and ask whether the sender is malicious','Open the link if the logo looks correct','Disable antivirus before opening the attachment'],
    [('Out-of-band verification','Checking a request through a separate trusted communication path.'),('Credential','Information used to authenticate, such as a password or security key.')])
add(4,[23,24,25,26,27],'Fake antivirus and scareware','How does fake antivirus software pressure a victim?',
    'Scareware presents alarming claims about infections or disk problems, then pressures the user to install software or pay for a false fix. The installed program may steal information, weaken real protection, or create more pop-ups. Use approved security tools and support channels.',
    'A browser pop-up announces hundreds of infections and demands immediate payment. A webpage cannot be trusted simply because it resembles a system scanner.',
    'Urgency and fear push the user past normal verification. Close the prompt safely and ask support to inspect the device if installation occurred.',
    'It invents or exaggerates danger to trigger installation or payment',['It quietly improves disk performance for free','It is an operating-system patch from every vendor','It verifies that a website certificate is valid'],
    [('Scareware','Software or a message that uses frightening claims to push payment or installation.'),('Rogue antivirus','Malicious or deceptive software presented as legitimate antivirus protection.')])
add(4,[28,29,30],'Fake disk tools','Why is a fake disk defragmenter a security problem?',
    'A fake disk utility displays invented errors and asks the victim to buy or install a supposed repair. It uses the same social-pressure pattern as rogue antivirus and may install malware or collect payment information.',
    'The program reports critical disk errors immediately after a user visits a suspicious site, even though it never performed a trustworthy scan.',
    'A realistic interface is only appearance. Verify alerts through the operating system or an approved support process.',
    'It uses false system errors to sell or install an unsafe product',['It reorganizes approved files under administrator supervision','It creates a verified offline backup','It checks a signed operating-system update'],
    [('Fake disk defragmenter','Scareware that claims storage errors exist and pressures the user to purchase a false repair.')])
add(4,[31,32],'User awareness and reconnaissance','Why do technical controls and user awareness work together?',
    'Filters and endpoint controls can block many lures, but attackers change content and research targets. Users need a clear way to recognize unusual requests, verify them, and report them. Defenders also need to understand reconnaissance because public details can make a targeted message more convincing.',
    'A filter allows a new sender. An employee notices the unusual payment request and calls the known manager instead of acting.',
    'Technology reduces exposure while trained human judgment can interrupt a message that passes automated checks.',
    'Each can catch suspicious activity the other misses',['Training makes mail filters unnecessary','A mail filter can determine every human intention','Reconnaissance only examines physical buildings'],
    [('Reconnaissance','Collecting information about a target before taking further action.'),('Security awareness','Helping people recognize, avoid, and report security risks in their work.')])

# Lecture 5
add(5,[2,5],'Operating-system hardening','What does operating-system hardening mean?',
    'Operating-system hardening means changing a host’s configuration to reduce its attack surface and limit damage. Common steps include timely patching, limited user privileges, removing unneeded services, enabling host firewalls, using endpoint protection, and applying tested security settings.',
    'A workstation does not need a remote service, so an administrator disables it and closes the related listening port.',
    'Hardening removes unnecessary opportunities and strengthens the functions that must remain. It is an ongoing process as software and needs change.',
    'Reducing unnecessary exposure and strengthening required functions',['Adding every optional service for future use','Giving all users administrator access','Disabling updates so settings never change'],
    [('Hardening','Reducing attack surface and strengthening a system through secure configuration.'),('Attack surface','The collection of reachable paths, functions, and weaknesses that could be attacked.')])
add(5,[6,7,8],'Patching safely','Why do organizations test patches before broad deployment?',
    'Patches correct known defects and vulnerabilities, but a change may conflict with an application or configuration. Organizations obtain trusted updates, test them on representative systems, plan deployment and rollback, install them according to risk, and verify the result.',
    'A security patch works on a test workstation but breaks a required legacy application. Testing reveals the compatibility problem before every employee is affected.',
    'Delay also carries risk because known vulnerabilities remain exposed. Teams balance urgency with controlled testing and compensating safeguards.',
    'Testing can reveal compatibility or operational problems before production rollout',['Testing proves attackers cannot use any future vulnerability','A tested patch never needs verification after installation','Testing replaces the need to obtain the patch from a trusted source'],
    [('Patch','A software update that corrects defects, including security weaknesses.'),('Test environment','A controlled environment used to evaluate a change before production.'),('Rollback','A planned return to the earlier version or configuration if a change fails.')])
add(5,[9,10,11],'Least privilege and reverse shells','How does using a non-administrator account reduce damage?',
    'Least privilege gives a user or process only the permissions needed for approved work. If malicious code runs under that account, it may have less ability to change protected files or security settings. A reverse shell makes the compromised host initiate a command channel outward, sometimes through commonly allowed traffic.',
    'A user can edit documents but cannot install a system driver. Malware launched by that user encounters the same permission boundary unless it exploits another weakness.',
    'Least privilege limits authority; it does not prevent every compromise. Egress monitoring and host controls help detect or restrict unauthorized outbound command channels.',
    'Malicious code initially receives fewer powerful permissions',['The account cannot connect to any network','The user automatically becomes an administrator during attacks','Every reverse shell uses an inbound blocked port only'],
    [('Least privilege','Granting only the permissions needed for an approved task.'),('Reverse shell','A command shell in which the compromised host initiates a connection to the remote operator.'),('Egress filtering','Controlling traffic that leaves a network or host.')])
add(5,[12,13,14,15,16,17,18,19],'Services, updates, and host firewalls','How do disabled services and host firewalls reduce attack surface?',
    'An unnecessary service creates code, a listening path, and configuration that the host does not need. Disabling it removes that opportunity. A host firewall restricts which remaining services may receive or send traffic. Automatic updates can reduce exposure time when the organization has an appropriate testing and deployment process.',
    'A database server should not expose a file-sharing service nobody uses. Disable it rather than relying only on a perimeter firewall.',
    'The host firewall follows the device across networks and can restrict local traffic that never crosses the internet firewall.',
    'They remove unused entry points and restrict access to required ones',['They make passwords and account controls unnecessary','They guarantee every allowed service is free of bugs','They turn a workstation into a network router'],
    [('Service','A program or function that runs to provide a capability, often listening for requests.'),('Host firewall','Traffic-filtering software on an individual device.'),('Automatic update','A mechanism that obtains and installs updates with limited manual action under configured policy.')])
add(5,[20,21,22],'Antivirus versus host IPS','How do antivirus and host IPS contribute to hardening?',
    'Antivirus detects known or suspicious malicious software. Host IPS watches events on one machine and can apply detailed behavioral or pattern rules. Both add layers, but they require updates, tuning, and review. False positives are legitimate events incorrectly flagged as threats.',
    'A host IPS rule alerts when an unusual program creates a file in a protected system folder. Antivirus may separately identify the file’s known malicious signature.',
    'Detailed host rules increase visibility but also generate noise. Analysts must distinguish useful signals from routine activity.',
    'They inspect different host evidence and can detect different suspicious behavior',['They physically disconnect every infected cable','They replace all operating-system permissions','They only protect public websites'],
    [('False positive','A legitimate event incorrectly identified as malicious.'),('Heuristic detection','Detection based on suspicious traits or behavior rather than one exact known signature.')])
add(5,[23,24,25,26,27,28,29],'Browser controls, hardening guides, and NAC','How can organizations enforce and validate workstation hardening?',
    'Organizations can use secure baselines and hardening guides, configuration policy, browser restrictions, endpoint tools, and Network Access Control. Changes should be applied in manageable groups and tested so administrators can trace compatibility failures. NAC can check device posture before granting normal network access.',
    'A laptop missing required patches connects to the network. NAC places it in a restricted remediation area until it meets policy.',
    'A long checklist does not prove the system works securely. Apply settings deliberately, test required work, and monitor whether devices stay compliant.',
    'Use tested baselines and posture checks to keep devices within policy',['Apply hundreds of settings at once without testing','Let users disable every safeguard permanently','Use NAC only to increase monitor brightness'],
    [('NAC','Network Access Control: technology that evaluates a device or user before granting network access.'),('Security baseline','An approved minimum set of security settings for a type of system.'),('Device posture','A device’s current security condition, such as patch and protection status.')])

# Lecture 6
add(6,[3,4,5,6],'Website safety changes over time','Why can the same website be safe one day and malicious another?',
    'A legitimate site can be compromised, an advertisement or external script can change, or a malicious site can be cleaned. Reputation and scan results describe a point in time. Defenders combine current evidence and avoid treating an earlier clean result as a permanent guarantee.',
    'A news site is safe in the morning, then an attacker changes one included script in the afternoon. Yesterday’s scan cannot evaluate the new content.',
    'A website is a changing collection of first-party and third-party resources. The domain name alone does not describe every resource loaded now.',
    'Website content and third-party resources can change after an earlier scan',['A domain name changes every second by definition','HTTPS guarantees all page content is harmless','A clean result deletes all future vulnerabilities'],
    [('Drive-by download','A download or exploit triggered through visiting a compromised or malicious page, sometimes with little interaction.'),('Reputation service','A service that records or estimates the safety history of domains, addresses, or files.')])
add(6,[7,8,9,10,12,14],'Manual source review','What does an analyst inspect during a manual website review?',
    'The analyst examines HTML, scripts, redirects, embedded frames, downloads, and obfuscated code for behavior that does not fit the site. An iframe is not automatically malicious, and JavaScript is not automatically malicious; context and destination matter.',
    'A hidden iframe loads a newly registered external domain and starts a download. Those combined facts justify deeper isolated analysis.',
    'Manual review can reveal logic that an automated tool misses, but opening active content on a normal workstation can expose the analyst.',
    'Page code, embedded resources, redirects, and suspicious behavior',['Only the color and font of the homepage','Only whether the domain uses HTTPS','The visitor’s private password database'],
    [('Iframe','An HTML element that embeds another page or resource inside a page.'),('Obfuscation','Making code or data harder for people or tools to understand.'),('Redirect','A response or script that sends a browser to another location.')])
add(6,[15,16,17,18,19,20,21,22,23,24],'Automated website analysis','What are the strengths and limits of automated website-analysis tools?',
    'Automated scanners and reputation services can quickly compare a site with known patterns, behavior, and reports. They scale better than manual review but can miss new attacks, produce false results, or evaluate a different moment and environment. Analysts should treat results as evidence, not proof.',
    'Two scanners report no known malware, but the site only delivers harmful code to one browser version. The scan reduces uncertainty without eliminating it.',
    'A reputation score depends on prior observation. A new malicious domain may not have a history yet.',
    'They provide fast evidence but can miss new or conditional behavior',['They guarantee a site stays safe forever','They make isolation unnecessary for suspicious content','They can determine a human attacker’s identity from the page color'],
    [('False negative','Malicious activity that a safeguard or test fails to identify.'),('Automated analysis','Using tools to inspect content or behavior with repeatable rules and detections.')])
add(6,[25,26],'Isolated dynamic testing','Why use a virtual machine to investigate a suspicious site?',
    'An isolated VM can mimic a target environment while monitoring file, registry, process, and network changes. A snapshot supports recovery after an authorized test. Analysts still restrict network access, avoid real credentials, protect the host, and follow policy because isolation can fail.',
    'The analyst opens a suspect page in a disposable guest, records its outbound connections, and reverts to the clean snapshot after collecting evidence.',
    'Dynamic analysis observes what content actually does. Static source review reads code without executing it. Each can reveal evidence the other misses.',
    'It contains the experiment and lets the analyst observe system changes',['It guarantees legal authorization for any website','It makes malware unable to contact any network automatically','It proves a clean host needs no backup'],
    [('Static analysis','Examining code or content without executing it.'),('Dynamic analysis','Observing behavior while code or content executes in a controlled environment.'),('Sandbox','An isolated environment designed to limit the effects of untrusted activity.')])
add(6,[27,28],'Safe investigation decisions','What should a defender do before interacting with a suspicious website?',
    'First confirm authorization and whether interaction is necessary. Use existing reputation and passive evidence when sufficient. If active testing is required, use an approved isolated environment, restrict connectivity, capture evidence, and never enter real credentials.',
    'A user reports a suspicious link. The analyst checks the message and approved intelligence sources before deciding whether a controlled visit adds value.',
    'Curiosity does not justify exposure. Investigation should answer a defined question with the least risky method that can answer it.',
    'Define the question and use the least risky authorized method',['Open it on a production administrator workstation','Forward it to coworkers to compare results','Enter a real password to see whether login works'],
    [('Passive investigation','Gathering existing information without directly interacting with the suspicious target.'),('Active investigation','Interacting with a target or content in a controlled, authorized manner.')])

# Lecture 7
add(7,[3,4,5,6,7],'Encryption vocabulary','How are plaintext, ciphertext, encryption, decryption, a cipher, and a key connected?',
    'Plaintext is the readable input. A cipher is the algorithm that combines plaintext with a key to produce ciphertext. Decryption uses the appropriate key and algorithm to recover plaintext. Security should rely on protecting keys and using reviewed algorithms, not hiding the algorithm.',
    'A file begins as readable plaintext. Encryption transforms it into ciphertext. An authorized recipient uses the required key to decrypt it.',
    'The algorithm is like a known lock design; the key controls who can perform the authorized transformation.',
    'A cipher and key transform plaintext into ciphertext',['A hash key converts ciphertext directly into a password','Plaintext is already unreadable encrypted output','Decryption permanently destroys all original data'],
    [('Plaintext','Readable data before encryption or after successful decryption.'),('Ciphertext','Data transformed by encryption into an unreadable form.'),('Cipher','An algorithm used for encryption and decryption.'),('Key','A value that controls a cryptographic transformation.')])
add(7,[8,9,15],'What cryptography can protect','Which security properties can cryptography support?',
    'Cryptography can support confidentiality, integrity, authentication, non-repudiation, and obfuscation in appropriate designs. It can protect data at rest and in transit; protecting data while actively in use is harder because an authorized process needs access to it.',
    'Encryption protects a stored file’s confidentiality. A verified digital signature can support integrity, sender authentication, and non-repudiation.',
    'One mechanism does not automatically supply every property. Encryption alone does not prove who created a message.',
    'Confidentiality, integrity, authentication, and related assurances',['Unlimited availability with no redundancy','Physical cooling for every server','Automatic deletion of every backup'],
    [('Confidentiality','Preventing unauthorized disclosure.'),('Integrity','Protecting accuracy and detecting unauthorized alteration.'),('Authentication','Establishing that an identity or source is genuine.'),('Non-repudiation','Evidence that makes it difficult for a party to credibly deny an action or message.')])
add(7,[10,11,12,13,14],'Hashing and collisions','What does a cryptographic hash do?',
    'A hash function maps input of any length to a fixed-length digest. Defenders compare digests to detect changes. Hashing is designed as a one-way operation and does not provide decryption. A collision occurs when different inputs produce the same digest; obsolete algorithms with practical collision weaknesses should not be used for collision-sensitive security.',
    'A vendor publishes a trusted file hash. After download, you compute the file’s hash and compare it with the trusted value to detect alteration.',
    'A digest is a fingerprint for comparison, not an encrypted copy of the file. You cannot reconstruct the full file from the digest.',
    'It creates a fixed-length digest used to compare data',['It creates ciphertext that every user can decrypt without a key','It guarantees two inputs can never share a digest','It compresses a file and stores every original byte'],
    [('Hash','A fixed-length digest computed from input data.'),('Digest','The output of a hash function.'),('Collision','Two different inputs producing the same hash output.'),('SHA-256','A member of the Secure Hash Algorithm family that produces a 256-bit digest.'),('MD5','An older 128-bit hash with collision weaknesses; unsuitable for collision-resistant security.')])
add(7,[16],'Stream and block ciphers','How do stream and block ciphers process data differently?',
    'A stream cipher processes a stream in small units, while a block cipher transforms fixed-size blocks. Secure use depends on the full construction, including modes, nonces, key handling, and authentication, rather than the category name alone.',
    'A block cipher may need a defined mode to protect a message longer than one block. Reusing a nonce in a mode that requires uniqueness can break security.',
    'The processing unit differs, but both still require an approved design and correct implementation.',
    'A stream cipher handles a stream in small units; a block cipher handles fixed-size blocks',['A stream cipher hashes while a block cipher stores plaintext','A block cipher never uses a key','A stream cipher can only protect images'],
    [('Stream cipher','A cipher that encrypts a data stream in small units.'),('Block cipher','A cipher that transforms fixed-size blocks of data.'),('Nonce','A value intended for one use or a defined uniqueness requirement in a cryptographic protocol.')])
add(7,[17,18,19,20],'Symmetric encryption','How does symmetric encryption work?',
    'Symmetric encryption uses the same secret key, or directly related shared secret, for encryption and decryption. It is efficient for large amounts of data, but authorized parties need a secure method to share and protect the secret key.',
    'A disk-encryption system uses a symmetric data-encryption key because large files must be processed efficiently.',
    'Anyone who obtains the shared key may decrypt protected data and possibly create convincing ciphertext, so key distribution and storage matter.',
    'The authorized parties use the same shared secret key',['Everyone encrypts with a public key and only a private key decrypts','No key is required after installation','The digest is reversed to recover plaintext'],
    [('Symmetric encryption','Encryption in which authorized parties use the same shared secret key.'),('AES','Advanced Encryption Standard: a widely used symmetric block cipher.'),('DES','Data Encryption Standard: an obsolete symmetric cipher with a 56-bit key.'),('3DES','Triple DES: repeated DES operations, now deprecated for new protection.')])
add(7,[21,22,23,24,25,26],'Asymmetric encryption and signatures','How do public and private keys work together?',
    'Asymmetric cryptography uses a mathematically related key pair. A public key may be shared while the private key remains controlled by its owner. Depending on the scheme, the pair supports encryption or digital signatures. For a signature, the private key creates the signature and the public key verifies it.',
    'A software vendor signs an update with its private key. A device uses the vendor’s trusted public key to verify the signature before installation.',
    'A valid signature supports source and integrity claims. It does not hide the signed data unless encryption is also used.',
    'The private key signs and the corresponding public key verifies',['The public key must stay secret while the private key is posted','Both keys are identical copies','A signature automatically encrypts every signed message'],
    [('Asymmetric cryptography','Cryptography that uses a related public and private key pair.'),('Public key','The shareable member of an asymmetric key pair.'),('Private key','The protected member of an asymmetric key pair.'),('Digital signature','A cryptographic value created with a private key and checked with a public key.'),('RSA','An asymmetric algorithm based on properties of large integers.'),('DSA','Digital Signature Algorithm: an asymmetric algorithm used for signatures.')])
add(7,[27,28,29],'Cryptographic attacks and downgrade risk','What is a downgrade attack?',
    'A downgrade attack forces systems to fall back from a stronger protocol or algorithm to an older weaker option. Defenders disable deprecated choices, require safe minimum versions, and monitor failed negotiation. Collision attacks are different: they seek distinct inputs with the same hash.',
    'A client and server both support a modern protocol, but an attacker interferes so they negotiate an obsolete version with known weaknesses.',
    'Compatibility fallbacks can create an attack path. Supporting a strong option does not help if an attacker can force the weak one.',
    'It forces communication to use an older weaker security option',['It adds a longer key to every connection','It restores a VM snapshot','It finds a website through DNS'],
    [('Downgrade attack','Forcing use of an older or weaker security mode.'),('Deprecated algorithm','An algorithm no longer recommended because stronger or safer choices exist.'),('Birthday attack','A collision-search strategy based on the birthday-paradox probability effect.')])
add(7,[30,31,32,33,34,35],'Software and hardware encryption','Where can encryption be applied?',
    'Encryption can protect individual files, file systems, full disks, removable drives, databases, and communications. Hardware modules such as TPMs and HSMs can protect keys or perform cryptographic operations. The appropriate control depends on the threat and what happens while the system is running.',
    'Full-disk encryption protects a stolen powered-off laptop, but an already unlocked laptop may expose files to the signed-in user or running malware.',
    'Encryption at rest does not replace account security, backups, or protection while data is actively used.',
    'At file, disk, device, database, and communication layers',['Only inside public web pages','Only after data has been deleted','Only on computers without operating systems'],
    [('FDE','Full-Disk Encryption: encryption intended to protect an entire storage volume.'),('EFS','Encrypting File System: Windows file-system encryption for selected files and folders.'),('TPM','Trusted Platform Module: hardware that supports protected cryptographic operations and key storage.'),('HSM','Hardware Security Module: dedicated hardware for protecting keys and performing cryptographic operations.'),('PGP','Pretty Good Privacy: a system associated with file and email cryptography.')])
add(7,[38,39,40,41,42,43],'Blocks, hash pointers, and Merkle trees','How does a blockchain connect records?',
    'A blockchain organizes transactions into blocks. A block header contains metadata and a hash reference to earlier data. Changing an earlier block changes its hash and breaks later references unless they are recomputed under the network’s rules. A Merkle tree combines transaction hashes into one root used to verify membership efficiently.',
    'To prove a transaction belongs to a block, a node can provide the transaction and a path of neighboring hashes leading to the recorded Merkle root.',
    'Hash links make changes evident; consensus rules determine which proposed history participants accept. Hashing alone does not make false input truthful.',
    'Each block references prior data with hashes and summarizes transactions with a Merkle root',['Every block stores only an unencrypted password','One central spreadsheet decides all peer actions','A hash pointer hides every transaction from all participants'],
    [('Blockchain','A ledger structure that links blocks of records using cryptographic references.'),('Hash pointer','A reference that includes the hash of the referenced data.'),('Merkle tree','A tree of hashes that summarizes many records in one root.'),('Merkle root','The top hash that commits to the records represented by a Merkle tree.')])
add(7,[44,45,46,47,50,51,52],'Consensus, mining, forks, and P2P','Why does a distributed blockchain need consensus?',
    'Participants need rules for agreeing on an accepted transaction history when messages, faults, and competing blocks exist. Proof-of-work mining searches for a nonce that satisfies a target and is difficult to find but easy to verify. A protocol change without shared adoption can create a fork.',
    'Two miners publish blocks at similar times. Nodes follow the protocol’s chain-selection rule until one history gains the required preference.',
    'Peer-to-peer distribution spreads data and work across nodes. It does not mean every node makes an independent history with no agreement rules.',
    'It gives nodes rules for selecting a shared accepted history',['It makes every transaction legal automatically','It prevents all software changes','It stores every private key in one central node'],
    [('Consensus','Rules and processes that help distributed participants agree on accepted state.'),('Nonce','A value varied during proof-of-work attempts.'),('Mining','In proof-of-work systems, searching for a valid block value and proposing the block.'),('Fork','A divergence in a blockchain history or protocol rules.'),('P2P','Peer-to-Peer: a network model in which peers provide and consume resources.'),('Distributed ledger','A ledger whose records are shared or replicated across multiple nodes.')])

# Lecture 8
add(8,[3,4,5,6,7,8,13,14],'Packets, TCP, and IP','What jobs do TCP and IP perform?',
    'IP provides addressing and routing for packets across networks. TCP runs above IP and provides a connection-oriented byte stream with ordering, acknowledgments, retransmission, and flow control. A packet also carries control information in headers; the application data is the payload.',
    'A browser sends data through TCP. IP routers forward the resulting packets. The receiver’s TCP reorders data and detects missing portions for retransmission.',
    'IP helps data reach the destination host. TCP helps the endpoints exchange an ordered reliable stream. They cooperate but solve different problems.',
    'IP routes packets; TCP provides reliable ordered transport',['TCP assigns website names while IP encrypts disks','IP guarantees application authentication','TCP stores every packet permanently'],
    [('Packet','A formatted unit of data sent through a network.'),('Header','Control information placed before payload data.'),('Payload','The carried data belonging to a higher layer or application.'),('TCP','Transmission Control Protocol: reliable connection-oriented transport.'),('IP','Internet Protocol: addressing and routing across IP networks.'),('Checksum','A value used to detect certain transmission errors.')])
add(8,[15,16,17,18,19,20,21],'Spoofing, scanning, and Wireshark','What evidence can a packet analyzer provide?',
    'A packet analyzer such as Wireshark captures and decodes traffic visible to the selected interface. Analysts can inspect addresses, ports, flags, timing, protocol fields, and unencrypted payloads. It does not automatically prove who physically operated a source, because addresses can be spoofed or traffic can pass through compromised hosts.',
    'Repeated SYN packets to many ports may indicate scanning. The pattern supports an interpretation when combined with context and logs.',
    'A capture sees what reached its collection point. Traffic elsewhere, encrypted content, or dropped traffic may be absent.',
    'Protocol fields and timing for traffic visible at the capture point',['Every event on networks the interface cannot observe','The real human identity behind every IP address','Plaintext from every encrypted session without keys'],
    [('Wireshark','A packet-capture and protocol-analysis application.'),('IP spoofing','Using a forged source IP address in packet headers.'),('Port scan','Probing ports to learn which network services may be reachable.'),('SYN','A TCP flag used to begin establishing a connection.')])
add(8,[22,23,24],'TCP/IP protocols and security','Why are application protocols part of network defense?',
    'The TCP/IP suite includes many application protocols, each with its own purpose and security properties. Defenders must know what a protocol exposes, whether it authenticates peers or encrypts data, and which ports and systems should use it. A protocol’s presence alone does not prove malicious activity.',
    'FTP can transfer files but sends sensitive information without encryption in its basic form. A secure alternative changes the protection of the connection.',
    'Traffic rules should follow actual business need. Blocking every unfamiliar protocol can break work; allowing every protocol expands exposure.',
    'Protocols define how services communicate and what protections they provide',['Every application protocol automatically encrypts data','Protocols only affect physical cables','One port number proves the user’s identity'],
    [('Protocol','Agreed rules and formats for communication.'),('TCP/IP','The suite of protocols used for internetwork communication, including TCP and IP.')])
add(8,[25,26,27],'SNMP and ICMP','How are SNMP and ICMP used differently?',
    'Simple Network Management Protocol lets administrators query and manage network-device information through agents and management data. SNMPv3 adds authentication and privacy features absent from older community-string designs. ICMP supports network control and diagnostic messages; ping commonly uses ICMP to test reachability and measure response time.',
    'A monitoring system uses SNMP to read interface counters and CPU use, while ping checks whether the device responds and how long replies take.',
    'A community string acts like a shared secret in older SNMP versions and should not be treated as strong modern protection.',
    'SNMP reads management data; ICMP supports reachability and network diagnostics',['SNMP transfers email while ICMP encrypts disks','ICMP manages device configuration databases','They are two names for HTTPS'],
    [('SNMP','Simple Network Management Protocol: monitors and manages network devices.'),('Community string','A shared value used for access in older SNMP versions.'),('ICMP','Internet Control Message Protocol: carries network status and diagnostic messages.'),('Ping','A diagnostic that commonly uses ICMP echo messages to test reachability and timing.')])
add(8,[28,29,30],'DNS and DNSSEC','What problem does DNSSEC address?',
    'DNS maps names to records such as IP addresses. DNS poisoning attempts to supply false answers so users reach an unintended destination. DNSSEC adds cryptographic signatures that let a validating resolver check that DNS data came from the signed zone and was not altered. DNSSEC does not encrypt DNS queries or prove a website itself is harmless.',
    'An attacker supplies a false address for a bank name. A validating resolver rejects the answer when its signature chain does not verify.',
    'DNSSEC protects authenticity and integrity of DNS data. HTTPS separately protects the web connection when correctly validated.',
    'It helps resolvers detect forged or altered DNS answers',['It hides every DNS query from the network','It scans the destination for malware','It assigns administrator rights to domain owners'],
    [('DNS','Domain Name System: a distributed naming system that maps names to records.'),('DNS poisoning','Causing a resolver or host to use fraudulent DNS information.'),('DNSSEC','Domain Name System Security Extensions: signatures for validating DNS data authenticity and integrity.')])
add(8,[31,32,33,34],'FTP, FTPS, and secure file transfer','Why is basic FTP unsafe for sensitive transfers?',
    'Basic File Transfer Protocol does not encrypt credentials or file contents, allowing interception on the network. FTPS wraps FTP with TLS. SFTP is a different protocol carried through SSH. Active and passive FTP also differ in how the data connection is established, which affects firewall behavior.',
    'A user sends a password over basic FTP on an untrusted network. Someone capturing the traffic may read it.',
    'Similar names do not mean identical protocols. FTPS extends FTP; SFTP uses SSH and has different ports and behavior.',
    'Basic FTP transmits credentials and content without encryption',['FTP automatically signs every transferred file','FTP uses full-disk encryption for the server','FTP prevents all man-in-the-middle attacks'],
    [('FTP','File Transfer Protocol: an unencrypted file-transfer protocol.'),('FTPS','FTP protected with TLS.'),('SFTP','SSH File Transfer Protocol: file transfer through SSH, distinct from FTPS.'),('TLS','Transport Layer Security: a protocol for authenticated encrypted network communication.')])
add(8,[35,36],'Secure email and application protocols','Which secure protocols match common network activities?',
    'HTTPS protects web traffic with TLS. S/MIME can sign or encrypt email content using certificates. SRTP protects real-time audio or video. SSH provides secure remote command access and tunneling. A secure protocol still depends on valid keys, certificates, configuration, and endpoint security.',
    'An administrator uses SSH instead of Telnet so credentials and commands are not sent as readable plaintext.',
    'Encryption protects data on the connection. It cannot make a malicious server trustworthy or repair an infected endpoint by itself.',
    'HTTPS for web, SSH for remote administration, and S/MIME for protected email content',['FTP for password secrecy and HTTP for private web traffic','ICMP for email encryption and DNS for disk encryption','SNMPv1 for private file transfer'],
    [('HTTPS','HTTP protected by TLS.'),('SSH','Secure Shell: encrypted remote login and related services.'),('S/MIME','Secure/Multipurpose Internet Mail Extensions: certificate-based signing and encryption for email.'),('SRTP','Secure Real-time Transport Protocol: protection for real-time media streams.'),('NTP','Network Time Protocol: synchronizes system clocks.')])
add(8,[37,38,39,40,41],'Placement of security devices','Why does security-device placement matter?',
    'A device can inspect or block only traffic that passes through its observation or enforcement point. Sensors and collectors belong where they can see relevant traffic. Inline prevention devices need capacity and safe failure behavior. Aggregation and correlation bring several views together but do not recover traffic that was never collected.',
    'A sensor placed outside encryption termination sees encrypted bytes. A sensor after termination may inspect the application traffic, subject to privacy and access policy.',
    'Draw the traffic path first. Then place each control where its input actually crosses and where failure will not create unacceptable impact.',
    'A control needs to sit on or observe the relevant traffic path',['Every network location sees identical traffic','Placement only changes the color of a diagram','A sensor can reconstruct packets that never reached it'],
    [('Sensor','A component that observes activity and produces detections or telemetry.'),('Collector','A component that receives and stores telemetry from sources.'),('Correlation engine','A system that combines events from multiple sources to find relationships.'),('Aggregation switch','A switch that combines traffic or connections for forwarding and observation.')])
add(8,[42,43,44,45,46,47],'Security logs and centralized analysis','What do security logs contribute to an investigation?',
    'Logs record events such as authentication attempts, requests, system errors, firewall decisions, and file changes. Analysts correlate timestamps, identities, addresses, and outcomes across sources. Central collection helps search and retention but requires time synchronization, access controls, storage planning, and normalization.',
    'A firewall shows an inbound connection, an application log shows a failed login, and an audit log identifies the account action. Together they create a stronger timeline.',
    'A log entry is evidence from one system’s viewpoint. It may be incomplete, misconfigured, or use a different clock, so corroboration matters.',
    'They preserve event evidence that can be correlated into a timeline',['They prevent every logged attack automatically','They prove a failed login caused data theft','They replace the need to synchronize clocks'],
    [('Security log','A record of security-relevant events.'),('Audit log','A record intended to show who performed an action and when.'),('SIEM','Security Information and Event Management: centralized collection, search, correlation, and alerting for security data.'),('Log normalization','Converting different log formats into consistent fields for analysis.')])
add(8,[48,49,50,51,52,53,54,55],'Virtualization security','What security benefits and risks come with virtualization?',
    'Virtualization supports snapshots, isolated testing, rapid recovery, centralized management, and flexible capacity. Risks include hypervisor flaws, VM escape, weak separation, unpatched guest systems, uncontrolled VM copies, and concentration of many services on one host. Type 1 hypervisors run on hardware; Type 2 hypervisors run on a host operating system.',
    'Ten server VMs share one physical host. Efficient management improves, but a host failure or hypervisor compromise can affect several services.',
    'A VM is still a computer that needs patching, access control, monitoring, and backup. A snapshot is not automatically a complete independent backup.',
    'Virtualization improves isolation and recovery but concentrates new risks in hosts and hypervisors',['Virtual machines require no patches','A Type 2 hypervisor has no host operating system','Snapshots guarantee off-site disaster recovery'],
    [('Hypervisor','Software or firmware that creates and manages virtual machines.'),('Type 1 hypervisor','A hypervisor that runs directly on hardware.'),('Type 2 hypervisor','A hypervisor that runs as software on a host operating system.'),('VM escape','A compromise in which code breaks out of a guest’s intended isolation.'),('VDI','Virtual Desktop Infrastructure: user desktops hosted as virtual machines on servers.'),('Container','An isolated application environment sharing the host operating-system kernel.')])
add(8,[56,57,58],'Cloud models and shared security','What changes when an organization uses cloud computing?',
    'Cloud providers deliver shared computing services through models such as SaaS, PaaS, and IaaS, and deployments may be public, private, community, or hybrid. Responsibility shifts by service model, but the customer still protects its data, identities, permissions, and configurations under its control.',
    'With SaaS, the provider runs the application platform, while the customer decides which employees may access confidential records and how data is classified.',
    'Cloud means using someone else’s managed computing resources under an agreement. Physical systems still exist, and misconfiguration remains possible.',
    'Some infrastructure duties shift, while customer data, identity, and configuration duties remain',['The provider becomes responsible for every customer password choice','Cloud data no longer resides on computers','Using SaaS removes the need for access reviews'],
    [('Cloud computing','On-demand access to shared computing services over a network.'),('SaaS','Software as a Service: using a provider-managed application.'),('PaaS','Platform as a Service: using a managed platform for applications.'),('IaaS','Infrastructure as a Service: renting compute, storage, and network resources.'),('CASB','Cloud Access Security Broker: technology that applies visibility and policy between users and cloud services.')])

questions=[]
vocab=[]
checks=[]
cloze=[]
term_seen={}
for number,s in enumerate(specs,1):
    qid=f'425-q{number:02d}'
    questions.append({'id':qid,'number':number,'section':s['lecture'],'q':s['q'],'title':s['title'],
        'answer':s['answer'],'teach':s['teach'],'example':s['example'],'correct':s['correct'],
        'distractors':s['wrong'],'slides':s['slides']})
    checks.append({'id':f'425-c{number:02d}','source':number,'section':s['lecture'],
        'q':f"Which statement best applies the lesson “{s['title']}”?",'correct':s['correct'],
        'distractors':s['wrong'],'teach':s['teach'],'answer':s['correct']})
    for term,definition in s['terms']:
        key=term.lower()
        if key in term_seen: continue
        term_seen[key]=number
        wrong_defs=[]
        for candidate in [x for x in s['terms'] if x[0]!=term]:
            wrong_defs.append(candidate[1])
        generic=['A guarantee that no cyber incident can occur','A physical cable used only for power','A report that replaces all technical controls']
        wrong_defs=(wrong_defs+generic)[:3]
        vocab.append({'id':f'425-v{len(vocab)+1:03d}','term':term,'exp':'','answer':definition,'teach':s['teach'],
            'correct':definition,'distractors':wrong_defs,'source':number,'section':s['lecture'],'q':f'What does {term} mean?'})

sorts=[
 {'id':'425-s01','source':12,'section':3,'q':'Build the TCP three-way handshake order','items':['SYN','SYN-ACK','ACK'],'teach':'A client requests a connection with SYN, the server acknowledges and responds with SYN-ACK, and the client completes setup with ACK.'},
 {'id':'425-s02','source':18,'section':4,'q':'Order a safe response to an unexpected account warning','items':['Stop before using the supplied link','Open the known app or trusted address','Check the account directly','Report the suspicious message'],'teach':'Independent verification keeps the suspicious message from controlling both the warning and the verification path.'},
 {'id':'425-s03','source':22,'section':5,'q':'Order a controlled patch deployment','items':['Obtain the trusted patch','Test on representative systems','Approve and schedule deployment','Install in production','Verify and monitor'],'teach':'Testing and approval come before broad installation; verification checks that the patch and required work both function.'},
 {'id':'425-s04','source':28,'section':6,'q':'Order an investigation of a suspicious website','items':['Define the question and confirm authorization','Check passive reputation evidence','Prepare an isolated environment if needed','Observe and capture evidence','Revert or clean the environment and report findings'],'teach':'Start with the least risky evidence. Active interaction belongs in an approved isolated environment with a defined purpose.'},
 {'id':'425-s05','source':30,'section':7,'q':'Build the encryption path','items':['Plaintext','Cipher plus encryption key','Ciphertext'],'teach':'The cipher uses the key to transform readable plaintext into ciphertext.'},
 {'id':'425-s06','source':34,'section':7,'q':'Build digital-signature verification','items':['Sender hashes the message','Sender signs the digest with the private key','Receiver computes the message digest','Receiver verifies with the public key','Receiver compares the verified and computed digests'],'teach':'The signature links the private key to a digest; the receiver independently hashes the received message to check integrity.'},
 {'id':'425-s07','source':45,'section':8,'q':'Order a basic incident-log investigation','items':['Define the event and time range','Collect relevant logs','Normalize time zones and fields','Correlate events across sources','Document supported findings and gaps'],'teach':'A defined scope guides collection. Time and field normalization support correlation before conclusions are written.'},
]

cloze_specs=[
 (6,2,'An ____ alerts on suspicious traffic; an ____ can also block it.',['IDS','IPS'],['ACL','FTP']),
 (8,2,'____ summarizes connections; ____ can preserve packet contents.',['flow data','full packet capture'],['DNS','NAC']),
 (10,3,'Unsafe database command construction can enable ____; unsafe browser output can enable ____.',['SQL injection','XSS'],['DDoS','FDE']),
 (15,4,'Broad deceptive messages are ____; targeted deceptive messages are ____.',['phishing','spear phishing'],['hardening','hashing']),
 (22,5,'Give only necessary permissions through ____; reduce exposed functions through system ____.',['least privilege','hardening'],['spoofing','mining']),
 (30,7,'Readable data are ____; encrypted output is ____.',['plaintext','ciphertext'],['digest','payload']),
 (32,7,'A ____ is one-way comparison output; ____ is reversible with the appropriate key.',['hash','encryption'],['DNS','encoding']),
 (35,7,'A ____ key creates a digital signature; the matching ____ key verifies it.',['private','public'],['shared','session']),
 (40,8,'____ provides IP routing; ____ provides reliable ordered transport.',['IP','TCP'],['DNS','FTP']),
 (42,8,'____ monitors device statistics; ____ commonly tests reachability and timing.',['SNMP','ICMP'],['SFTP','HTTPS']),
 (44,8,'____ protects FTP with TLS; ____ transfers files through SSH.',['FTPS','SFTP'],['FTP','SRTP']),
 (48,8,'A Type ____ hypervisor runs on hardware; Type ____ runs on a host OS.',['1','2'],['3','4']),
]
for i,(source,section,prompt,answers,extras) in enumerate(cloze_specs,1):
    cloze.append({'id':f'425-fill{i:02d}','source':source,'section':section,'q':prompt,'correct':'; '.join(answers),
                  'distractors':['; '.join(extras),'; '.join(reversed(answers)),'; '.join(reversed(extras))],
                  'teach':questions[source-1]['teach'],'answer':'; '.join(answers),'kind':'cloze','blanks':answers})

abbreviations={
 'SCADA':'Supervisory Control and Data Acquisition','VM':'Virtual Machine','ACL':'Access Control List',
 'IDS':'Intrusion Detection System','IPS':'Intrusion Prevention System','HIPS':'Host Intrusion Prevention System',
 'PCAP':'Packet Capture','DDoS':'Distributed Denial of Service','SQL':'Structured Query Language',
 'XSS':'Cross-Site Scripting','NAC':'Network Access Control','AES':'Advanced Encryption Standard',
 'DES':'Data Encryption Standard','DSA':'Digital Signature Algorithm','FDE':'Full-Disk Encryption',
 'EFS':'Encrypting File System','TPM':'Trusted Platform Module','HSM':'Hardware Security Module',
 'P2P':'Peer-to-Peer','TCP':'Transmission Control Protocol','IP':'Internet Protocol',
 'SNMP':'Simple Network Management Protocol','ICMP':'Internet Control Message Protocol','DNS':'Domain Name System',
 'DNSSEC':'Domain Name System Security Extensions','FTP':'File Transfer Protocol','FTPS':'File Transfer Protocol Secure',
 'SFTP':'SSH File Transfer Protocol','TLS':'Transport Layer Security','HTTPS':'Hypertext Transfer Protocol Secure',
 'SSH':'Secure Shell','S/MIME':'Secure/Multipurpose Internet Mail Extensions','SRTP':'Secure Real-time Transport Protocol',
 'NTP':'Network Time Protocol','SIEM':'Security Information and Event Management','VDI':'Virtual Desktop Infrastructure',
 'SaaS':'Software as a Service','PaaS':'Platform as a Service','IaaS':'Infrastructure as a Service','CASB':'Cloud Access Security Broker'
}
for term,exp in abbreviations.items():
    existing=next((v for v in vocab if v['term'].lower()==term.lower()),None)
    if existing: existing['exp']=exp

abbr_distractors={}
all_exp=list(abbreviations.values())
for term,exp in abbreviations.items():
    # Plausible wording variants are harder than unrelated answers but remain unambiguously wrong.
    words=exp.split()
    variants=[]
    if len(words)>1: variants.append(' '.join(words[:-1]+['Service']))
    variants.extend([f'Secure {" ".join(words[1:])}' if len(words)>1 else 'Secure Network Service',
                     f'{words[0]} Network Management'])
    abbr_distractors[term]=[x for x in dict.fromkeys(variants) if x!=exp][:3]
    while len(abbr_distractors[term])<3:
        candidate=all_exp[(list(abbreviations).index(term)+len(abbr_distractors[term])+1)%len(all_exp)]
        if candidate!=exp and candidate not in abbr_distractors[term]: abbr_distractors[term].append(candidate)

data={'title':'CIS 425 Defensive Cybersecurity','module':'Lectures 1–8','sections':sections,
      'questions':questions,'vocab':vocab,'checks':checks,'sorts':sorts,'readings':[],
      'references':[],'abbreviationDistractors':abbr_distractors,'cloze':cloze,
      'sourceNotice':'All eight supplied lecture decks define the course scope. Each lesson lists its lecture and slide numbers. Explanations clarify the slide material for study; they are not an instructor-issued answer key.'}
OUT.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print(f"Built {len(questions)} lessons, {len(vocab)} terms, {len(checks)} checks, {len(cloze)} fill-ins, and {len(sorts)} sorts")

