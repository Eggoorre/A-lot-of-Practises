#1
from os.path import split
all_watch = input("Введите общую стоимость часов: ")
a = int(all_watch)
b = 96 # Количество серебрянных часов
c = 6 # Количество золотых часов
d = 48 # Цена серебрянных часов
e = (b * d)
f = (a - e)
g = int(f / c)
print(g, "рублей", '\n')

#2
ct_pt1, ct_pt2 = input("Введите страну: ").split()
print( ct_pt1, ct_pt2,  sep='\n')

#3
S, R = map(int, input().split())
print(S + R, '\n')

#4
a = (1 + 7 ** 4)
answ = int(a)
print(answ, '\n')

#5
v = float(input("Введите плановую сумму объёма продаж: "))
answ = float(v * 0.19)
print("Прибыль:", round(answ, 2), '\n')

#6
w_in_p = int(input("Введите вес: "))
h_in_d = int(input("Введите рост: "))
w_in_k = w_in_p * 0.453592
h_in_m = h_in_d * 0.0254
print(round(w_in_k / (h_in_m ** 2), 2), '\n')

#7
S = 10000
h = 0.01
answer = (S * h)
print(int(answer), '\n')

#8
N, M = map(int, input().split())
print(M // (N + 1), '\n')

#9
N = (int(input("Введите количество быков: ")))
K = (int(input("Введите количество семей: ")))
print("Количество быков, которых нужно отпустить:", N % K, '\n')

#10
s_m = int(input("Введите расстояние в метрах: "))
s_fullmiles = (s_m // 1609)
print("Расстояние в полных милях:", s_fullmiles)