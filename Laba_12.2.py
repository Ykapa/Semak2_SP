class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name}, Кухня: {self.cuisine_type}')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, open):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = flavors
        self.location = location
        self.open = open

    def list_flavors(self):
        print('Список сортов мороженного: ', lst)

    def describe_rest(self):
        print(f'Расположение ресторана: {self.location}, Часы работы ресторана {self.open}')

    def add_flavors(self):
        lst.append(input('Какие вкусы добавить? '))

    def del_flavors(self):
        lst.remove(input('Какие вкусы убрать? '))

    def check(self):
        if str(input('Наличие какого вкуса узнать? ')) in lst:
            print('Такой есть')
        else:
            print('Такого нет')

    class Cup_ice_cream:
        def __init__(self, name, flavors):

            self.name = name
            self.flavors = flavors

    class Horn_ice_cream:
        def __init__(self, name, flavors):

            self.name = name
            self.flavors = flavors

    class Briquette_ice_cream:
        def __init__(self, name, flavors):

            self.name = name
            self.flavors = flavors

lst = ['Ванильное', 'Шоколадное', 'Клубничное', 'Фисташковое', 'Сливочное']

a = IceCreamStand('ICE&CREAM', 'Italian', lst, 'ул. Парковая 19 ', '10:00 - 22:00')

a.describe_restaurant()
a.describe_rest()
a.list_flavors()
a.add_flavors()
a.del_flavors()
a.check()