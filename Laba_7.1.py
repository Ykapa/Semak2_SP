from PIL import Image

image = Image.open('Inosuke.jpg')
image.show()

print("Размер изображения:", image.size)
print("Формат изображения:", image.format)
print("Цветовая модель изображения:", image.mode)
