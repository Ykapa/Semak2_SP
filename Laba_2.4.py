C1 = input("Введите цвет: ").replace(' ', '')
C2 = input("Введите цвет: ").replace(' ', '')



if (C1.lower() == "красный" or C1.lower() == "синий" or C1.lower() == "жёлтый") and (C2.lower() == "красный" or C2.lower() == "синий" or C2.lower() == "жёлтый") and C1.lower() != C2.lower():
    if ( C1.lower() == "красный" or C1.lower() == "синий")  and (C2.lower() == "красный" or C2.lower() == "синий"):
        print("Получится ФИОЛЕТОВЫЙ цвет")
    elif (C1.lower() == "синий" or C1.lower() == "жёлтый") and (C2.lower() == "синий" or C2.lower() == "жёлтый"):
        print("Получится ЗЕЛЁНЫЙ цвет")
    elif (C1.lower() == "красный" or C1.lower() == "жёлтый") and (C2.lower() == "красный" or C2.lower() == "жёлтый"):
        print("Получится ОРАНЖЕВЫЙ цвет")
else:
    print("Введён неправильный набор цветов!")
