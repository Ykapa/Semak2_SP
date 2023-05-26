import json

check = True

with open('123.json','r') as file:
    data = json.load(file)

    new_product = {}
    new_product['name'] = input('Введите название товара: ')
    new_product['price'] = int(input('Введите цену товара: '))
    new_product['weight'] = int(input('Введите вес товара: '))
    new_product['available'] = bool(input('Есть ли товар в наличии (True/False): '))

    data['products'].append(new_product)

    with open('123.json', 'w') as file:
        json.dump(data, file)

with open('123.json') as json_file:
    data = json.load(json_file)
    data_sp = list(data['products'])
    for i in range(len(data_sp)):
        print('Название: ' + data_sp[i]['name'])
        print('Цена: ' + str(data_sp[i]['price']))
        print('Вес: ' + str(data_sp[i]['weight']))
        check = (data_sp[i]['available'])
        if (data_sp[i]['available']):
            print("В наличии")
        else:
            print("Нет в наличии")
        print('')



