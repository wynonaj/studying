"""Who starts a process, when it runs, and what each party does next."""
from copy import deepcopy

def add_timelines(D):
 hash_source=next(x for x in D['orientation'] if x['id']=='425-context-23')
 meaning='A calculated sequence of bits, usually displayed as letters and numbers, produced from particular data such as a file’s contents. It is also called a digest.'
 definition=deepcopy(hash_source)
 definition.update(id='425-introduction-hash-value',q='What is a hash value?',correct=meaning,distractors=['A randomly chosen name with no relationship to the contents.','An encrypted copy that always contains every original byte.','A guarantee that no other possible input can have the same result.'],teach='A program reads the supplied contents and applies a specified hash calculation. The displayed letters and numbers represent that calculation’s result. The same method and exactly the same bytes give the same result. It is not a random choice, and uniqueness is not guaranteed.',answer=meaning,example='A publisher computes a value for its original file. Your computer computes a value for your downloaded copy. You compare those two values to check the contents.',term='Hash value')
 position=next(i for i,x in enumerate(D['orientation']) if x['id']=='425-introduction-hash')
 D['orientation'].insert(position,definition)
 D['prerequisites'][definition['id']]=[]
 v=deepcopy(definition);v.update(id='425-term-hash-value',orientation=False,foundation=False,exp='')
 v['setting']=dict(D['practicalContexts']['hash'],example=definition['example']);v['contextKey']='hash';v['topicIntroId']=D['questions'][36]['topicIntroId']
 f=deepcopy(v);f.update(id='425-foundation-hash-value',foundation=True)
 D['vocab'].append(v);D['foundations'].append(f)
 digest=next(x for x in D['foundations'] if x['term']=='Digest')
 D['prerequisites'][v['id']]=[f['id']]
 D['prerequisites'][f['id']]=[digest['id']]
 index=D['basicRoute'].index(digest['id'])+1
 D['basicRoute'].insert(index,f['id'])
 if index+1<len(D['basicRoute']):D['prerequisites'][D['basicRoute'][index+1]]=[f['id']]
 hash_timeline=[
  dict(when='Before the download is offered',who='Software publisher',event='Finalizes the original release file. The file’s exact bytes are the contents that recipients should obtain.'),
  dict(when='Before or when the release is published',who='Publisher’s hash program',event='Reads the original file and computes a reference hash using a named method such as SHA-256. The publisher makes that reference available through a trusted release channel.'),
  dict(when='You download the release',who='Your browser or download tool',event='Transfers the file to your computer. A download by itself does not imply that a separate reference-hash comparison has happened.'),
  dict(when='You or a configured verification tool initiates checking',who='Your computer’s hash program',event='Reads the downloaded file’s bytes and computes its hash using the same method as the publisher. It is not comparing the file with itself.'),
  dict(when='Both values are available',who='You or the verification program',event='Compares your computed value with the trusted reference value for that exact release. A different version of the legitimate file needs its own reference.'),
  dict(when='The values differ',who='Person or system deciding whether to use the file',event='Treats the contents as different from the trusted original and investigates or obtains the correct file. The mismatch does not explain whether the cause was corruption, a legitimate edit, or malicious alteration.'),
  dict(when='The values match',who='Person or verification program',event='Has evidence supporting a content match under the hash’s security assumptions. The match alone is not a guarantee that the file is harmless, or proof of its publisher if the reference was untrusted.'),
  dict(when='Checking for later changes instead of checking a download',who='A file-integrity monitoring system or administrator',event='Keeps a trusted earlier baseline, recalculates the file’s hash later, and compares the new value with that earlier reference. This is a second scenario; not every system performs it automatically.'),
 ]
 encryption_timeline=[
  dict(when='Before protecting the report',who='User or system policy',event='Identifies the file and who should be allowed to read it, then selects an appropriate encryption feature.'),
  dict(when='Encryption is requested or automatically required by that feature',who='Encryption software or protected hardware',event='Obtains the required key material and transforms the readable file data into ciphertext. Where the key is generated, stored, or unlocked depends on the system.'),
  dict(when='Saving or sending the protected data',who='The application',event='Stores or transmits the encrypted representation and handles keys according to its design. A separate unprotected original must also be considered.'),
  dict(when='An authorized person later opens the information',who='The authorized application',event='Uses the appropriate decryption procedure and key to recover readable contents. A running application may now have plaintext in memory, which needs its own access protection.'),
 ]
 signature_timeline=[
  dict(when='The document is ready for approval',who='Sender',event='Selects the exact content to sign and uses the private signing key through signing software.'),
  dict(when='The signed document is sent',who='Sender’s application',event='Supplies the document and signature. Signing alone has not hidden the contents.'),
  dict(when='The recipient needs to rely on the document',who='Recipient’s verification software',event='Checks the received content and signature using a trusted corresponding public key.'),
  dict(when='Verification returns a result',who='Recipient',event='Uses pass or fail as evidence about the signed content and key. The decision still depends on trust in the key, custody of the private key, and the task’s requirements.'),
 ]
 network_timeline=[
  dict(when='Before communication',who='Administrator',event='Configures the relevant routing, access, monitoring, or application policy.'),
  dict(when='A client requests communication',who='Client and network equipment',event='Process the connection or packets using the selected protocols and configured rules.'),
  dict(when='The control or service handles the request',who='Relevant network or application component',event='Produces the result described below, such as delivered data, a response, an allow/deny decision, or an observation record.'),
  dict(when='The result must be used or investigated',who='Receiving application or administrator',event='Uses the returned data or reviews the recorded evidence. The exact follow-up depends on this question’s service or control.'),
 ]
 detection_timeline=[
  dict(when='Before an alert',who='Security team',event='Configures detection or prevention rules and ensures the sensor receives the activity it needs to observe.'),
  dict(when='Relevant activity occurs',who='Sensor or endpoint security software',event='Observes the event and evaluates the applicable rule or baseline.'),
  dict(when='A rule flags the activity',who='Detection or prevention system',event='Produces an alert; a prevention system may also block activity. The alert is not yet proof that the event was malicious.'),
  dict(when='The alert is reviewed',who='Security analyst',event='Checks related evidence, decides whether it was a true threat or a false alert, and chooses a response. Findings may lead to careful rule tuning.'),
 ]
 for pool in ['questions','checks','vocab','foundations','orientation','topicOrientation','trueFalse','cloze','sorts','discussions']:
  for x in D[pool]:
   n=x.get('number',x.get('source'));term=x.get('term','').lower();flow=x['walkthrough']
   # Default chronology uses the exact authored starting point, operation,
   # result, and follow-up for this concept rather than inventing automation.
   actor='The person or program performing this task'
   if n in [6,51]:actor='The organization assigning security responsibilities'
   elif n in [22,23,24,25,46,47,48,49,50,52,84]:actor='The organization’s responsible staff'
   elif n in [8,30,68,70]:actor='The recipient and the person investigating the request'
   elif n in [17,28,29,32,65]:actor='The affected application or device, followed by defenders'
   x['timeline']=[
    dict(when='At the start of this scenario',who=actor,event=flow['starting']),
    dict(when='The relevant operation is initiated or the described event occurs',who=actor,event=flow['operation']),
    dict(when='That operation or event produces its result',who=actor,event=flow['result']),
    dict(when='A decision or follow-up action is needed',who=actor,event=flow['use']),
   ]
   if 'trusted reference' in flow['use'] and ('digest' in flow['result'] or term=='hash value'):
    x['timeline']=deepcopy(hash_timeline)
   elif any(word in term for word in ['hash','digest','sha-256']) or x['id'] in ['425-context-'+str(i) for i in range(21,28)]:x['timeline']=deepcopy(hash_timeline)
   elif 'ciphertext' in flow['result'] and n not in [37,39]:x['timeline']=deepcopy(encryption_timeline)
   elif 'signature' in term or n==61:x['timeline']=deepcopy(signature_timeline)
   elif n in [12,26,67] or term in ['ids','ips','edr']:x['timeline']=deepcopy(detection_timeline)
   elif n in [5,11,42,43,66,77,78,79,80]:
    x['timeline']=deepcopy(network_timeline)
    x['timeline'][2]['event']=flow['result'];x['timeline'][3]['event']=flow['use']
 # Simple chronological checks directly test when and why the comparison runs.
 checks=[
 ('reference','Before recipients can check a release against its original contents, what reference can the publisher provide?','A hash computed from the exact original release file using a named method.','A random value unrelated to the file.|Only the color of the download button.|A claim that filenames can never be copied.','The reference represents the publisher’s particular release contents. Recipients must obtain it through a trusted channel.'),
 ('start','Does downloading any file automatically mean your computer has compared its hash with a trusted publisher reference?','No; a user or configured verification process must perform that comparison.','Yes; every browser always does this separately for every download.|Yes; saving a filename is the same operation.|Yes; the file chooses its own trusted publisher.','Some tools automate checks, but the mere fact that a download completed does not establish that this particular comparison happened.'),
 ('two','Which two values are compared in the publisher-reference download scenario?','Your computed hash of the download and the trusted hash of the exact original release.','The downloaded file’s name and your account password.|A file’s hash and that same hash copied into a second box.|Two values chosen randomly after downloading.','The useful comparison is against a trusted reference for the desired contents, not against the downloaded file’s own value repeated twice.'),
 ('later','An administrator wants to detect changes to a configuration file over time. What should be compared?','A newly calculated hash and a trusted earlier baseline for that file.','Only the file with itself at the same instant.|Only two copies of the current filename.|A new hash with an unrelated random number.','This is a later-change monitoring scenario. The baseline must be protected, and authorized changes may require establishing an approved new baseline.'),
 ('deterministic','Two computers use the same hash method on exactly the same bytes. What should happen?','They calculate the same hash value.','They deliberately choose different random values.|The file must automatically become encrypted.|One computer must reveal a private signing key.','The result is determined by the input and method. Its appearance can look random, but the procedure does not choose a new random identifier each time.'),
 ]
 for name,q,right,wrong,why in checks:
  x=deepcopy(hash_source);x.update(id='425-timeline-check-'+name,q=q,correct=right,distractors=wrong.split('|'),answer=why,teach=why,example=why,timeline=deepcopy(hash_timeline))
  position=next(i for i,card in enumerate(D['orientation']) if card['id']=='425-context-24')
  D['orientation'].insert(position,x);D['prerequisites'][x['id']]=[]
 D['hashTimeline']=hash_timeline
 D['counts'].update(vocab=len(D['vocab']),foundations=len(D['foundations']),orientation=len(D['orientation']))
