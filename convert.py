from PIL import Image
from fpdf import FPDF

import os

path = "file_1"

img_list = []
first = True
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if first == True:
        img_1 = Image.open(file_path)
        first = False
    else:
        img_list.append(Image.open(file_path))
pdf1_filename = "file1.pdf"
img_1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=img_list)
    


