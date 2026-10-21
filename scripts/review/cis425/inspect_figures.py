"""Private contact sheets for reviewing source figures; never deployed."""
from pathlib import Path
from zipfile import ZipFile
from PIL import Image,ImageOps,ImageDraw
from io import BytesIO
root=Path('C:/Users/Nona/Downloads');out=Path('scripts/review/cis425/private');out.mkdir(exist_ok=True)
names=['Lab 0 (2).docx','CIS 425 - Defensive Cybersecurity.docx','Lab 2 Deliverable submission.docx','CIS 425 - Defensive Cybersecurity_ In-class assignments.docx']
for idx,name in enumerate(names):
 cells=[]
 with ZipFile(root/name) as z:
  for n in z.namelist():
   if '/media/' not in n:continue
   try:
    img=Image.open(BytesIO(z.read(n))).convert('RGB');img.thumbnail((480,310))
    tile=Image.new('RGB',(500,345),'white');tile.paste(img,((500-img.width)//2,25));ImageDraw.Draw(tile).text((8,5),n,fill='black');cells.append(tile)
   except Exception:pass
 for start in range(0,len(cells),8):
  batch=cells[start:start+8];sheet=Image.new('RGB',(1000,345*((len(batch)+1)//2)), '#dddddd')
  for i,tile in enumerate(batch):sheet.paste(tile,((i%2)*500,(i//2)*345))
  sheet.save(out/f'{idx}-{start//8}.jpg')
 print(name,len(cells),'figures')
