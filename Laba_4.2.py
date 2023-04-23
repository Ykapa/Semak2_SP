
def check():
    while True:
        try:
            n = float(input("Введите число: "))
            return(n)
        except ValueError:
            print("ValueError")

num = check()

if num == 0:
    print("ZeroDivisionError")
else:
    num = num / 100
    print(num)