import os
from PIL import Image
import math
import glob
  
f = r"C:/Users/Nader/Desktop/image project/ماسک صورت هیدرودرم"
size = 10000
divide1 = 5
divide2 = 6
divide3 = 7
divide4 = 8
divide5 = 9
divide6 = 12

print(len(os.listdir(f)))
os.listdir(f)
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    width, height = img.size 
    if height>width:
        r = height/width
        img = img.resize((math.ceil(1724/(r*divide1)),math.ceil(1724/divide1)))
    else:
        r = width/height
        img = img.resize((math.ceil(1724/divide1),math.ceil(1724/(r*divide1))))
    img.save(f_img)

m = list(filter(lambda x: os.path.getsize(x) > size,
            [os.path.join(f, x) for x in os.listdir(f)]))
print(len(m))
for i in range(len(m)):
    f_img = f + "/" + m[i][len(f)+1:]
    img = Image.open(f_img)
    width, height = img.size
    if height>width:
        r = height/width
        img = img.resize((math.ceil(1724/(r*divide2)),math.ceil(1724/divide2)))
    else:
        r = width/height
        img = img.resize((math.ceil(1724/divide2),math.ceil(1724/(r*divide2)))) 
    img.save(f_img)
    
m = list(filter(lambda x: os.path.getsize(x) > size,
            [os.path.join(f, x) for x in os.listdir(f)]))
print(len(m))
for i in range(len(m)):
    f_img = f + "/" + m[i][len(f)+1:]
    img = Image.open(f_img)
    width, height = img.size
    if height>width:
        r = height/width
        img = img.resize((math.ceil(1724/(r*divide3)),math.ceil(1724/divide3)))
    else:
        r = width/height
        img = img.resize((math.ceil(1724/divide3),math.ceil(1724/(r*divide3))))
     
    img.save(f_img)

m = list(filter(lambda x: os.path.getsize(x) > size,
            [os.path.join(f, x) for x in os.listdir(f)]))
print(len(m))
for i in range(len(m)):
    f_img = f + "/" + m[i][len(f)+1:]
    img = Image.open(f_img)
    width, height = img.size
    if height>width:
        r = height/width
        img = img.resize((math.ceil(1724/(r*divide4)),math.ceil(1724/divide4)))
    else:
        r = width/height
        img = img.resize((math.ceil(1724/divide4),math.ceil(1724/(r*divide4))))
     
    img.save(f_img)
    
m = list(filter(lambda x: os.path.getsize(x) > size,
            [os.path.join(f, x) for x in os.listdir(f)]))
print(len(m))
for i in range(len(m)):
    f_img = f + "/" + m[i][len(f)+1:]
    img = Image.open(f_img)
    width, height = img.size
    if height>width:
        r = height/width
        img = img.resize((math.ceil(1724/(r*divide5)),math.ceil(1724/divide5)))
    else:
        r = width/height
        img = img.resize((math.ceil(1724/divide5),math.ceil(1724/(r*divide5))))
     
    img.save(f_img)

m = list(filter(lambda x: os.path.getsize(x) > size,
            [os.path.join(f, x) for x in os.listdir(f)]))
print(len(m))
for i in range(len(m)):
    f_img = f + "/" + m[i][len(f)+1:]
    img = Image.open(f_img)
    width, height = img.size
    if height>width:
        r = height/width
        img = img.resize((math.ceil(1724/(r*divide6)),math.ceil(1724/divide6)))
    else:
        r = width/height
        img = img.resize((math.ceil(1724/divide6),math.ceil(1724/(r*divide6))))
     
    img.save(f_img)
'''
for i in range(len(os.listdir(f))):
    old_name = f+"/"+os.listdir(f)[i]
    new_name = f+"/"+os.listdir(f)[i][-13:]
    os.rename(old_name, new_name)

'''
