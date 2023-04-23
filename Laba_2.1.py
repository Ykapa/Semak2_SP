pass_1 = input("Введите пароль: ").replace(' ', '')
pass_2 = input("Повторите пароль: ").replace(' ', '')

if pass_1 == pass_2:
    print("Пароль принят!")
else:
    print("Пароль не принят!")
