
def ticket():
    msi = 0
    msj = 0
    c = 0
    while True:
        ticket = str(input("Введите номер билета: "))
        lp = int(len(ticket)/2)
        fir = ticket[:lp]
        sec = ticket[lp:]

        mass_i = list(fir)
        mass_j = list(sec)

        while len(mass_i) > c:
            msi += int(mass_i[c])
            msj += int(mass_j[c])
            c += 1

        if msi == msj:
            print("Счастливый номер")
            break
        else:
            print("Не счастливый номер")
ticket()