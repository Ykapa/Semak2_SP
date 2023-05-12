from PIL import Image

img = Image.open('Anime.jpg')
img2 = Image.open('WTF.jpg')

img2 = img2.reduce(5)
img.paste(img2)

img.save("Anime_WTF.jpg")