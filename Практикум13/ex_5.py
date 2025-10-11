def tel_card_pay(p):
    if p not in [5, 10, 25, 50, 100]:
        print(f'Ошибка, нет такой карточки.')

    if p == 5 or p == 10:
        return p
    elif p == 25:
        return p + 3
    elif p == 50:
        return p + 8
    elif p == 100:
        return p + 20


price = int(input(f'Введите цену вашей карточки, в $: '))
print(tel_card_pay(price))
