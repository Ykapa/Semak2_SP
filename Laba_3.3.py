
while True:
    word = input("Введите слово: ")
    if "stop" in word:
        break
    elif "ф" in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")