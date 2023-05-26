class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name}, Кухня: {self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан сейчас открыт')

new_Restaurant = Restaurant('TOKYO CITY', 'Japanese')

print(new_Restaurant.restaurant_name)
print(new_Restaurant.cuisine_type)
new_Restaurant.describe_restaurant()
new_Restaurant.open_restaurant()