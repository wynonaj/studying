from extract_lectures import files,Compound,BASE
from PIL import Image,ImageDraw
from zipfile import ZipFile
from io import BytesIO
for lecture,path in files.items():
 images=[]
 if path.suffix=='.pptx':
  with ZipFile(path) as z:blobs=[(n,z.read(n)) for n in z.namelist() if n.startswith('ppt/media/')]
 else:
  c=Compound(path.read_bytes());data=c.stream('Pictures') if any(e[0]=='Pictures' for e in c.entries) else b'';blobs=[]
  for marker,end in [(b'\x89PNG\r\n\x1a\n',b'IEND'),(b'\xff\xd8\xff',b'\xff\xd9')]:
   pos=0
   while True:
    start=data.find(marker,pos)
    if start<0:break
    stop=data.find(end,start+len(marker))
    if stop<0:break
    stop+=8 if end==b'IEND' else 2;blobs.append((str(start),data[start:stop]));pos=stop
 for name,blob in blobs:
  try:
   im=Image.open(BytesIO(blob)).convert('RGB')
   if im.width<150 or im.height<70:continue
   im.thumbnail((470,285));tile=Image.new('RGB',(490,310),'white');tile.paste(im,((490-im.width)//2,22));ImageDraw.Draw(tile).text((6,5),f'L{lecture}: {name}',fill='black');images.append(tile)
  except Exception:pass
 for start in range(0,len(images),8):
  part=images[start:start+8];out=Image.new('RGB',(980,310*((len(part)+1)//2)),'#ddd')
  for i,img in enumerate(part):out.paste(img,((i%2)*490,(i//2)*310))
  out.save(BASE/f'lecture{lecture}-figures-{start//8}.jpg')
 print('Lecture',lecture,len(images),'reviewable raster figures')
