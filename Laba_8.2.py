from PIL import Image

dict = {"новый год": "Dec.jpg", "8 марта": "Mar.jpg", "23 февраля": "Fev.jpg"
}

Sp = str(input("Введите название праздника: ")).lower()
img = Image.open(dict[Sp])
img.show()


