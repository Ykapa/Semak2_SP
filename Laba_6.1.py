dict_1 = {"США": "Вашингтон", "Швеция": "Стокгольм", "Япония": "Токио", "Россия": "Москва", "Канада": "Оттава"}
dict_2 = {}
for key, value in dict_1.items():
    print(key, value)

K = str(input("\nСтрана: "))
if dict_1.get(K):
    print(dict_1[K], "\n")
else:
    print("Страны нет в словаре!\n")

LST = sorted(dict_1.items())
for i in range(0, len(LST)):
    dict_2.update({LST[i][0]: LST[i][1]})
for key, value in dict_2.items():
    print(key, value)


