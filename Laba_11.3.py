class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating_restaurant):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating_restaurant = rating_restaurant

    def describe_restaurant(self):
        print(
            f'Название ресторана: {self.restaurant_name}, Кухня: {self.cuisine_type}, Рейтинг ресторана: {self.rating_restaurant}')

    def open_restaurant(self):
        print('Ресторан сейчас открыт')

    def rate_restaurant(self):
        rating = input("Введите новый рейтинг: ")
        print(f'Новый рейтинг ресторана: {rating}')
        return rating

new_Restaurant = Restaurant('TOKYO CITY', 'Japanese', "7")

new_Restaurant.describe_restaurant()
new_Restaurant.open_restaurant()

rating = new_Restaurant.rate_restaurant()
new_Restaurant = Restaurant('TOKYO CITY', 'Japanese', rating)

new_Restaurant.describe_restaurant()