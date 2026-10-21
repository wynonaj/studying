"""Professor examples retained in their original types and option order."""
def attach_samples(D):
 specs=[
 (1,'True/False','Cipher text is the scrambled and unreadable output of encryption.','True',None),
 (2,'True/False','Hackers these days are targeting at personal data beyond CC# and bank account# to make money.','True',None),
 (3,'True/False','SET-based attack has become more popular these days due to its stealthy penetration.','True — SET uses social engineering and deceptive pages to capture information.',None),
 (4,'True/False','The reverse shell attack is capable of defeating packet filtering firewall but not proxy firewall.','False as written — a proxy’s protection depends on its configuration and inspection.',None),
 (5,'True/False','TCP/IP represent a suite of protocols including DNS, SNMP, SMPT, POP, and FTP etc.','True, with SMTP replacing the SMPT typo.',None),
 (6,'Multiple choice','Ian recently earned his security certification and has been offered a promotion to a position that requires him to analyze and design security solutions as well as identify users’ needs. Which of these generally recognized security positions has Ian been offered?','A. Security administrator',['Security administrator','Security technician','Security officer','Security Manager']),
 (7,'Multiple choice','What is a race condition?','D. Concurrent threads access a shared resource and cause unintended consequences',['When a vulnerability is discovered and there is a race to see if it can be patched before it is exploited by attackers','When a software update is distributed prior to a vulnerability being discovered','When an attack finishes its operation before antivirus can complete its work','When two concurrent threads of execution access a shared resource simultaneously, resulting in unintended consequences']),
 (8,'Multiple choice','Which of the following is correct about Vishing?','C. VoIP makes caller ID spoofing easier',['It is a social engineering skill tailored to organizations','It tries to elicit confidential data from large organizations','VoIP makes the caller ID spoofing way too easy','It uses real persons to call all the time']),
 (9,'Multiple choice','To investigate a phishing email, where would you go for sender information?','D. Email Header',['Attachment','Embedded URL','Anti-virus','Email Header','Email Body']),
 (10,'Multiple choice','Which of the following is a static analysis tool?','C. JSUnpack',['Firebug','McAfee Advisor','JSUnpack','Norton SafeWeb','OpenSSL']),
 (11,'Multiple choice','Which of the following is responsible for data packet quality and basic security features in data transmission over computer networks?','A. TCP — reliable, ordered delivery with error detection.',['TCP','IP','UDP','HTTPS','HTTP']),
 (12,'Fill in the blank','When an IDS generates an alarm on normal traffic that is actually not malicious or suspicious, that alarm is called a(n) _____ error.','False positive',None),
 (13,'Fill in the blank','A _____ is a computer program or a part of a program that lies dormant until it is triggered by the C2 server.','Bot — receives instructions from a command-and-control server.',None),
 (14,'Fill in the blank','A _____ splits one Blockchain instance into two (hint: not by natural selection).','Hard fork',None),
 (15,'Fill in the blank','A _____ is a tool we use to check the integrity of data packet content.','Checksum',None),
 (16,'Discussion','In the discussion of OS hardening, Dr. Guo mentioned several factors that alleviate the pressure of security update implementations: network bandwidth, cloud computing, big data & analytics, and virtualization.','Explain the bottleneck each reduces: distribution, coordination, prioritization, and testing.',None),
 (17,'Discussion','What are the major types of computer viruses? What are the differences among virus, worm, scareware, adware, spyware, and backdoor?','Define each mechanism, compare propagation, and include the textbook’s program/macro and armored/mutation categories.',None),
 (18,'Discussion','How do Confidentiality, Authentication, and Obfuscation correlate in cryptographic applications?','Explain different goals and how appropriate mechanisms complement each other.',None),
 (19,'Discussion','Hash algorithms are naturally resistant to hash collisions. Why?','Qualify this as computational resistance for well-designed cryptographic hashes; collisions remain possible.',None),
 (20,'Discussion','How does Blockchain work? Pros and cons?','Connect hash commitments, validation, consensus, and tradeoffs.',None),
 (21,'Discussion','What is a bitcoin?','Explain currency, signature-authorized spending, ledger agreement, incentives, and pseudonymity.',None)]
 D['samples']=[dict(source=n,type=kind,prompt=prompt,shortAnswer=answer,options=options or [],label=D['questions'][n-1]['sample'],uncertain=D['questions'][n-1].get('uncertain',False)) for n,kind,prompt,answer,options in specs]
