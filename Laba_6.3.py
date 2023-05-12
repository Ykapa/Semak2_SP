dict = {"Андрей": ["Русский", "Английский", "Японский"], "Иван": ["Китайский", "Русский"],
        "Никита": ["Китайский", "Японский"], "Екатерина": ["Японский", "Турецкий", "Английский"]
}
Mass = []
Mass_A = []

for i in dict.keys():
    LST = list(dict[i])
    for j in range(0, len(LST)):
        if "Китайский" in LST[j]:
            Mass_A.append(i)
        if LST[j] not in Mass:
            Mass.append(LST[j])

M = sorted(Mass)

print("Кол-во языков:", len(Mass))
print(*M)
print(*Mass_A)



