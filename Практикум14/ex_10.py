nums_list_1 = list(map(int,
                       input(f'Введите первый набор чисел: ').split()))
nums_list_2 = list(map(int,
    input(f'Введите второй набор чисел: ').split()))

range_start = int(input(f'Введите начало среза: ')) - 1
range_end = int(input(f'Введите конец среза: '))

nums_list_2.extend(nums_list_1[range_end:range_start - 1:-1])

print(f'Список 1: {nums_list_1}\n'
      f'Список 2: {nums_list_2}')