nums_list = list(map(int, input().split()))

sum_nums_even = sum(x for x in nums_list if x % 2 == 0)
sum_nums_odd = sum(x for x in nums_list if x % 2 == 1)

print(f'Сумма чётных: {sum_nums_even}\n'
      f'Сумма нечётных: {sum_nums_odd}')
