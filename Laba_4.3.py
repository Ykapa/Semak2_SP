
def mag_date():
    date = input("Введите дату: ")
    st = date.split(".")
    i = int(st[0])
    j = int(st[1])
    k = int(st[2][2:])

    if i * j == k:
        print(True)
    else:
        print(False)

mag_date()
