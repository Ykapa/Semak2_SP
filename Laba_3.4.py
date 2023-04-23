import random
E = 0
F = 0

while True:
    A = str(random.randrange(10, 99))
    B = str(random.randrange(10, 99))
    C = int(A) + int(B)
    D = input(A + " + " + B + " = ")
    if int(C) == int(D):
        F += 1
    else:
        E += 1

    if E == 3:
        F = str(F)
        print("Игра окончена. Правильных ответов: " + F)
        break