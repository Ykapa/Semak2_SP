import json

check = True

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
