import zipfile,xml.etree.ElementTree as E,posixpath,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];out={};ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
for ch in [1,2,3,10]:
 z=zipfile.ZipFile(f'/Users/wynonajaner/Downloads/Schwalbe Ch {ch} Slides.pptx');ss=[]
 for n in sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+.xml$',n)],key=lambda n:int(re.search(r'(\d+)\.xml',n)[1])):
  num=int(re.search(r'(\d+)\.xml',n)[1]);s={'slide':num,'text':'\n'.join(''.join(t.text or '' for t in p.findall('.//a:t',ns)) for p in E.fromstring(z.read(n)).findall('.//a:p',ns)).strip(),'diagram':'','notes':'','images':[]}
  rel=f'ppt/slides/_rels/slide{num}.xml.rels'
  if rel in z.namelist():
   for r in E.fromstring(z.read(rel)):
    if r.attrib.get('TargetMode')=='External':continue
    target=posixpath.normpath('ppt/slides/'+r.attrib['Target']);typ=r.attrib['Type'].split('/')[-1]
    if typ=='image' and Path(target).suffix.lower() in ['.png','.jpg','.jpeg','.gif','.svg']:
     name=f'ch{ch}-{Path(target).name}';p=ROOT/'dist/cis464-media'/name;p.write_bytes(z.read(target));s['images'].append('cis464-media/'+name)
    if typ in ['notesSlide','diagramData']:
     s['notes' if typ=='notesSlide' else 'diagram']+='\n'.join(t.text or '' for t in E.fromstring(z.read(target)).findall('.//a:t',ns))
  ss.append(s)
 out[ch]=ss
(ROOT/'dist/cis464-slides.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
for ch,ss in out.items():
 print(ch,len(ss))
 for s in ss:
  if (ch==1 and s['slide'] in [44,46,55,67,71,72]) or (ch==2 and s['slide'] in [29]) or(ch==3 and s['slide'] in [25]):print(s['slide'],s['images'])
