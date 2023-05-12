from PIL import Image

image = Image.open('Inosuke.jpg')
image = image.reduce(3)

S = str(input("Как отзеркалить? ")).upper()
if "ГОР" in S:
    out = image.transpose(Image.FLIP_TOP_BOTTOM)
    out.show()
    out.save("Inosuke_Gor.jpg")
elif "ВЕР" in S:
    out = image.transpose(Image.FLIP_LEFT_RIGHT)
    out.show()
    out.save("Inosuke_Ver.jpg")


