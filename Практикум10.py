#1
import math as mt
a, b = map(int, input().split("x"))
if (a / 2) ** 2 + (b / 2) ** 2 <= 6.5 ** 2:
    print("Да")
else:
    print("Нет")

#2
a, b = map(int, input().split("x"))
c, d, e = map(int, input().split("x"))

if ((a <= c and b <= d) or (a <= d and b <= c) or
    (a <= c and b <= e) or (a <= e and b <= c) or
    (a <= d and b <= e) or (a <= e and b <= d)):
    print("да")
else:
    print("нет")

#3
n, m = map(int, input().split("x"))
k = int(input())
COUNT = 0

if k < m * n:
    for line in range(1, n):
        if (line * m) >= k and ((n - line) * m) >= (n * m - k):
            COUNT += 1
    for col in range(1, m):
        if (col * n) >= k and ((m - col) * n) >= (n * m - k):
            COUNT += 1
else:
    print(f'Некорректный ввод')

if COUNT > 0:
    print(f'Успешно')
else:
    print(f'Неосуществимо')


#4
cell = input(f'Введите клетку: ')
l = cell[:1]
n = int(cell[1:])
if l == ('a') or l == ('c') or l == ('e') or l == ('g'):
    if n == 1 or n == 3 or n == 5 or n == 7:
        print(f'чёрный')
    else:
        print(f'белый')
elif l == ('b') or l == ('d') or l == ('f') or l == ('h'):
    if n == 1 or n == 3 or n == 5 or n == 7:
        print(f'белый')
    else:
        print(f'чёрный')

#5
letters = ['a','b','c','d','e','f','g','h']
inf = input('Введите ход: ')
start, end = inf.split('-')
for i in range(8):
    if start[0] == letters[i]:
        if letters[i - 1] == end[0] or letters[i+1] == end[0]:
            if (int(start[1]) + 2 == int(end[1]) or
                    int(start[1]) - 2 == int(end[1])):
                print('Верно')
            else:
                print('Ошибка')
        elif letters[i - 2] == end[0] or letters[i + 2] == end[0]:
            if (int(start[1]) + 1 == int(end[1]) or
                    int(start[1]) - 1 == int(end[1])):
                print('Верно')
            else:
                print('Ошибка')


#6
data = input('Введите данные: ')
n, k, m = map(int, data.split(' '))
odin_krug = (n + k - 1) // k
total_time = odin_krug * 2 * m
print(total_time)


#7
k = int(input("Введите количество: "))
COUNT = 0
for i in range(k):
    if k % 5 == 0 and k > 4:
        COUNT +=1
    else:
        k -= 7
for j in range(k):
    if k % 7 == 0 and k > 6:
        COUNT += 1
    else:
        k -= 5
if COUNT > 0:
    print('да')
else:
    print('нет')


#8
position = int(input('Введите порядковый номер цифры: '))
current_position = 1
if position == current_position:
    print(0)
current_position += 1
for number in range(1, 201):
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        temp_number //= 10
        if current_position == position:
            print(digit)
        current_position += 1


#9
x_first = float(input('Координаты по Х первой окружности: '))
y_first = float(input('Координаты по Y первой окружности: '))
r_first = float(input('Координаты по R первой окружности: '))
x_second = float(input('Координаты по Х второй окружности: '))
y_second = float(input('Координаты по Y второй окружности: '))
r_second = float(input('Координаты по R второй окружности: '))

distance = ((x_second - x_first) ** 2 + (y_second - y_first) ** 2)**0.5
if distance > r_first + r_second:
    print('Окружности лежат одна вне другой, не касаясь')
elif distance < abs(r_first - r_second):
    print('Одна окружность лежит внутри другой, не касаясь')
elif distance == r_first + r_second:
    print('Окружности имеют внешнее касание')
elif distance == abs(r_first - r_second):
    print('Окружности имеют внутреннее касание')
else:
    print('Окружности пересекаются')

#10
coord_U_L_1 = input()
coord_D_R_1 = input()
coord_U_L_2 = input()
coord_D_R_2 = input()
x1_l, y1_u = map(float, coord_U_L_1.split(';'))
x1_r, y1_d = map(float, coord_D_R_1.split(';'))
x2_l, y2_u = map(float, coord_U_L_2.split(';'))
x2_r, y2_d = map(float, coord_D_R_2.split(';'))
if x1_r < x2_l or x2_r < x1_l or y2_u < y1_d or y1_u < y2_d:
    print('Прямоугольники лежат вне друг-друга, не касаясь')
elif (x1_r == x2_l or x1_l == x2_r) and (y1_d < y2_u and y1_u > y2_d):
    print('Прямоугольники имеют касание')
elif (y1_u == y2_d or y1_d == y2_u) and (x1_l < x2_r and x1_r > x2_l):
    print("Прямоугольники имеют касание")
elif (x1_l > x2_l and x1_r < x2_r and y1_d > y2_d and y1_u < y2_u):
    print("Первый прямоугольник полностью внутри второго, не касаясь")
elif (x2_l > x1_l and x2_r < x1_r and y2_d > y1_d and y2_u < y1_u):
    print("Второй прямоугольник полностью внутри первого, не касаясь")
else:
    print("Прямоугольники имеют пересечение")
