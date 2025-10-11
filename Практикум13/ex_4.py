def payment(p):
    if p < 20:
        print(f'Ошибка, недостаточный перевод.')
    elif p > 1000:
        print(f'Недостаточно средств, повторите попытку.')
    else:
        print(f'Успех!')


pay = int(input())
payment(pay)
