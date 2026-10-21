"""Read course PPTX and legacy PPT source text locally without running Office or macros."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import struct,json,hashlib
from pypdf import PdfReader
BASE=Path(__file__).parent/'private';BASE.mkdir(exist_ok=True)
DOWNLOADS=Path('C:/Users/Nona/Downloads')

class Compound:
 def __init__(self,b):
  assert b[:8]==bytes.fromhex('d0cf11e0a1b11ae1');self.b=b;self.ss=1<<struct.unpack_from('<H',b,30)[0];self.ms=1<<struct.unpack_from('<H',b,32)[0]
  dif=list(struct.unpack_from('<109I',b,76));n=struct.unpack_from('<I',b,72)[0];sec=struct.unpack_from('<I',b,68)[0]
  for _ in range(n):
   a=struct.unpack('<'+'I'*(self.ss//4),self.sector(sec));dif+=a[:-1];sec=a[-1]
  fatdata=b''.join(self.sector(s) for s in dif if s<0xfffffffa);self.fat=list(struct.unpack('<'+'I'*(len(fatdata)//4),fatdata))
  directory=self.chain(struct.unpack_from('<I',b,48)[0],self.fat)
  self.entries=[]
  for i in range(0,len(directory),128):
   d=directory[i:i+128];length=struct.unpack_from('<H',d,64)[0];name=d[:max(0,length-2)].decode('utf-16le',errors='replace')
   if d[66]:self.entries.append((name,d[66],struct.unpack_from('<I',d,116)[0],struct.unpack_from('<Q',d,120)[0]))
  root=next(e for e in self.entries if e[1]==5);self.mini=self.chain(root[2],self.fat)[:root[3]]
  mini_fat=self.chain(struct.unpack_from('<I',b,60)[0],self.fat);self.mfat=list(struct.unpack('<'+'I'*(len(mini_fat)//4),mini_fat))
 def sector(self,n):return self.b[(n+1)*self.ss:(n+2)*self.ss]
 def chain(self,start,fat,mini=False):
  result=[];seen=set();n=start
  while n<0xfffffffa and n<len(fat) and n not in seen:
   seen.add(n);result.append(self.mini[n*self.ms:(n+1)*self.ms] if mini else self.sector(n));n=fat[n]
  return b''.join(result)
 def stream(self,name):
  e=next(e for e in self.entries if e[0]==name)
  return self.chain(e[2],self.mfat if e[3]<4096 else self.fat,mini=e[3]<4096)[:e[3]]

def records(data):
 pos=0
 while pos+8<=len(data):
  vi,typ,length=struct.unpack_from('<HHI',data,pos);end=pos+8+length
  if end>len(data):break
  payload=data[pos+8:end];yield typ,vi&15,payload;pos=end
def ppt_text(data):
 result=[]
 for typ,ver,payload in records(data):
  if typ in (4000,4008,4026):
   text=payload.decode('utf-16le' if typ!=4008 else 'cp1252',errors='replace').replace('\r','\n').strip('\x00\n')
   if text:result.append(text)
  elif ver==15:result+=ppt_text(payload)
 return result
def legacy(path):
 data=Compound(path.read_bytes()).stream('PowerPoint Document');units=[];seen=set()
 def walk(data):
  for typ,ver,payload in records(data):
   if typ in (1006,1008):
    txt='\n'.join(ppt_text(payload));key=(typ,txt)
    if txt and key not in seen:seen.add(key);units.append(dict(unit=len(units)+1,type='slide' if typ==1006 else 'notes',text=txt))
   elif ver==15:walk(payload)
 walk(data)
 return units
def modern(path):
 units=[]
 with ZipFile(path) as z:
  for kind,prefix in [('slide','ppt/slides/slide'),('notes','ppt/notesSlides/notesSlide')]:
   entries=sorted([n for n in z.namelist() if n.startswith(prefix) and n.endswith('.xml')],key=lambda n:int(n[len(prefix):-4]))
   for entry in entries:
    tree=ET.fromstring(z.read(entry));paras=[]
    for p in tree.iter():
     if p.tag.rsplit('}',1)[-1]=='p':
      text=''.join(e.text or '' for e in p.iter() if e.tag.rsplit('}',1)[-1]=='t')
      if text:paras.append(text)
    units.append(dict(unit=int(entry[len(prefix):-4]),type=kind,text='\n'.join(paras)))
 return units

with ZipFile(DOWNLOADS/'PPTs_export.zip') as z:
 for name in z.namelist():
  if name.startswith('Lecture ') and name.endswith(('.ppt','.pptx')):(BASE/Path(name).name).write_bytes(z.read(name))
files={1:DOWNLOADS/'Lecture 1_Opening.pptx',2:BASE/'Lecture 2 Architecture.ppt',3:BASE/'Lecture 3 Overview of Attacks - part I.pptx',4:BASE/'Lecture 4 Overview of Attacks - part II.pptx',5:DOWNLOADS/'Lecture 5 - OS Hardening.pptx',6:DOWNLOADS/'Lecture 6 - How to determine if a website is malicious.pptx',7:DOWNLOADS/'Lecture 7_Cryptography & Cryptocurrency.ppt',8:DOWNLOADS/'Lecture 8 Sec_NWK_Admn.ppt'}
manifest=[]
for n,p in files.items():
 units=modern(p) if p.suffix=='.pptx' else legacy(p)
 (BASE/f'lecture{n}.json').write_text(json.dumps(units,ensure_ascii=False,indent=2),encoding='utf-8')
 (BASE/f'lecture{n}.txt').write_text('\n\n'.join(f'--- {u["type"]} {u["unit"]} ---\n{u["text"]}' for u in units),encoding='utf-8')
 manifest.append(dict(id=11+n,name=p.name,lecture=n,units=len(units),chars=sum(len(u['text']) for u in units),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),status='reviewed',location='PPTs_export.zip' if n in (2,3,4) else 'Downloads',method='OOXML slide and note extraction' if p.suffix=='.pptx' else 'Legacy PPT record extraction; text-bearing slide/note records deduplicated'))
 print(n,p.name,len(units),sum(len(u['text']) for u in units))
# Review the duplicate lecture-3 export too; retain a reproducible comparison.
alternate=BASE/'Lecture 3 Overview of Attacks - part I-1.pptx'
if alternate.exists():
 a=modern(alternate);b=json.loads((BASE/'lecture3.json').read_text(encoding='utf-8'))
 (BASE/'lecture3-alternate.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
 print('Lecture 3 alternate matches:',a==b)
annotation=DOWNLOADS/'annotated-CIS%20425%20-%20827.pdf'
if annotation.exists():
 doc=PdfReader(annotation);units=[]
 for n,p in enumerate(doc.pages,1):
  notes=[str(a.get_object().get('/Contents','')) for a in p.get('/Annots',[])]
  units.append(dict(unit=n,text=p.extract_text(),annotations=notes))
 (BASE/'annotated827.json').write_text(json.dumps(units,ensure_ascii=False,indent=2),encoding='utf-8')
 print('Original annotated exercise now available:',len(units),'pages')
(Path(__file__).parent/'lecture-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
