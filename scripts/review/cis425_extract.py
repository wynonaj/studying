from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import json
from pypdf import PdfReader

root=Path('C:/Users/Nona/Downloads')
out=Path('scripts/review/cis425')
out.mkdir(exist_ok=True)
names=['CIS425 Midterm Study Guide.docx','CIS425_Study_Guide.pdf','CIS 425 - Defensive Cybersecurity.docx','SET_Lab2_Presentation.pptx','Lab 2 Deliverable submission.docx','annotated-Lab%201.pdf','Keylogger_Lab1_Presentation.pptx','Lab 0 (2).docx','annotated-CIS%20425%20-%20827.pdf','CIS 425 - Defensive Cybersecurity_ In-class assignments.docx']
names.insert(2,next(p.name for p in root.glob('CompTIA*') if '(1)' in p.name))
import sys
manifest=[]
for i,name in enumerate(names,1):
    if '--rest' in sys.argv and i<=3:continue
    if name=='annotated-CIS%20425%20-%20827.pdf':name='CIS 425 - 827.pdf'
    path=root/name
    if not path.exists():
        manifest.append({'id':i,'name':name,'status':'missing'})
        continue
    units=[]
    if path.suffix=='.pdf':
        doc=PdfReader(path)
        for n,p in enumerate(doc.pages,1):
            txt=p.extract_text() or ''
            notes=[]
            for ref in p.get('/Annots',[]):
                a=ref.get_object()
                if a.get('/Contents'):notes.append(str(a['/Contents']))
            units.append({'unit':n,'text':txt,'annotations':notes})
    else:
        with ZipFile(path) as z:
            entries=['word/document.xml'] if path.suffix=='.docx' else sorted([n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')],key=lambda n:int(n.split('slide')[-1].split('.')[0]))
            for n,entry in enumerate(entries,1):
                tree=ET.fromstring(z.read(entry))
                texts=[''.join(el.itertext()) for el in tree.iter() if el.tag.rsplit('}',1)[-1]=='t']
                units.append({'unit':n,'text':'\n'.join(texts)})
            for entry in z.namelist():
                if entry.startswith('ppt/notesSlides/notesSlide') and entry.endswith('.xml'):
                    tree=ET.fromstring(z.read(entry)); units.append({'unit':entry,'text':'\n'.join(el.text or '' for el in tree.iter() if el.tag.rsplit('}',1)[-1]=='t')})
    (out/f'{i:02}.json').write_text(json.dumps(units,ensure_ascii=False,indent=2),encoding='utf-8')
    (out/f'{i:02}.txt').write_text('\n\n'.join(f'--- UNIT {u["unit"]} ---\n'+u['text']+'\n'+'\n'.join(u.get('annotations',[])) for u in units),encoding='utf-8')
    manifest.append({'id':i,'name':name,'status':'extracted','units':len(units),'chars':sum(len(u['text']) for u in units)})
if '--rest' in sys.argv and (out/'manifest.json').exists():
    old=json.loads((out/'manifest.json').read_text())
    manifest=sorted([m for m in old if m['id']<=3]+manifest,key=lambda m:m['id'])
(out/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))
