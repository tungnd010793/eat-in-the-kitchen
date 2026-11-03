#!/bin/bash
# QC một lô cụm vừa về: whisper + nghe lại theo đoạn (qc_lan.py), rồi ghép tấm khung hình các cụm thành qc/_xem_lo.jpg
D=/f/Tungnd/phim/EAT_IN_THE_KITCHEN
cd $D/_zh/cong_cu && python -X utf8 qc_lan.py "$@" 2>&1 | grep "^cụm"
cd $D && python -X utf8 -c "
import sys
from PIL import Image,ImageDraw,ImageFont
ns=[int(x) for x in sys.argv[1:]]; ims=[Image.open(f'qc/cum_{n:03d}.jpg').convert('RGB') for n in ns]
w=ims[0].width; h=sum(i.height+26 for i in ims); t=Image.new('RGB',(w,h),'white'); d=ImageDraw.Draw(t); f=ImageFont.truetype('arial.ttf',20); y=0
for n,i in zip(ns,ims): d.text((6,y+2),f'cum {n}',fill='black',font=f); t.paste(i,(0,y+26)); y+=i.height+26
t.save('qc/_xem_lo.jpg',quality=85)" "$@"
