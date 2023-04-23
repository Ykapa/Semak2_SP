S = ""

while True:
    word = input("Введите слово: ")
    if len(word) > 0:
        S = S + " " + word
    else:
        break
print(S)