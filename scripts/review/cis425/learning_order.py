"""A consistent beginner curriculum, explicit basic meanings, and acyclic prerequisites."""
def arrange_learning(D):
 Q=D['questions'];V=D['vocab']
 basics=[
 ('Data',42,'Information represented so a computer can store or process it.','A name, photograph, password, or saved document is data.'),
 ('Input',37,'The information supplied to a procedure or program.','When you hash a file, the file’s contents are the input.'),
 ('Output',37,'The result produced by a procedure or program.','A hash function produces a digest as its output.'),
 ('Hash comparison',37,'Computing a digest and checking whether it matches a trusted reference digest.','A changed downloaded file will normally produce a different digest than the trusted original.'),
 ('Tamper evidence',20,'Information that makes an unauthorized change detectable; it does not mean making every change impossible.','A mismatch with a trusted digest provides evidence that contents differ.'),
 ('Secret',37,'Information intentionally kept from people who are not allowed to know it.','A private signing key is a secret; a public verification key is meant to be shared.'),
 ('Key management',59,'Creating, distributing, storing, replacing, and retiring cryptographic keys securely.','Protecting the key matters as well as choosing the encryption algorithm.'),
 ('Encryption versus hashing',37,'Encryption produces ciphertext that can be decrypted with the proper key; hashing produces a digest without a decryption operation.','Encrypt a private file to hide it; compute its hash to compare its contents with a trusted copy.'),
 ]
 for i,(term,n,meaning,example) in enumerate(basics):
  v=dict(id=f'425-first-term-{i}',source=n,section=Q[n-1]['section'],term=term,exp='',q=f'What is {term}?',correct=meaning,answer=meaning,teach=meaning,example=example,distractors=['Giving every user unrestricted access.','Blocking every connection without checking its purpose.','A guarantee that every computer action is trustworthy.'])
  V.append(v)
  D['foundations'].append(dict(v,id='425-foundation-'+v['id'],foundation=True,format='mc'))
 for x in D['foundations']:
  if x['id'].startswith('425-foundation-425-first-term-'):
   alternatives=[v['answer'] for v in V if v['term']!=x['term'] and v['term'] in ['Algorithm','Plaintext','Ciphertext','Hash function','Digital signature'] and v['answer']!=x['answer']]
   x['distractors']=alternatives[:3]
 # These foundational definitions intentionally avoid relying on advanced labels.
 simple={
 'Algorithm':'A defined set of steps for doing a task. An algorithm is the procedure, not its secret settings.',
 'Cryptographic key':'A value that controls a cryptographic operation. For encryption, changing the key changes how readable information is transformed. It is data used by the procedure, not a physical keyboard key.',
 'Plaintext':'The readable information before it is encrypted, or after it is decrypted.',
 'Ciphertext':'The encrypted version of information. The matching decryption operation and key recover the readable version.',
 'Encryption':'Changing readable information into an encrypted form using a procedure and a key, to protect it from unauthorized reading.',
 'Decryption':'Recovering the readable information from its encrypted version using the appropriate procedure and key.',
 'Hash function':'A procedure that turns input information into a fixed-length result called a digest. It is not encryption and has no decryption operation.',
 'Digest':'The fixed-length result produced by a hash function: a compact summary used for comparison. It is not the original file or an encrypted copy of it.',
 'SHA-256':'One particular cryptographic hash function. Its result contains 256 bits, displayed as 64 hexadecimal characters. It does not encrypt a file.',
 'Symmetric cryptography':'Encryption in which the participants use the same shared secret key for encryption and decryption.',
 'Asymmetric cryptography':'Cryptography using a related pair of keys: a shareable public key and a secret private key. The roles of the keys depend on whether the goal is encryption or signing.',
 'Digital signature':'A value made using a private signing key that others can check using the corresponding trusted public key. It ties the signed content to that key and helps detect changes; it does not hide the message.',
 }
 for x in V+D['foundations']:
  if x['term'] in simple:
   x.update(answer=simple[x['term']],teach=simple[x['term']])
   if x.get('foundation') or not x.get('exp'):x['correct']=simple[x['term']]
 # Explicit core order prevents circular explanations such as hash -> digest -> hash.
 core=['Data','Bit','Byte','Input','Output','Algorithm','Secret','Cryptographic key','Plaintext','Ciphertext','Encryption','Decryption','Hash function','Digest','Hash comparison','Encryption versus hashing','Confidentiality','Integrity','Availability']
 lookup={x['term']:x for x in D['foundations']}
 D['basicRoute']=[lookup[t]['id'] for t in core]
 modules=[
 ('basics','1. Computers, information, and protection',[22,47,49,52,53,46,48,6,51,23,50,24]),
 ('networks','2. Networks and defensive controls',[42,77,5,11,15,25,26,12,27,66,67,78,43,79,80,81,82]),
 ('attacks','3. Attacks and social engineering',[17,7,28,29,30,8,9,69,2,68,70,44,65]),
 ('labs','4. Labs, hardening, and investigation',[35,83,84,31,3,32,4,13,33,71,72,16,34]),
 ('analysis','5. Website analysis',[36,73,74,10]),
 ('crypto','6. Keys, hashes, and cryptography',[1,37,18,38,54,55,56,57,58,59,60,61,39,62,63,64,45,19]),
 ('blockchain','7. Blockchain and Bitcoin',[20,40,75,21,41,76,14]),
 ]
 D['learningModules']=[dict(id=i,title=t,lessons=ns) for i,t,ns in modules]
 D['learningOrder']=[n for _,_,ns in modules for n in ns]
 assert len(D['learningOrder'])==84 and len(set(D['learningOrder']))==84
 # Rank all definition cards once. Edges to later definitions are omitted so the
 # graph is a DAG; the plain definition and glossary still explain each topic.
 rank={id:i for i,id in enumerate(D['basicRoute'])}
 by_lesson={n:i for i,n in enumerate(D['learningOrder'])}
 remainder=sorted([x for x in D['foundations'] if x['id'] not in rank],key=lambda x:by_lesson[x['source']])
 for x in remainder:rank[x['id']]=len(rank)
 vocab_by_id={x['id']:x for x in V}
 for x in V:
  rank[x['id']]=rank['425-foundation-'+x['id']]+0.1
 for id,deps in D['prerequisites'].items():
  if id in rank:D['prerequisites'][id]=[d for d in deps if rank.get(d,-1)<rank[id]]
 for index,id in enumerate(D['basicRoute']):D['prerequisites'][id]=D['basicRoute'][max(0,index-1):index]
 for x in D['foundations']:
  D['prerequisites'].setdefault(x['id'],[])
 for x in V:D['prerequisites'].setdefault(x['id'],['425-foundation-'+x['id']])
 # Extra application questions test the distinction instead of repeating a name.
 cases=[
 (37,'A cryptographic procedure stays the same, but its controlling secret value changes. What changed?','The key','The entire definition of an algorithm|The computer’s keyboard|The size of every possible file','The algorithm is the procedure. The key is a value supplied to it.'),
 (1,'A readable note is encrypted. What is the encrypted output called?','Ciphertext','Plaintext|The original document|A physical key','Plaintext is the readable input; ciphertext is the encrypted output.'),
 (37,'You need to recover the original readable message later. Which operation fits?','Encryption followed by decryption with the appropriate key','Hashing followed by hash decryption|Deleting the only original|An ordinary checksum used as a password','Encryption is designed to be reversed with the appropriate key. A hash is not.'),
 (37,'You hash a large file. Is the digest another copy of that file?','No; it is a fixed-length summary computed from the contents','Yes; it stores every original byte|Yes; it is always readable text from the file|Yes; it can always be decrypted to the file','A digest cannot contain a reversible copy of every arbitrarily long input.'),
 (19,'What does the 256 in SHA-256 describe?','The digest length in bits','The number of passwords in the file|The number of files allowed|The length of every input file','SHA-256 always produces a 256-bit digest, regardless of input length.'),
 (37,'A downloaded file’s digest differs from the trusted original digest. What does that show?','The contents do not match the trusted original','The sender’s identity has automatically been proved|The file was decrypted|The replacement is definitely harmless','A trusted comparison detects different contents; it does not alone explain why they differ.'),
 (37,'An attacker changes a file and replaces its posted plain hash too. Why is that a problem?','An untrusted reference hash can be replaced along with the file','A plain hash always proves the publisher’s identity|Hashes automatically stop every edit|Hashing keeps all original data secret','A reference must be trusted; an ordinary unkeyed hash is not sender authentication.'),
 (38,'Alice encrypts a message for Bob using public-key encryption. Which private key recovers it?','Bob’s private decryption key','Alice’s unrelated private signing key|Everyone’s public key|A plain packet checksum','The recipient’s public key is paired with the recipient’s private key for the encryption scheme.'),
 (18,'Alice signs a readable message without encrypting it. Is its content hidden?','No; a signature does not automatically provide secrecy','Yes; every signature encrypts the whole message|Yes; public keys are always secret|Yes; hashing means nobody can read the message','Signing and encryption protect different goals.'),
 (15,'A receiver checks an ordinary packet checksum. What is the main purpose?','Detect accidental corruption in transmission','Prove the real-world sender’s identity|Keep the packet secret|Prevent an attacker from ever recomputing a value','An ordinary checksum is an error check, not cryptographic sender authentication.'),
 ]
 for i,(n,prompt,right,wrong,why) in enumerate(cases):
  x=dict(id=f'425-first-check-{i}',source=n,section=Q[n-1]['section'],q=prompt,correct=right,distractors=wrong.split('|'),answer=why,teach=why,example=Q[n-1]['example'],format='mc')
  D['checks'].append(x);D['prerequisites'][x['id']]=list(D['basicRoute'])
 D['counts'].update(vocab=len(V),foundations=len(D['foundations']),checks=len(D['checks']))
