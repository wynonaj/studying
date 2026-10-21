"""Introduce basic terms before use and expand abbreviations in explanatory prose."""
import re

def clarify_language(D):
 definitions=[
 ('encryption',1,'What is encryption?','Changing readable information into a protected form so people without permission cannot readily read it.','Changing only the name of a file|Deleting every copy of the information|Making the computer physically larger','Encryption is a calculation performed by software or hardware on information, such as a report’s contents. It protects confidentiality: who can read the information.'),
 ('algorithm',37,'What is an algorithm?','A defined set of steps for performing a task.','The physical keyboard|The person who owns a file|The name printed on the laptop','A computer program follows instructions. An algorithm describes the procedure those instructions implement, such as the calculation used for encryption.'),
 ('key',37,'What is a cryptographic key?','A digital value used by a cryptographic procedure to control its operation.','A physical key on the keyboard|The name of the person who wrote a report|A guarantee that a file is harmless','In encryption, the key is data supplied to the encryption procedure. It controls the particular transformation of the information. The key is distinct from the procedure itself and is not necessarily the user’s password.'),
 ('decryption',1,'What is decryption?','Recovering readable information from its encrypted version using the appropriate procedure and key.','Changing only the file’s icon|Finding out who bought the laptop|Automatically repairing a broken hard drive','An authorized application can decrypt protected contents to make them readable again. Encryption transforms readable contents into a protected form; decryption recovers them.'),
 ('hash',37,'What is a hash function?','A procedure that computes a fixed-length summary from supplied information.','A procedure that always hides the original file|A physical lock on the computer|A way to increase a file’s storage space','A hash program reads information, such as the contents of a downloaded file, and calculates a result called a digest. Computing that result does not encrypt the original file.'),
 ('digest',37,'What is a digest in hashing?','The fixed-length computed result of a hash function.','A full encrypted copy of every original byte|The computer’s physical storage drive|The person who downloaded the file','A digest is a compact calculated summary. Comparing it with a trusted reference helps check contents. It is not the file itself and is not decrypted to recover that file.'),
 ]
 cards={}
 for name,n,q,right,wrong,why in definitions:
  id='425-introduction-'+name
  cards[name]=dict(id=id,source=n,section=D['questions'][n-1]['section'],q=q,correct=right,distractors=wrong.split('|'),answer=why,teach=why,example=why,foundation=True,orientation=True,format='mc',context='A student is protecting the contents of a report saved on a laptop. A separate task is checking whether a downloaded file matches a trusted original.')
  D['prerequisites'][id]=[]
 # The existing concrete story stays intact. Basic definitions are inserted
 # before the first question that relies on each technical operation.
 ordered=[]
 for x in D['orientation']:
  if x['id']=='425-context-5':ordered.extend(cards[t] for t in ['encryption','algorithm','key','decryption'])
  if x['id']=='425-context-21':ordered.extend(cards[t] for t in ['hash','digest'])
  ordered.append(x)
 D['orientation']=ordered
 expansions={v['term']:v['exp'] for v in D['vocab'] if v.get('exp')}
 expansions.update({
 'TLS':'Transport Layer Security','SSL':'Secure Sockets Layer','HTTPS':'Hypertext Transfer Protocol Secure','HTTP':'Hypertext Transfer Protocol',
 'TCP/IP':'Transmission Control Protocol / Internet Protocol','TCP':'Transmission Control Protocol','IP':'Internet Protocol',
 'UDP':'User Datagram Protocol','DNSSEC':'Domain Name System Security Extensions','SQL':'Structured Query Language',
 'HIPS':'Host Intrusion Prevention System','HIDS':'Host Intrusion Detection System','NIDS':'Network Intrusion Detection System',
 'FTPS':'File Transfer Protocol over Transport Layer Security','SFTP':'Secure Shell File Transfer Protocol','SSH':'Secure Shell',
 'SRTP':'Secure Real-time Transport Protocol','S/MIME':'Secure/Multipurpose Internet Mail Extensions',
 'NTP':'Network Time Protocol','NTS':'Network Time Security','ACL':'Access Control List','URL':'Uniform Resource Locator',
 'OS':'Operating System','CPU':'Central Processing Unit','RAM':'Random Access Memory','GUI':'Graphical User Interface',
 'USB':'Universal Serial Bus','API':'Application Programming Interface','HTML':'Hypertext Markup Language',
 'VoIP':'Voice over Internet Protocol','ECC':'Elliptic Curve Cryptography','TPM':'Trusted Platform Module','HSM':'Hardware Security Module',
 'VDI':'Virtual Desktop Infrastructure','NAT':'Network Address Translation','CASB':'Cloud Access Security Broker',
 'SaaS':'Software as a Service','PaaS':'Platform as a Service','IaaS':'Infrastructure as a Service',
 'CISO':'Chief Information Security Officer','APT':'Advanced Persistent Threat','DoS':'Denial of Service',
 'SHA-256':'Secure Hash Algorithm with a 256-bit digest','FIDO':'Fast IDentity Online','IT':'Information Technology',
 })
 D['abbreviationExpansions']=expansions
 pattern=re.compile(r'(?<![\w])('+ '|'.join(re.escape(k) for k in sorted(expansions,key=len,reverse=True))+r')(?![\w])')
 def expand(s):
  def replace(m):
   full=expansions[m[0]]
   return m[0] if s[m.end():].startswith(' ('+full+')') else m[0]+' ('+full+')'
  return pattern.sub(replace,s)
 fields={'answer','teach','example','object','location','purpose','action','meaning','context','intro','goal','shortAnswer'}
 def walk(value):
  if isinstance(value,list):
   for item in value:walk(item)
  elif isinstance(value,dict):
   for k,v in list(value.items()):
    if k in fields and isinstance(v,str):value[k]=expand(v)
    elif isinstance(v,(dict,list)):walk(v)
 walk(D)
 D['counts']['orientation']=len(D['orientation'])
