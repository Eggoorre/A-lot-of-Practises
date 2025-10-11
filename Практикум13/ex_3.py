def total_discount(price, discount_card, holiday):
    discount_counter = 0

    if price <= 5000:
        discount_counter += 0
    elif 15000 >= price > 5000:
        discount_counter += 0.03
    elif 20000 >= price > 15000:
        discount_counter += 0.07
    elif 30000 >= price > 20000:
        discount_counter += 0.1

    if discount_card == 1:
        discount_counter += 0.05

    if holiday == 1:
        discount_counter += 0.03

    if discount_counter > 0.15:
        final_price = price * (1 - 0.15)
    else:
        final_price = price * (1 - discount_counter)

    return round(float(final_price), 2)


pr = int(input(f'Введите цену товара: '))
dc = int(input(f'У вас есть скидочная карта?(1 - да, 0 - нет): '))
hol = int(input(f'Сегодня праздничный день?(1 - да, 0 - нет): '))

print(total_discount(pr, dc, hol))