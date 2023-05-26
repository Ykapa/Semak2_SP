from tkinter import *

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, flavors, location, open):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors
        self.location = location
        self.open = open

    def describe_rest(self):
        print(
            f'Название ресторана: {self.restaurant_name}, Кухня: {self.cuisine_type}\nРасположение ресторана: {self.location}, Часы работы ресторана {self.open} ')

    def flavors(self):
        print('Вкусы мороженного:', lst)


lst = ['Ванильное', 'Шоколадное', 'Клубничное', 'Фисташковое', 'Сливочное']

a = Restaurant('ICE&CREAM', 'Italian', lst, 'ул. Парковая 19 ', '10:00 - 22:00')

a.describe_rest()

root = Tk()
root.geometry('300x300')
root.title("Виды мороженного")
root.resizable(width=False, height=False)

frame = Frame(root, bg = 'SkyBlue')
frame.place(relx=0.1, rely = 0, relwidth = 0.8, relheight = 0.9)
title = Label(root, text = 'Меню:', bg = 'SkyBlue', font = 50)
title.place(relx=0.15, rely = -0.25, relwidth = 0.7, relheight = 0.7)

Sp = 0.1
for i in lst:
    text = i
    Sp += 0.12
    a = Label(root, text = text, bg = 'white', font = 25)
    a.place(relx=0.15, rely = Sp , relwidth = 0.7, relheight = 0.1)

root.mainloop()