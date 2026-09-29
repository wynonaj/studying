import json
from pathlib import Path
p=Path(__file__).resolve().parents[3]/'dist/cis304-content.json'
d=json.loads(p.read_text())
rows=[
(44,'FAIS stands for ____ ____ ____ ____.','Functional; Area; Information; System','Financial; Analysis; Information; Service|Functional; Application; Integration; Software|Financial; Area; Integration; System','FAIS = Functional Area Information System. A functional area is one department or type of work, such as accounting, human resources, or sales. An information system combines people, processes, data, and technology to handle information.','Remember: Functional Area tells you its scope—one part of the business. For example, a payroll system supports the human-resources function.'),
(44,'A FAIS primarily supports ____ in a business.','one functional area','all functions as an integrated whole|only external partner organizations|only the physical computer network','A FAIS focuses on the information needs of one business function. A function is a type of work, such as accounting or sales. A FAIS can connect to other systems, but its primary focus is still that function.','Remember: ask whose work the system mainly supports. An accounting system focused on accounting is a functional-area system; being connected to something else does not automatically change that focus.'),
(45,'In CIS 304, EIS stands for ____ ____ ____.','Enterprise; Information; System','Executive; Information; Service|Electronic; Integration; Software|Enterprise; Integration; Service','EIS = Enterprise Information System in this course. Enterprise means the organization as a whole. An EIS supports information and processes across business functions.','Remember: the E here is Enterprise. Think across departments, rather than one department’s information needs. Other contexts can use EIS differently; use your course’s meaning.'),
(45,'An EIS helps connect information and work ____.','across business functions','within one isolated functional area only|only inside a computer processor|only within the operating system','An enterprise system helps parts of the organization work together. For example, a customer order may need sales, inventory, shipping, and accounting to share consistent information.','Remember: sales records the order, inventory checks availability, shipping delivers it, and accounting tracks payment. The key idea is supporting that cross-functional flow.')
]
d['foundations']=[]
for i,(n,q,a,w,intro,why) in enumerate(rows,1):
 d['foundations'].append(dict(id=f'304-foundation-{i}',source=n,section=4,kind='cloze',foundation=True,foundationIntro=intro,q=q,correct=a,answer=a,distractors=w.split('|'),blanks=a.split('; '),teach=why,example=intro))
# Keep these as ordinary cloze practice, not a prerequisite interruption.
for card in d.pop('foundations'):
 card['teach']=card.pop('foundationIntro')+'\n\n'+card['teach']
 card.pop('foundation',None)
 d['cloze'].append(card)
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
