import random

LST = []

for i in range(5):
    I = random.randrange(0, 9)
    LST.append(I)

Number = int(input("Попробуйте угадать число: "))

if Number in LST:
    print("Поздравляю, вы угадали число!")
else:
    print("""К сожалению вы не угадали число! В следующий раз повезёт...
Список чисел был таким: """, *LST
          )
