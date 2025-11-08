x = 0
while x < 1:
    input_numbers_with_3 = input().split()
    numbers_with_3 = [int(x) for x in input_numbers_with_3]
    if 3 not in numbers_with_3:
        x += 0
        print(f'Неверный ввод, введите ОДНО'
              f' число 3 среди всех остальных чисел')
    else:
        x += 1
        numbers_with_3.remove(3)
        print(numbers_with_3)
