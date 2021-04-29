from PIL import Image
import os
from PyPDF2 import PdfFileReader, PdfFileMerger

width_cin, height_cin =  675, 418 #cin size
size_a4 = width_a4, height_a4 = (1700, 2340)  #a4 size
margin = 10

cin = Image.open("generate/cin.png")
w, h = cin.size
hh = h - height_cin

recto = cin.crop((0,0,width_cin, height_cin))
verso = cin.crop((0, hh, width_cin, h))

# create empty images
a4 = Image.new('RGB', size_a4, color=(255, 255, 255) )
size_a4__ = width_a4__ , height_a4__ = (width_a4-2*margin  ,  height_a4-2*margin)
a4__ = Image.new('RGB', size_a4__, color=(255, 255, 255) )


# calcul paddings
num_width = int(width_a4__ / width_cin)
pad_width = int((width_a4__ - width_cin * num_width) / num_width )

num_height = int(height_a4__ / height_cin) -1
pad_height = int((height_a4__ - height_cin * num_height) / (num_height-1) )

#loops
recto__ = a4__.copy()
verso__ = a4__.copy()
x = pad_width + width_cin
y = pad_height + height_cin
for i in range(num_width):
    for j in range(num_height):
        recto__.paste(recto, (x*i, y*j))
        verso__.paste(verso, (pad_width + x*i, y*j))

#save pdfs
recto_a4 = a4.copy()
recto_a4.paste(recto__, (margin, margin))
path1 = "generate/recto_a4.pdf"
recto_a4.save(path1, "PDF")

verso_a4 = a4.copy()
verso_a4.paste(verso__, (margin, margin))
path2 = "generate/verso_a4.pdf"
verso_a4.save(path2, "PDF")


#merge pdfs
file1 = PdfFileReader(path1)
file2 = PdfFileReader(path2)
merged = PdfFileMerger()
merged.append(file1)
merged.append(file2)
with open("generate/merged.pdf", "wb") as merged_stream:
    merged.write(merged_stream)

# delete files
os.remove(path1)
os.remove(path2)








