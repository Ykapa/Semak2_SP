class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name}, Кухня: {self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан сейчас открыт')

new_Restaurant = Restaurant('TOKYO CITY', 'Japanese')

new_Restaurant2 = Restaurant('Wan Li', 'Chinese')

new_Restaurant3 = Restaurant('Farmstead', 'Russian')

new_Restaurant.describe_restaurant()
new_Restaurant2.describe_restaurant()
new_Restaurant3.describe_restaurant()