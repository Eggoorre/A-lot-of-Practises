#1
result_list = []

while True:
    result = int(input())
    result_list.append(result)
    if result == -1:
        break
result_list.sort()
print(result_list[-1])


#2
result_list = []

while True:
    result = int(input())
    result_list.append(result)
    if result == -1:
        break
result_list.sort()
print(len(result_list) - 1)


#3
income_list = []

while True:
    income = int(input())
    income_list.append(income)
    if income == 0:
        break
print(sum(income_list) / (len(income_list) - 1))


#4
number = int(input())
sum = 0
for i in range(1 ,number + 1):
    sum += i
    print(sum)


#5
n = int(input())
sum = 0
counter = 0
for i in range(1, n):
    for j in range(1, n):
        if i % j == 0 and j != i:
           sum += j
    if sum == i:
        counter += 1
    sum = 0
print(counter)


#6
n = int(input())

for i in range(n):
    answ = i * '*'
    print(f'{answ:>10}')


#7
while True:
    num = input(f'Введите число: ')
    if str.isdigit(num) == False:
        print(f'Ошибка. Попробуйте ещё раз.')
    else:
        print(f'Введено целое число: {num}')
        break


#8
number_list = []
for i in range(1, 10):
    number_list.append(i)
    n = int(''.join(map(str, number_list)))
    print(f' {n} * 8 + {i} = {(n * 8) + i}')

number_2_list = []
for i in range(1, 10):
    number_2_list.append(i)
    m = int(''.join(map(str, number_2_list)))
    print(f' {m} * 9 + {i+1} = {(m * 9) + i + 1}')

number_3_list = []
for i in range(1, 10):
    number_3_list.append(1)
    k = int(''.join(map(str, number_3_list)))
    print(f'{k} * {k} = {k ** 2}')

#9
n = int(input())
num = 0
k = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0 :
            break
    else:
        print(i)


#10
n = int(input())
sum = 0
counter = 0
for i in range(1, n):
    for j in range(1, n):
        if i % j == 0 and j != i:
           sum += j
    if sum == i:
        print(i)
    sum = 0