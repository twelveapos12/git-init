from PIL import Image
import pixelate
import random
import subprocess
#!/usr/local/bin/python3

from PIL import Image
img = Image.open("original/textura.png")

rmd = random.randint(1,100)


imgSmall = img.resize((32,32),resample=Image.BILINEAR)



result = imgSmall.resize(img.size,Image.NEAREST)
name = str(rmd) + ".png"



result.save(name)
subprocess.call(['./move.sh'])
