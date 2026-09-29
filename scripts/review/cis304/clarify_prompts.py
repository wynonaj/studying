import json
from pathlib import Path
p=Path(__file__).resolve().parents[3]/'dist/cis304-content.json'
d=json.loads(p.read_text())
clarified={
24:'What do Business Process Management (BPM), Business Process Improvement (BPI), and Business Process Re-engineering (BPR) have in common?',
25:'How do Business Process Management (BPM), Business Process Improvement (BPI), and Business Process Re-engineering (BPR) differ?',
26:'What is the major trade-off between Business Process Improvement (BPI) and Business Process Re-engineering (BPR)?',
46:'What is the difference between a Functional Area Information System (FAIS) and an Enterprise Information System (EIS)?',
48:'How does an Enterprise Resource Planning (ERP) system help a business organization?'
}
for q in d['questions']:
 if q['number'] in clarified:
  q['originalPrompt']=q.get('originalPrompt',q['q'])
  q['q']=clarified[q['number']]
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
