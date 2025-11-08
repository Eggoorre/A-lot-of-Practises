numbers_list = []
for i in range(10):
    number = int(input())
    numbers_list.append(number)

numbers_list_new = []
for i in range(len(numbers_list) - 1):
    number_sum = numbers_list[i] + numbers_list[i + 1]
    numbers_list_new.append(number_sum)

print(numbers_list_new)
