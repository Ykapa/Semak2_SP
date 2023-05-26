from PIL import Image

img = Image.open('otkrytka.jpg')

img_crop = img.crop((80,100,900,400))
img_crop.show()
#img_crop.save('otkrytka_crop.jpg')



