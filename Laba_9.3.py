import csv

V = 0
check = True

print("Нужно купить:")

with open("1234.csv") as file:
    file = csv.reader(file)
    for i in file:
        if check:
            check = False
        else:
            j = i[0].split(";")
            title = j[0]
            sum = j[1]
            cost = j[2]
            V = V + (int(sum) * int(cost))
            print(title + " - " + sum + " шт. за " + cost + " руб.")
print("Итоговая сумма: " + str(V) + " руб.")