import random

K = 0
LST = []
LSTD = []

for j in range(15):
    I = random.randrange(0, 15)
    if I in LST:
        LSTD.append(I)
    LST.append(I)

for I in range(0,15):
    for J in range(0, len(LSTD)):
        if I == LSTD[J]:
            K += 1
    K += 1
    if K > 1:
        print("Число", str(I), "повторяется", str(K), "раза!")
    K = 0

