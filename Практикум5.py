#1
a = int(input())
if a % 400 == 0:
    print(366)
elif a % 100 == 0:
    print(365)
elif a % 4 == 0:
    print(366)
else:
    print(365)

#2
import turtle as trt

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

if (xc - x) ** 2 + (yc - y) ** 2 < r ** 2:
    print("Точка внутри окружности.")
elif (xc - x) ** 2 + (yc - y) ** 2 == r ** 2:
    print("Точка на окружности")
else:
    print("Точка вне окружности.")

trt.up()
trt.setposition(xc, yc - r)
trt.down()
trt.circle(r)
trt.up()
trt.setposition(x, y)
trt.down()
trt.dot(10)
trt.done()
print('\n')

#3
a = int(input())
b = a // 1000
c = a % 1000
d = c // 100
e = c % 100
f = e // 10
g = e % 10
if 10 * b + d == 10 * g + f:
    print("настоящее")
else:
    print("кривое")
print('\n')

#4
a = int(input())
if a % 10 == 1:
    print(a, "попугай")
elif (a % 10 <= 4) and (a % 10 >= 2):
    print(a, "попугая")
else:
    print(a, "попугаев")
print('\n')

#5
w_in_p = int(input("Введите вес: "))
h_in_d = int(input("Введите рост: "))
w_in_k = w_in_p * 0.453592
h_in_m = h_in_d * 0.0254
index_f = round(w_in_k / (h_in_m ** 2), 2)
if index_f < 16:
    print("выраженный дефицит массы тела")
elif (index_f >= 16) and (index_f <= 18.49):
    print("недостаточная масса тела")
elif (index_f >= 18.5) and (index_f <= 24.99):
    print("норма")
elif (index_f >= 25) and (index_f <= 29.99):
    print("избыточная масса тела")
elif (index_f >= 30) and (index_f <= 34.99):
    print("ожирение первой степени")
elif (index_f >= 35) and (index_f <= 39.99):
    print("ожирение второй степени")
else:
    print("ожирение третьей степени")
print('\n')

#6
a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and a == c:
    print("3")
elif a == b or b == c or a == c:
    print("2")
else:
    print("0")
print('\n')

#7
N, K, M = map(int, input().split())
if abs(M - K) > N - abs(K - M):
    print(N - abs(K-M) - 1)
else:
    print(abs(M-K) - 1)
print('\n')

#8
k = int(input())
g = k // (17 * 29)
s = (k - g * 17 * 29) // 29
r = (k - g * 17 * 29) - s * 29
if g != 0:
    print(g, "галлеонов")
if s != 0:
    print(s, "сиклей")
if r != 0:
    print(r, "кнатов")
print('\n')

#9
h1, h2, h3 = map(int, input().split())
if h1 > h2 > h3:
    print(h1, h2, h3)
elif h1 > h3 > h2:
    print(h1, h3, h2)
elif h2 > h3 > h1:
    print(h2, h3, h2)
elif h2 > h1 > h3:
    print(h2, h1, h3)
elif h3 > h1 > h2:
    print(h3, h1, h2)
elif h3 > h2 > h1:
    print(h3, h2, h1)

#10
pincode = int(input("Введите ПИН-код"))
num1 = pincode // 1000
num2 = (pincode % 1000) // 100
num3 = ((pincode % 1000) % 100) // 10
num4 = (((pincode % 1000) % 100) % 10) % 10
if (pincode < 10000) and (pincode < 1900 or pincode > 2050):
    if num1 != num2 != num3 != num4:
        print("OK")
    else:
        print("ERROR")
else:
    print("ERROR")
