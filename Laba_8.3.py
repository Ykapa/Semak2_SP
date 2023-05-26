from PIL import Image,ImageDraw,ImageFont

Name = str(input("Введите имя получателя: "))
Title = Name + ", Поздравляю!"

img = Image.open('otkrytka.jpg')
draw = ImageDraw.Draw(img)

Nmb = int(input("Вариант вставки: "))
if Nmb == 1:
    font = ImageFont.truetype( "ComicSansMS3.ttf", 30)
    draw.text((350, 50), Title, (255, 255, 255), font=font)
    img.show()
    #img.save('otkrytka_title1.png')
if Nmb == 2:
    font = ImageFont.truetype("comicz.ttf", 50)
    draw.text((250, 2050), Title, (0, 0, 0), font=font)
    img.show()
    #img.save('otkrytka_title2.png')