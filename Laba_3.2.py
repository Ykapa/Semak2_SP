S = ""

while True:
    word = input("Введите слово: ")
    if word == "stop":
        break
    else:
        S = S + " " + word
print(S)