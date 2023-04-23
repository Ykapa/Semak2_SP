
def check():
    while True:
        n = int(input("Введите число: "))
        if n % 3 == 0:
            print("Число", n, "делится на 3")
        else:
            print("Число ", n, " не делится на 3")
        break
check()

