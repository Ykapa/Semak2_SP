import os
from PIL import Image,ImageFilter

os.mkdir("Pictures")

for i in os.listdir("Pic"):
    if i.endswith(".jpg") or i.endswith(".png"):
        img = Image.open(str(i))
        SM_img = img.filter(ImageFilter.SMOOTH)
        BW_img = SM_img.filter(ImageFilter.FIND_EDGES)
        BW_img.show()
        #BW_img.save(r"C:\Users\159950\PycharmProjects\Semak_Laba9\Pictures\img" + str(i) +".jpg")