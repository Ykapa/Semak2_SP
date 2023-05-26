ru_en = {}
ru_en_sort = {}

with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for i in file:
        p = i.strip().split('-')
        En_w = p[0].strip()
        Ru_w = p[1].strip()
        ru_en[Ru_w] = En_w

    S = sorted(ru_en.items())
    for i in S:
        ru_en_sort[i[0]] = i[1]

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for key, value in ru_en_sort.items():
        file.write(f"{key} - {value}\n")