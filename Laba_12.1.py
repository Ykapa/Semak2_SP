class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name}, Кухня: {self.cuisine_type}')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = flavors

    def list_flavors(self):
        print('Список вкусов мороженного: ', lst)

lst = ['Шоколадный', 'Ванильный', 'Фисташковый', 'Клубничный']

a = IceCreamStand('ICE&CREAM', 'Italian', lst)

a.describe_restaurant()
a.list_flavors()

