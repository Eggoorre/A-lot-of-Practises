#1
counter = 0
for i in range(100, 1000):
    if i % 17 == 0:
        counter += 1
        print(i, end=' ')
print('\n', counter)

#2
counter = 0
word = input()

for i, letter in enumerate(word):
    if i % 3 == 0:
        counter += 1
        print(word[i+2], end='')


#3
import math as mth
while True:
    number = float(input('Введите число: '))
    root = mth.sqrt(number)

    if root == int(root):
        print(f'Это число является полным квадратом')
    else:
        print(f'Число не является полным квадратом, попробуйте ещё раз')


#4
number_range = int(input('Введите количество'
                         ' натуральных чисел для суммы: '))
print(round((number_range * (number_range + 1)) / 2))


#5
number = int(input())
for i in range(number):
    answ = i ** 3
    if answ <= number and i != 0:
        print(answ, end=' ')


#6
number = int(input())
for i in range(number):
    answ = 2 ** i
    if answ <= number:
        print(answ)


#7
number = int(input())
power_of_two = False
for i in range(0, 100):

    if 2 ** i == number:
        power_of_two = True
        break

if power_of_two == True:
    print('Верно')
else:
    print('Неверно')


#8
number = int(input())
count = 0
left = 1
right = number

while left <= right:
    mid = (left + right) // 2
    count += 1

    if mid == right or mid == left:
        break
    elif mid < left:
        left = mid + 1
    else:
        right = mid - 1
print(count + 1)


#9
n, k, r = map(int, input().split())
count = 1
day = 1
while n * ((100 + k)/100) ** count < r:
    count += 1
    day += 1
    if n * ((100 + k)/100) ** count >= r:
        day += 1
        break
print(day)

#10
count = 0
prev_temp = None
while True:
    temp = float(input())

    if (temp > 37.8 or temp < 37.4) and temp != 0:
        print('Некорректный ввод')

    if temp == 0:
        break
    if prev_temp is not None and temp < prev_temp:
        count += 1
    prev_temp = temp
print(count)