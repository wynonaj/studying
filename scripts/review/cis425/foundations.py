"""Plain-language, one-concept questions and prerequisite links for beginner practice."""
import re

def add_foundations(D):
 Q=D['questions']
 # Each entry is a separate question, rather than one bundled comparison answer.
 terms=[
 (22,'Confidentiality','Keeping information private so only permitted people or systems can read it.','A stranger reading your private medical record violates confidentiality.'),
 (22,'Integrity','Protecting information from changes that are not permitted.','Someone changing a grade without permission violates integrity.'),
 (22,'Availability','Keeping information and services accessible to authorized users when needed.','An attack that prevents students from opening the registration site harms availability.'),
 (47,'Vulnerability','A weakness in a system, setting, or procedure that could be used to cause harm.','An unpatched software flaw can provide an attacker with a way in.'),
 (25,'Choke point','A place where selected network traffic must pass, so a defender can check or control it.','An entrance with a security checkpoint is a physical analogy; a network gateway can play the same role.'),
 (25,'Visibility','The ability to observe what is happening using records from computers, accounts, and networks.','A login record shows which account signed in and when.'),
 (25,'Scalability','The ability to handle more users, devices, or traffic as demand grows.','A security service must still inspect traffic when the company doubles in size.'),
 (25,'Gateway','A device or service through which traffic passes between networks.','An office gateway handles traffic traveling between the office and the Internet.'),
 (25,'Network segmentation','Dividing a network into sections and controlling communication between them.','Separate payment computers from guest Wi-Fi and permit only necessary connections.'),
 (25,'Redundancy','Providing an additional component or path that can take over if another fails.','Two properly configured network devices can avoid losing service when one fails.'),
 (25,'Single point of failure','One component whose failure can stop an entire service.','If all access depends on one device with no backup, its failure can disconnect the office.'),
 (34,'Endpoint','An end-user or server device where programs run, such as a laptop, phone, or server.','A staff laptop is an endpoint; its records can show which program started a connection.'),
 (34,'Telemetry','Measurements and event records collected from systems for monitoring.','A computer reports a program starting and a new network connection.'),
 (34,'Log','A stored record of events, usually including times and event details.','A login log records a successful or failed sign-in.'),
 (34,'Correlation','Connecting related records to understand a sequence of events.','Match a suspicious login time with the computer’s program and connection records.'),
 (34,'Incident','An event that threatens or compromises the security of information or systems.','An attacker using a stolen account is a security incident.'),
 (34,'Containment','Limiting an incident’s spread or damage while investigation and recovery proceed.','Disconnect an affected laptop from the network under the response procedure.'),
 (34,'Process','A running instance of a computer program.','Opening a browser starts one or more processes.'),
 (34,'Administrator','An account or person with elevated rights to manage a system.','An administrator can install system software that a standard user cannot.'),
 (47,'Asset','Something valuable that an organization wants to protect.','Student records, computers, money, and a working registration service are assets.'),
 (47,'Threat','A potential cause of harm to an asset.','A criminal trying to steal student records is a threat to those records.'),
 (47,'Risk','The possibility of harm, assessed through how likely it is and how serious its impact would be.','A frequently targeted system holding sensitive records can present substantial risk.'),
 (47,'Threat actor','A person or group capable of causing harm, such as an attacker or malicious insider.','A criminal group attempting account theft is a threat actor.'),
 (47,'Attack vector','The route or method an attacker uses to reach a target.','A deceptive email attachment can be an attack vector.'),
 (47,'Attack surface','The collection of places and ways a system could be attacked.','Exposed services, accounts, and applications contribute to the attack surface.'),
 (48,'Mitigate','To reduce how likely harm is or how severe it would be; mitigation does not necessarily remove all risk.','Installing a security update reduces the risk of attacks exploiting the repaired weakness.'),
 (48,'Risk acceptance','A deliberate decision to live with an understood level of remaining risk.','The owner documents and accepts a small remaining risk after review.'),
 (48,'Risk avoidance','Stopping or declining an activity so its associated risk is not undertaken.','A business stops offering an unsafe service.'),
 (48,'Risk transfer','Shifting some consequences of risk to another party, often through insurance or a contract.','Insurance may cover some losses; it does not fix the vulnerable computer.'),
 (2,'Credit-card number (CC#)','The identifying number on a credit card; CC means credit card and # means number here.','CC# and bank account# mean credit-card number and bank-account number, not social-media hashtags.'),
 (2,'Personal data','Information relating to a person, such as a name, login, address, health record, or account information.','An attacker can sell stolen login details even without a credit-card number.'),
 (8,'Vishing','Voice phishing: deceptive phone calls or voice messages used to trick someone into revealing information or taking an action.','A caller pretending to be campus IT asks for your login code.'),
 (8,'VoIP','Voice over Internet Protocol: technology that carries voice calls over Internet-based networks.','An Internet calling service uses VoIP.'),
 (8,'Caller-ID spoofing','Making a call display a misleading caller number or name.','A fraudulent call appears to come from the university help desk.'),
 (30,'Spear phishing','A phishing attempt tailored to a particular person or group.','A message names your department and manager to appear convincing.'),
 (30,'Smishing','Phishing delivered through text messages.','A text claims your delivery failed and asks you to sign in through a deceptive link.'),
 (30,'419 scam','Advance-fee fraud that promises a larger reward after the victim pays money first.','A stranger promises an inheritance after you pay a processing fee.'),
 (30,'Social engineering','Manipulating people into revealing information or performing actions that help an attacker.','A fake support worker persuades an employee to reveal a password.'),
 (17,'Malware','Software designed to perform harmful or unauthorized actions.','A program secretly recording passwords is malware.'),
 (17,'Program virus','A virus attached to a program file that runs when the infected program runs.','Opening an infected executable activates attached malicious instructions.'),
 (17,'Macro virus','A virus that uses a document application’s macro instructions.','A malicious document activates code through its macro feature.'),
 (17,'Armored virus','A virus that makes detection or examination harder by concealing its code or resisting analysis.','Hidden or deliberately confusing instructions slow an analyst’s examination.'),
 (17,'Oligomorphic virus','A virus that chooses among a limited collection of predefined forms.','Different infections may use one of several prepared forms.'),
 (17,'Swiss cheese infection','A virus technique that distributes malicious or decoding instructions through gaps or parts of a host program.','The harmful code is spread through the host rather than kept in one obvious block.'),
 (17,'Split infection','A virus technique that separates malicious or decoding code into pieces to make analysis harder.','An analyst must connect separated pieces to understand the virus.'),
 (27,'Flow record','A summary of a network conversation, such as communicating addresses, ports, times, and byte counts; it normally does not contain the full message.','A record can show how much data a laptop sent without storing the transferred file.'),
 (27,'Full packet capture','Recording the actual bytes of observed network packets, within the sensor’s capture limits.','An analyst can inspect recorded packet headers and captured content; encrypted content stays encrypted without suitable keys.'),
 (27,'Application allowlisting','Allowing approved programs to run while restricting programs that are not approved.','An unknown downloaded executable is prevented from starting.'),
 (67,'Signature detection','Detecting activity by matching a known pattern associated with a threat.','A scanner recognizes bytes associated with known malware.'),
 (67,'Anomaly detection','Detecting behavior that differs from an expected pattern or baseline.','An employee account downloads far more records than it normally does.'),
 (67,'Baseline','A reference describing expected or normal behavior for comparison.','Usual login times and transfer sizes help identify unusual activity.'),
 (67,'Detection tuning','Adjusting detection rules or thresholds using investigated results, to reduce false alerts while still catching attacks.','Check whether a backup caused harmless alerts before changing the rule; do not silence all warnings.'),
 (67,'Business impact','The effect an event has on services, information, money, legal duties, or customer trust.','Blocking a real payment service can cost sales even when the alert was a mistake.'),
 (36,'Reputation label','A rating such as suspicious or safe based on a service’s previous observations of a website or file.','A site rated safe yesterday can be compromised today; a label is evidence, not a permanent guarantee.'),
 (73,'Manual analysis','A person directly examines evidence or controls an investigation.','An analyst reads a suspicious script and explains its behavior.'),
 (73,'Automated analysis','Software performs analysis tasks according to its rules or models.','A service scans a submitted page and reports suspicious features.'),
 (10,'JSUnpack','A tool that reveals concealed JavaScript code and URLs by unpacking scripts; it can also emulate execution.','An analyst uses it to inspect hidden instructions in a suspicious script.'),
 (10,'JavaScript','A programming language commonly used to make web pages interactive; malicious scripts can misuse browser capabilities.','A page script may handle a form or redirect the browser.'),
 (10,'Firebug','A historical browser debugging tool used to inspect and troubleshoot web pages and scripts.','An analyst could inspect page behavior with browser debugging tools.'),
 (10,'McAfee Advisor','A website reputation service associated with site-safety ratings.','A rating offers prior safety observations rather than a full explanation of a script.'),
 (10,'Norton SafeWeb','A website reputation service that reports assessments of site safety.','Its assessment can differ from another scanner because their observations differ.'),
 (10,'OpenSSL','A cryptographic software toolkit and library supporting functions such as encryption, certificates, and TLS.','It supports secure communication software; it is not a website reputation database.'),
 (37,'Cryptographic key','A value used by a cryptographic algorithm to control encryption, decryption, or another cryptographic operation.','The algorithm is the procedure; the key selects the particular transformation. Protect secret keys like sensitive access information.'),
 (37,'Hash function','A procedure that maps input data to a fixed-length digest for a specified hash algorithm.','Hashing a downloaded file allows its digest to be compared with a trusted reference.'),
 (20,'Blockchain','A ledger organized into blocks that contain cryptographic links to earlier blocks, with rules for validating and agreeing on history.','Changing an old block changes its hash links, making the change detectable.'),
 (20,'Block','A group of transactions or records plus information used to connect and validate them in a blockchain.','A Bitcoin block contains transactions and a header used in proof of work.'),
 (20,'Ledger','A record of transactions or events.','A payment ledger records who transferred value and where it went.'),
 (20,'Transaction','A record of an action such as transferring value or spending a previous payment output.','A Bitcoin transaction authorizes spending and creates new outputs.'),
 (20,'Consensus','The process by which participants agree on an accepted history under the network’s rules.','Bitcoin participants resolve competing histories using valid accumulated proof of work.'),
 (20,'Validation','Checking whether data or an action follows the required rules.','A node checks that a transaction is authorized and does not spend an already spent output.'),
 (20,'Proof of work','A mechanism requiring a search for a result that satisfies a target, while allowing others to check the result efficiently.','Bitcoin miners try candidate block headers until a hash meets the required target.'),
 (21,'Bitcoin','A peer-to-peer digital currency and network that records and validates transfers using a blockchain.','Users authorize spending with keys rather than asking a central bank to update its ledger.'),
 (21,'Miner','A participant that attempts to produce blocks using proof of work and can receive protocol rewards and fees.','A miner searches for a qualifying block-header hash.'),
 (76,'Double-spending problem','The problem of preventing the same digital funds from being spent twice in conflicting transactions.','An owner signs two payments spending the same output; both signatures may be valid, but both payments cannot be accepted together.'),
 (76,'Unspent output','A transaction output that has not yet been consumed by a valid spending transaction.','Spending an output consumes it and creates new outputs under new spending conditions.'),
 (42,'Reliable delivery','Transport that detects missing data and attempts retransmission so an application receives a complete ordered stream or a failure.','TCP retransmits missing data; this does not guarantee zero delay or secrecy.'),
 (42,'Byte stream','A sequence of bytes delivered to an application in order, without preserving the sender’s separate message boundaries.','An application using TCP defines how to separate messages within the received stream.'),
 (42,'Datagram','A separately handled message whose delivery and ordering are not automatically guaranteed by UDP.','A voice application can use UDP messages and decide how to handle missing audio.'),
 (42,'Routing','Choosing where to forward packets so they can travel toward their destination.','A router forwards an IP packet toward the destination network.'),
 (42,'Best-effort delivery','Attempting delivery without a built-in promise that every packet will arrive, arrive once, or arrive in order.','IP forwards packets, while another layer or the application handles missing data if needed.'),
 (42,'TCP handshake','The usual SYN, SYN-ACK, ACK exchange used to establish a TCP connection.','The two endpoints exchange connection information before ordinary data transfer.'),
 (42,'Port','A transport-layer number used to distinguish services or conversations on a device.','A server may listen on TCP port 443 for HTTPS connections.'),
 (42,'IP address','An address used at the network layer to identify an interface or destination for packet delivery.','Routers use destination IP information to forward packets.'),
 (56,'Stream cipher','A symmetric encryption construction that combines data with a generated sequence of key-dependent values.','The data is processed as a stream rather than only as independent fixed-size blocks.'),
 (56,'Block cipher','A symmetric encryption construction that transforms fixed-size blocks of data using a key.','AES operates on 128-bit blocks; a mode of operation handles longer messages.'),
 (56,'Sponge construction','A design that absorbs input into an internal state and then squeezes out output.','SHA-3 is based on a sponge design; SHA-256 uses a different design.'),
 (56,'One-time pad','Encryption using a truly random secret key as long as the message, shared securely and used only once.','Reusing the same pad breaks the security argument; repeating a password is not a one-time pad.'),
 (53,'Data at rest','Data stored on a device or storage service.','A saved document on a laptop is data at rest.'),
 (53,'Data in transit','Data traveling between systems or components.','A message moving from a browser to a web server is data in transit.'),
 (53,'Data in use','Data being processed by a running program.','A document open in an editor is being processed; disk encryption does not protect it from all running malware.'),
 (45,'ROT13','A substitution that moves each alphabetic letter thirteen positions; applying it twice restores the original text.','It hides text from casual viewing but is not secure encryption.'),
 (54,'XOR','A bit operation producing zero for equal input bits and one for different input bits.','1 XOR 1 is 0; 1 XOR 0 is 1.'),
 (54,'Substitution cipher','A cipher that replaces symbols with other symbols according to a rule.','Replacing each letter with the next letter is a simple substitution.'),
 (33,'Patch','A software change that repairs a defect, including a security weakness.','An operating-system update can repair a flaw used by attackers.'),
 (33,'Service','A program or function that provides a capability, often in the background or over a network.','An unused file-sharing service may create unnecessary exposure.'),
 (35,'Snapshot','A saved point-in-time state used to return a virtual machine to an earlier condition.','After a lab exercise, restore a known clean state; dependent snapshots are not automatically independent backups.'),
 (35,'NAT','Network Address Translation: changing address information as traffic crosses a boundary, often allowing guests or internal hosts to use an external connection.','A guest may reach outside through its host’s translated connection.'),
 (35,'Host and guest','The host runs virtualization software; a guest is an operating system running inside a virtual machine.','Your physical laptop is the host; the lab operating system is a guest.'),
 (51,'Security administrator','A role that analyzes and designs security solutions and identifies users’ needs in this textbook.','Ian’s design and user-needs duties match the administrator role.'),
 (51,'Security technician','A role focused on installing, configuring, and troubleshooting security technology.','A technician configures a security appliance and resolves an operational fault.'),
 (51,'Security manager','A role that supervises security personnel and coordinates security work.','A manager assigns work, manages resources, and oversees the team.'),
 (51,'CISO','Chief Information Security Officer: the executive responsible for directing the organization’s information-security program.','The CISO sets security strategy and communicates major risks to leadership.'),
 (24,'Layering','Using multiple safeguards that protect different stages or boundaries.','Filtering, restricted permissions, and monitoring protect different parts of an attack path.'),
 (24,'Limiting','Restricting access or permissions to what is necessary.','A standard employee cannot change every system setting.'),
 (24,'Diversity','Using safeguards with different failure modes so one weakness is less likely to defeat everything.','Different protective mechanisms complement each other rather than all relying on one fragile check.'),
 (24,'Obscurity','Hiding unnecessary details to make an attacker’s work harder, as a supporting measure.','Avoid revealing internal system details, while still using proper access controls.'),
 (24,'Simplicity','Keeping security understandable and manageable to reduce mistakes.','A clear, well-maintained access policy is easier to enforce correctly.'),
 (78,'Stateful firewall','A firewall that tracks connection state and uses that context when applying rules.','It can distinguish traffic belonging to an allowed connection from an unrelated incoming attempt.'),
 (78,'Packet-filtering firewall','A firewall that applies rules to packet fields such as addresses, protocols, and ports.','A rule denies traffic from a blocked source address.'),
 (78,'Application gateway','A proxy-style control that handles application communication and can enforce application-specific rules.','A web gateway can filter destinations and inspect supported web requests.'),
 (78,'Circuit gateway','A control that relays connections and evaluates connection-level information rather than fully understanding every application message.','It can control a connection without interpreting the complete content of each web request.'),
 (63,'Self-encrypting drive','A storage drive that performs encryption internally using its own hardware and key-management features.','Drive protection still depends on correct configuration and access controls.'),
 (83,'Container','An isolated application environment that commonly shares the host operating-system kernel.','Containers and full virtual machines have different isolation boundaries.'),
 (83,'VDI','Virtual Desktop Infrastructure: centrally hosted desktops accessed by users remotely.','Staff connect to managed virtual desktops instead of running the whole desktop locally.'),
 (83,'Type I hypervisor','Virtualization software that runs directly on the underlying hardware.','It manages guests without a general-purpose host operating system beneath it.'),
 (83,'Type II hypervisor','Virtualization software that runs as an application on a host operating system.','A desktop virtualization application runs guests on your laptop OS.'),
 (83,'VM sprawl','Uncontrolled growth of virtual machines that become hard to inventory, update, and manage.','An abandoned guest stays online without an owner applying patches.'),
 (84,'Cloud computing','Using remotely provided computing resources such as storage, servers, platforms, or applications.','A company uses a provider’s hosted service instead of operating every component itself.'),
 (84,'SaaS','Software as a Service: a provider operates an application that customers use.','Users access hosted email while still managing accounts, access, and their information.'),
 (84,'PaaS','Platform as a Service: a provider operates a platform on which customers deploy applications.','Developers manage their application and data while the provider manages the supplied platform.'),
 (84,'IaaS','Infrastructure as a Service: a provider supplies computing infrastructure while customers manage guest operating systems and applications.','The customer must patch its operating system in a rented virtual server.'),
 (84,'Shared responsibility','The division of security duties between a service provider and its customer.','Using the cloud does not remove the customer’s duties for accounts, data, and configuration.'),
 ]
 terms += [
 (75,'Merkle proof','A set of hashes that lets someone check that a transaction belongs under a particular Merkle root.','It proves inclusion relative to the root, not that every real-world claim in the transaction is true.'),
 (40,'Block header','A block’s control information, including commitments and fields used in proof-of-work verification.','A Bitcoin miner hashes candidate headers while searching for a qualifying result.'),
 (40,'Previous-block hash','The hash reference in a block that links it to the preceding block.','Changing earlier history changes the reference that later blocks must match.'),
 (76,'Confirmation','A transaction’s inclusion in an accepted block, with additional blocks providing further depth in the accepted history.','More accumulated valid work makes a history rewrite more costly under the system’s assumptions.'),
 (41,'Block subsidy','New bitcoin made available to a miner under the protocol’s block-reward rules.','It is distinct from the fees paid by transactions.'),
 (41,'Transaction fee','Value paid by a transaction for inclusion in a block.','Fees and the block subsidy provide incentives for block production.'),
 (17,'Trojan','Malicious software disguised as something legitimate or desirable.','A fake useful download conceals harmful functionality.'),
 (58,'DES','Data Encryption Standard: a historical symmetric block cipher with a 56-bit effective key, too small for modern protection.','Recognize it as a block cipher rather than a hash or public-key algorithm.'),
 (58,'3DES','Triple DES: a historical construction that applies DES operations three times; it is not a modern deployment choice.','It extends DES processing rather than turning DES into a signature algorithm.'),
 (58,'RC4','A historical symmetric stream cipher with weaknesses; it is not a modern secure deployment choice.','Recognize the stream-cipher category.'),
 (58,'Blowfish','A symmetric block cipher with 64-bit blocks and a variable key length.','The block size describes how much data one block contains, not the key length.'),
 (58,'Twofish','A symmetric block cipher with 128-bit blocks and keys up to 256 bits.','It is a block cipher, not a public-key exchange.'),
 (58,'IDEA','International Data Encryption Algorithm: a symmetric block cipher with 64-bit blocks and a 128-bit key.','Distinguish the size of a data block from the size of its key.'),
 (60,'ECC','Elliptic Curve Cryptography: a family of public-key techniques based on elliptic-curve mathematical problems.','ECC supports constructions for signatures and key agreement; it is not one universal encryption operation.'),
 (60,'Diffie-Hellman','A method for two parties to establish a shared secret using exchanged public information.','Authentication is also needed to avoid an attacker impersonating the parties.'),
 (60,'Key exchange','A process for establishing cryptographic key material between parties.','Two participants establish a shared secret before protecting later communication.'),
 (59,'Hybrid encryption','Combining public-key methods for establishing or protecting key material with symmetric encryption for the message data.','A secure session can use public-key authentication and efficient symmetric protection for bulk data.'),
 (62,'Downgrade attack','An attempt to make parties use a weaker security option than they otherwise would.','An attacker tries to force an older, weaker protocol choice.'),
 (62,'Brute-force attack','Trying candidate keys or passwords until one works.','A larger unpredictable secret can make exhaustive guessing impractical.'),
 (62,'Cryptanalysis','Studying a cryptographic system to find weaknesses or recover protected information without the intended secret.','An analyst investigates patterns or design weaknesses rather than possessing the proper decryption key.'),
 (64,'Latency','Delay between an action and its response.','A real-time system may need protection that stays within its response-time budget.'),
 (39,'Prime number','An integer greater than one divisible only by one and itself.','Five and eleven are prime numbers used in the small RSA teaching example.'),
 (39,'Modulo','The remainder operation after division by a positive integer.','Thirteen modulo five is three.'),
 (39,'Coprime','Two integers whose greatest common divisor is one.','Three and forty are coprime; two and forty are not.'),
 (39,'Modular inverse','A number that multiplies another number to give remainder one under a specified modulus.','Three times twenty-seven is eighty-one, which leaves remainder one modulo forty.'),
 (28,'SYN flood','An attack that sends many TCP connection requests to consume connection-handling resources.','The server may hold resources waiting for connection establishment to finish.'),
 (28,'Slowloris','An attack that keeps many web requests incomplete to occupy server connections.','It can exhaust a web server without requiring extremely high bandwidth.'),
 (28,'Bandwidth','The data-carrying capacity of a connection over time.','A large update takes less distribution time over a faster connection, all else equal.'),
 (9,'Email header','Message metadata including routing and sender-related fields used in email investigation.','Inspect full headers rather than trusting the displayed sender name alone.'),
 (9,'Return-Path','An email header field related to the envelope return address for delivery failures.','Compare it with other trusted mail evidence; it is not alone proof of the human sender.'),
 (29,'Database','An organized collection of data managed for storage and retrieval.','A student system stores records in a database.'),
 (29,'SQL','Structured Query Language: a language used to request or change data in relational databases.','Unsafe construction of a SQL command can let input become command syntax.'),
 (29,'Parameterized query','A database command that supplies values separately from the command’s structure.','A name entered by a user is treated as data rather than new SQL instructions.'),
 (29,'Output encoding','Representing data safely for its output context so it is not interpreted as executable markup or code.','Show a comment as text rather than allowing it to become browser script.'),
 (29,'WebGoat','An intentionally vulnerable training application used to learn about application security in a controlled environment.','It provides exercises for understanding and fixing flaws.'),
 (65,'Stuxnet','Malware associated with a targeted attack on industrial control equipment, used in the lecture to discuss targeted compromise and deceptive monitoring.','Monitoring that trusts compromised components can show misleading information.'),
 (68,'Website defacement','Unauthorized changes to a website’s visible content.','Replacing a company homepage with an attacker’s message harms integrity and reputation.'),
 (72,'HIPS','Host Intrusion Prevention System: software on a device that can detect and block suspicious local actions.','Host-level prevention can address actions that a network-only sensor does not observe.'),
 (79,'TLS','Transport Layer Security: a protocol supporting protected communication, including confidentiality and integrity with authentication configured appropriately.','HTTPS uses TLS to protect web communication.'),
 (79,'HTTPS','HTTP over TLS: protected communication between a web client and server.','The connection can be protected even when the endpoint itself is compromised.'),
 (79,'FTPS','FTP protected using TLS; control and data channel protection must be configured as intended.','It retains FTP’s control/data channel model.'),
 (79,'SFTP','SSH File Transfer Protocol: file transfer over an SSH connection, distinct from FTP with TLS.','It uses SSH rather than simply adding a letter to FTP.'),
 (79,'SSH','Secure Shell: a protocol for authenticated, protected remote communication.','SFTP operates over SSH.'),
 (79,'S/MIME','A standard supporting email-content signing and encryption using cryptographic certificates and keys.','Signed email is not automatically secret unless it is also encrypted.'),
 (79,'SRTP','Secure Real-time Transport Protocol: protection for real-time media traffic.','It can protect voice or video media carried by the real-time transport protocol.'),
 (79,'NTP','Network Time Protocol: synchronizing clocks across systems; ordinary NTP does not itself guarantee cryptographic protection.','Consistent times help compare events in different logs.'),
 (81,'Port mirror','A switch feature that copies selected network traffic to a monitoring destination.','A sensor sees only the traffic actually copied to it.'),
 (81,'Network tap','A device or mechanism that provides a copy of traffic on a network link for monitoring.','Place it on a link that carries the traffic needed for the investigation.'),
 (82,'Log retention','How long event records are kept before deletion or archival.','An incident from months ago may be hard to reconstruct if relevant logs were already deleted.'),
 (84,'Public cloud','Cloud resources provided for use by multiple customers under the provider’s service arrangements.','The customer still manages its own access and data responsibilities.'),
 (84,'Private cloud','Cloud infrastructure dedicated to one organization.','Dedicated use does not remove the need for hardening and monitoring.'),
 (84,'Hybrid cloud','A deployment combining distinct cloud environments with connections or integration between them.','An organization connects its private environment with a public provider.'),
 (84,'Community cloud','Cloud infrastructure shared by organizations with common requirements.','Several organizations may share requirements for mission or compliance.'),
 ]
 terms += [
 (34,'Operating system','The main software that manages a device’s resources and provides services to applications.','Windows and Linux are operating systems.'),
 (34,'Application','A program used to perform a task, such as browsing the web or editing a document.','A web browser is an application running on an operating system.'),
 (42,'Network','Connected devices that can exchange information.','Computers in an office can communicate through a local network.'),
 (42,'Protocol','Rules describing how communicating systems format and exchange information.','TCP and IP define different rules for communication.'),
 (42,'Server','A system or program that provides a service to clients.','A web server responds to requests for pages.'),
 (42,'Client','A system or program that requests a service from a server.','A browser is a web client.'),
 (42,'Bit','A binary digit with value zero or one.','A change to one bit can change a cryptographic digest.'),
 (42,'Byte','A group of eight bits.','A file’s size is often measured in bytes.'),
 (34,'Permission','A rule granting an account or program a particular allowed action.','An account may be permitted to read a file but not change it.'),
 (34,'Authorization','Deciding or enforcing which actions an identity is allowed to perform.','Verifying who signed in differs from deciding which records that account may edit.'),
 (39,'Algorithm','A defined procedure for completing a task or calculation.','Encryption uses an algorithm together with the required key.'),
 (28,'Resource exhaustion','Using up limited capacity so a system cannot serve legitimate work.','An attack occupies all available server connections.'),
 (51,'Security officer','A security role whose exact duties depend on the organization; distinguish it from the textbook’s specifically defined administrator duties.','For Ian’s design and user-needs question, the textbook answer is security administrator.'),
 ]
 existing={v['term'].casefold():v for v in D['vocab']}
 for i,(n,term,meaning,example) in enumerate(terms,1):
  if term.casefold() in existing:
   v=existing[term.casefold()];v.update(answer=meaning,teach=meaning,example=example,correct=meaning)
   continue
  q=Q[n-1]
  wrong=['A method that guarantees every attack is stopped.','A rule that gives everyone unlimited access.','A process that removes the need to investigate problems.']
  v=dict(id=f'425-basic-term-{i}',source=n,section=q['section'],term=term,exp='',q=f'What is {term}?',correct=meaning,answer=meaning,teach=meaning,example=example,distractors=wrong)
  D['vocab'].append(v);existing[term.casefold()]=v

 # Definition alternatives describe other real concepts, rather than vague advice.
 for v in D['vocab']:
  if not v['id'].startswith('425-basic-term-'):continue
  candidates=[t['answer'] for t in D['vocab'] if t['section']==v['section'] and t['term']!=v['term'] and t['answer']!=v['answer']]
  v['distractors']=list(dict.fromkeys(candidates))[:3]

 # Keep every original lesson ID and preserve original wording for reference.
 rewrites={
 26:('What is the difference between an Intrusion Detection System (IDS) and an Intrusion Prevention System (IPS)?','An IDS detects suspicious activity and alerts; an IPS can also block or interrupt suspicious activity.','IDS stands for Intrusion Detection System. IPS stands for Intrusion Prevention System. Detection raises an alert. Prevention can take action to stop activity. Both need careful rules so normal work is not mistaken for an attack.'),
 24:('Which example correctly applies the principles of layering, limiting, diversity, obscurity, and simplicity?','Use multiple safeguards, grant only needed access, vary protection methods, hide unnecessary details, and keep rules understandable.','Layering means several protective layers. Limiting means giving only necessary access. Diversity reduces reliance on one kind of protection. Obscurity hides unnecessary information but cannot replace real security. Simplicity keeps controls understandable and manageable.'),
 22:('Which protection matches confidentiality, integrity, and availability respectively?','Keep information private; prevent unauthorized changes; keep services usable by authorized people.','Confidentiality means only permitted people can see the data. Integrity means the data is not changed without permission. Availability means authorized users can get the data or service when needed.'),
 25:('How should a business use choke points, visibility, availability, and scalability when designing defenses?','Inspect traffic at controlled entry points, collect useful records, provide backup paths, and plan for growing traffic.','A choke point is a controlled place where traffic passes. Visibility means collecting evidence of activity. Availability means keeping services working. Scalability means handling growth. For example, a store checks traffic entering its network, keeps payment computers separate from other systems, records activity on staff devices, and provides a backup network device so one failure does not stop sales.'),
 27:('Which description correctly distinguishes packet capture, flow records, a proxy, and application allowlisting?','Packet capture stores packet bytes; flow records summarize connections; a proxy handles requests; allowlisting controls which programs run.','Packet capture records observed packet contents within recording limits. Flow records summarize who communicated, when, and how much. A proxy receives and forwards application requests while applying rules. Application allowlisting prevents unapproved programs from running. These are four different jobs.'),
 42:('What different jobs do TCP, UDP, and IP perform when computers communicate?','TCP delivers an ordered byte stream with recovery; UDP sends separate messages without those guarantees; IP forwards packets toward destinations.','TCP puts received bytes in order and retransmits missing data when possible. UDP sends individual messages called datagrams without automatically recovering missing messages or putting them in order. IP handles addressing and forwarding packets between networks; best effort means it does not promise delivery.'),
 43:('Which statement correctly matches DNS, SNMP, ICMP, FTP, SMTP, and POP to their jobs?','DNS looks up names; SNMP manages devices; ICMP carries network diagnostic/control messages; FTP transfers files; SMTP sends mail; POP retrieves mail.','Each protocol defines rules for a different communication task. DNSSEC adds authentication of signed DNS data, not encryption of ordinary queries. Traditional FTP does not encrypt its transfers. A protocol’s name alone does not mean its traffic is confidential.'),
 38:('Which keys protect a message for Bob and allow Bob to verify Alice’s signature?','Encrypt for Bob using Bob’s public key; Alice signs using her private key, and Bob verifies using Alice’s trusted public key.','For confidentiality, use the recipient’s public encryption key so the recipient’s private key can decrypt. For a signature, the sender uses the sender’s private signing key; others verify with the corresponding trusted public key. The private keys remain secret.'),
 40:('What separate jobs do a proof-of-work nonce, a Merkle root, and the previous-block hash perform?','The nonce is varied to search for a qualifying hash; the Merkle root summarizes the transactions; the previous-block hash links to earlier history.','A nonce is a search value. The Merkle root is computed from transaction hashes. The previous-block hash identifies the earlier block being built upon. These values support different parts of the block structure.'),
 45:('Which Chapter 3 protection best addresses a lost, powered-off laptop containing confidential files?','Full-disk encryption protects stored data when the keys remain protected.','Full-disk encryption protects data saved on the drive. It does not prevent every attack after the device is unlocked. Other Chapter 3 concepts have separate definition questions, including steganography, forward secrecy, TPM, HSM, and stream and block ciphers.'),
 47:('How do an asset, a vulnerability, a threat, and risk relate in a security decision?','A valuable resource has a weakness; something could exploit it; risk considers the likelihood and impact of the resulting harm.','An asset is something valuable. A vulnerability is a weakness. A threat is a potential cause of harm. Risk considers how likely harm is and how serious it would be. An attack vector is the route used to reach the target.'),
 48:('A business installs a patch to reduce a known security risk. Which risk response is it using?','Mitigation: reducing the likelihood or impact of harm.','Mitigate means reduce. A patch repairs a weakness, reducing the chance of a successful attack. Acceptance means knowingly living with risk; avoidance means stopping the risky activity; transfer shifts some consequences, such as through insurance.'),
 51:('Which pairing correctly matches a security role with its duties?','An administrator designs solutions and identifies users’ needs; a technician configures tools; a manager supervises the team.','In this textbook, the security administrator analyzes and designs solutions for users. A technician installs, configures, and troubleshoots tools. A manager supervises personnel. Layering, limiting, diversity, obscurity, and simplicity are separate principles, each with its own definition question.'),
 50:('Which facts help assess what a threat actor can do and why they might do it?','Their skills, money and tools, existing access, and motivation.','Capability means skills and tools. Resources include money and time. Access describes what the actor can already reach. Motivation is the reason for acting. A trusted employee and an outside criminal may have different opportunities even when both want money.'),
 53:('Which example correctly matches data at rest, in transit, and in use?','A saved file is at rest; a message crossing a network is in transit; a document being processed by a program is in use.','Different stages expose data in different places. Storage encryption protects stored data. Protected communication helps while it travels. Permissions and endpoint protection help when programs use readable data.'),
 56:('How do a stream cipher, a block cipher, a sponge construction, and a one-time pad differ?','Stream ciphers process a stream; block ciphers transform fixed-size blocks; sponge designs absorb then squeeze; a one-time pad needs a truly random key used once.','These are the four constructions in this question. A stream cipher processes data using a key-dependent stream. A block cipher operates on fixed-size blocks. A sponge absorbs input and squeezes output. A true one-time pad uses a random secret key as long as the message and never reuses it.'),
 59:('Why do secure communication systems often combine asymmetric and symmetric cryptography?','Public-key techniques help establish or protect a shared secret; symmetric encryption efficiently protects the message data.','Asymmetric methods use a public/private key pair. Symmetric encryption uses a shared secret. Combining them avoids using expensive public-key operations for every byte of a large transfer. The parties must also authenticate the exchange.'),
 58:('Which categories contain DES, 3DES, AES, RC4, Blowfish, Twofish, and IDEA?','DES, 3DES, AES, Blowfish, Twofish, and IDEA are symmetric block ciphers; RC4 is a symmetric stream cipher.','Block ciphers transform fixed-size blocks. Stream ciphers process a key-dependent stream. AES uses 128-bit blocks with 128-, 192-, or 256-bit keys. Recognizing a historical algorithm for the exam does not make it suitable for current use.'),
 60:('Which statement correctly distinguishes RSA, ECC, digital signatures, and Diffie-Hellman?','RSA and ECC support public-key constructions; signatures verify signed messages; Diffie-Hellman establishes a shared secret.','RSA and ECC are mathematical foundations for particular schemes. Signatures let a recipient verify that the trusted signing key authorized specific content. Diffie-Hellman helps establish shared key material, but the exchange also needs authentication against impersonation.'),
 62:('Which example distinguishes a downgrade attack from a weak algorithm or an implementation flaw?','A downgrade forces a weaker option; a weak algorithm has inadequate protection; an implementation flaw is a mistake in the program using it.','An attacker can exploit the selected protocol, the mathematical protection, or the code that implements it. These are different problems: choosing a good algorithm does not automatically make flawed software safe.'),
 63:('Which statement correctly distinguishes file encryption, full-disk encryption, TPM, and HSM?','File encryption protects selected files; disk encryption protects stored drive data; TPM and HSM protect particular keys and cryptographic operations.','Choose the protection according to where exposure occurs. A lost locked drive differs from a program reading an unlocked document. A protected key component does not make every application immune to attack.'),
 64:('Why must a battery-powered device consider processing time, memory, energy, and response delay when using cryptography?','Security operations consume limited resources, so the implementation must meet security requirements within the device’s operating limits.','A small device may have little memory and battery power. A time-sensitive application also needs a timely response. Use appropriate secure designs and implementations rather than assuming stronger-looking settings have no resource cost.'),
 66:('Which controls directly fit blocking an IP address, filtering website categories, and restricting unapproved programs?','Firewall or ACL rules for an IP address; a filtering proxy for websites; application allowlisting for program execution.','An IP rule evaluates traffic addresses. A web proxy handles web requests and applies site policies. Application allowlisting controls which software may run. Monitoring an event is different from blocking it.'),
 67:('A legitimate nightly backup repeatedly causes attack alerts. How should the security team adjust detection?','Investigate the backup, adjust the relevant rule carefully, and verify that actual attacks still generate alerts.','Tune detection means adjust the rules using investigated evidence. First confirm why the backup triggered the alert. Then reduce that harmless alert without disabling useful attack detection. Consider business impact: needless blocking interrupts work, but hiding genuine attacks leaves the organization exposed.'),
 73:('How do manual analysis, automated analysis, static analysis, and dynamic analysis differ?','Manual means a person does the work; automated means software does it; static avoids execution; dynamic observes execution.','These are the four labels. Manual versus automated describes who performs the analysis. Static versus dynamic describes whether the program being examined runs. A person can read code manually and statically; a tool can automatically observe it running dynamically.'),
 74:('Why can a website’s reputation label disagree with a new behavior test?','A reputation rating reflects earlier observations; the website or the conditions of the new test may have changed.','A reputation label is a service’s rating of a site based on observations such as previous scans. It is not a permanent safety guarantee. Compare when the tests ran, what each observed, and whether each reached the same content.'),
 76:('Why can two validly signed Bitcoin transactions still conflict by trying to spend the same funds?','A signature authorizes a spend; validation and consensus must also prevent the same output from being spent twice.','Double spending means trying to use the same digital funds twice. A person controlling a key can sign two conflicting transactions. A valid signature shows authorization, not that the funds remain unspent. Nodes check unspent outputs and agree on a valid history.'),
 77:('What is the usual nesting of an application message inside TCP/IP communication?','Application data is carried in a TCP segment, which is carried in an IP packet, which is carried in a link-layer frame.','Each layer adds its own control information. The IP payload can include a TCP header and TCP data. The frame carries the IP packet across a particular local link.'),
 78:('How do packet-filtering firewalls, connection-aware controls, and application gateways inspect different information?','Packet filters inspect fields such as addresses and ports; connection-aware controls consider connection context; application gateways can apply application-specific rules.','Different controls can see and enforce different things. Allowing a port does not prove the carried activity is safe. Proxy inspection and connection tracking also depend on their configured rules and visibility.'),
 79:('Which statement correctly distinguishes FTPS, SFTP, HTTPS, S/MIME, SRTP, and NTP?','FTPS protects FTP with TLS; SFTP transfers files over SSH; HTTPS protects web traffic; S/MIME protects email content; SRTP protects media; NTP synchronizes clocks.','Start with the application task, then identify its protection. FTPS and SFTP use different protocols. Ordinary NTP does not automatically provide cryptographic protection. A secure-looking name is not a substitute for checking how the service is actually configured.'),
 80:('What distinct information do DNS, SNMP, and ICMP provide to a network administrator?','DNS provides name records; SNMP provides device-management information; ICMP provides network-control and diagnostic messages.','A DNS lookup investigates name resolution. SNMP can report managed device status. ICMP messages help diagnose reachability or delivery problems. Each gives only part of the evidence; none proves every application is working correctly.'),
 81:('Why might a network sensor miss an attack occurring elsewhere in the organization?','The sensor sees only traffic that actually reaches its monitored link or copied traffic feed.','A switch mirror copies selected traffic and a tap observes a link. Neither automatically sees every device everywhere. Combine network observations with endpoint and account records where necessary.'),
 82:('How should an investigator use login, process, network, and file logs together?','Compare their times and event details to reconstruct activity, while checking missing records, clock differences, and how long evidence was kept.','Each record shows only part of the story. Matching related records helps identify what happened and which systems are affected. Missing logs or inconsistent clocks limit the conclusions.'),
 83:('How do Type I hypervisors, Type II hypervisors, containers, and VDI differ?','Type I runs on hardware; Type II runs on a host OS; containers commonly share a kernel; VDI provides remotely accessed desktops.','A hypervisor manages virtual machines. A container usually shares the host kernel rather than having the same boundary as a complete guest OS. VDI describes delivery of desktops. VM sprawl means uncontrolled growth that makes inventory and patching difficult.'),
 84:('How do SaaS, PaaS, and IaaS change what the customer manages?','SaaS supplies an application; PaaS supplies an application platform; IaaS supplies infrastructure while the customer manages guest operating systems and applications.','The service arrangement determines which duties belong to the provider or customer. Accounts, data, access choices, and configuration still require attention. Public, private, community, and hybrid describe deployment arrangements rather than these service layers.'),
 }
 for n,(prompt,right,plain) in rewrites.items():
  q=Q[n-1];q['originalPrompt']=q.get('originalPrompt',q['q']);old=q['correct']
  q.update(q=prompt,correct=right,teach=plain)
  for x in D['checks']:
   if x.get('source')==n and x.get('correct')==old:x.update(correct=right,teach=plain)
 # Explain shorthand in every displayed version while retaining the original sample.
 Q[1]['teach']='CC means credit card. The # symbol means number here: CC# means credit-card number, and bank account# means bank-account number. The statement says criminals also profit from other personal information, such as passwords, identity details, and medical records.'
 Q[1]['answer']=Q[1]['teach']+' '+Q[1]['answer']
 Q[1]['q']='Attackers target personal information beyond credit-card numbers and bank-account numbers to make money. True or false?'
 Q[24]['example']='A store checks traffic entering its network, separates payment computers from other computers, collects activity records from staff devices, and uses a backup device so one failure does not stop sales.'

 # Acronyms have both expansion questions and separate function/meaning questions.
 D['foundations']=[]
 for v in D['vocab']:
  meaning=v['answer']
  card=dict(v,id='425-foundation-'+v['id'],q=f'What is {v["term"]}'+(f' ({v["exp"]})' if v.get('exp') else '')+'?',correct=meaning,teach=meaning,answer=meaning,foundation=True,format='mc')
  candidates=[t['answer'] for t in D['vocab'] if t['term']!=v['term'] and t['section']==v['section'] and t['answer']!=meaning]
  candidates+= [t['answer'] for t in D['vocab'] if t['section']!=v['section'] and t['answer']!=meaning]
  card['distractors']=list(dict.fromkeys(candidates))[:3]
  D['foundations'].append(card)
 foundation_by_term={v['term']:f for v,f in zip(D['vocab'],D['foundations'])}
 aliases={
  'Cryptographic key':['key','keys','key use','secret key','public key','private key'],
  'Digital signature':['signature','signatures','signed','signing'],
  'Symmetric cryptography':['symmetric','symmetric key'],
  'Asymmetric cryptography':['asymmetric','public-key'],
  'Hash function':['hash','hashes','hashing'],
  'Credit-card number (CC#)':['CC#','credit-card number','bank account#'],
  'Full packet capture':['PCAP','packet capture'], 'Flow record':['flow','flow records'],
  'Endpoint':['endpoint','host','workstation'], 'Vishing':['vishing'],
  'Reputation label':['reputation','reputation label'], 'Double-spending problem':['double spending','double-spending'],
  'Network segmentation':['segments','segmentation'], 'Redundancy':['redundant','redundancy'],
  'Mitigate':['mitigate','mitigation','mitigating'],
  'Confidentiality':['confidentiality','disclosure'], 'Integrity':['integrity','alteration'],
  'Asset':['asset','assets'], 'Vulnerability':['vulnerability','vulnerabilities'],
  'Stream cipher':['stream cipher','stream ciphers'], 'Block cipher':['block cipher','block ciphers'],
  'Application allowlisting':['allowlisting','whitelisting'], 'Manual analysis':['manual'],
  'Automated analysis':['automated'], 'Static analysis':['static'], 'Dynamic analysis':['dynamic'],
  'Program virus':['program virus','file-infecting'], 'Macro virus':['macro'],
 }
 patterns=[]
 for v in D['vocab']:
  names=[v['term']]+aliases.get(v['term'],[])
  if v.get('exp'):names.append(v['exp'])
  patterns.append((v, re.compile(r'(?<![\w])(?:'+ '|'.join(re.escape(name) for name in names)+r')(?![\w])',re.I)))
 D['prerequisites']={}
 all_items=Q+D['checks']+D['trueFalse']+D['cloze']+D['sorts']+D['vocab']+D['foundations']
 for x in all_items:
  # Include the terms in options too: learners need to understand all choices.
  fields=['q','correct'] if x.get('foundation') else ['q','correct','answer','teach','example']
  text=' '.join(str(x.get(k,'')) for k in fields)
  if not x.get('foundation'):text+=' '+' '.join(x.get('distractors',[]))
  dependencies=[]
  for v,pattern in patterns:
   f=foundation_by_term[v['term']]
   if pattern.search(text) and x['id'] not in [v['id'],f['id']]:
    if v.get('exp'):dependencies.append(v['id'])
    dependencies.append(f['id'])
  D['prerequisites'][x['id']]=list(dict.fromkeys(dependencies))
 D['counts']['vocab']=len(D['vocab']);D['counts']['foundations']=len(D['foundations'])
