from PIL import Image,ImageFilter

K = ""

for i in range(1, 6):
    K = str(i) + ".jpg"
    with Image.open(K) as img:
        SM_img = img.filter(ImageFilter.SMOOTH)
        BW_img = SM_img.filter(ImageFilter.FIND_EDGES)
        BW_img.show()
        BW_img.save("BW_" + str(i) +".jpg")