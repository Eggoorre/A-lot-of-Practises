#1
bitc_summ = int(input())
bit_num = str(bitc_summ)
print(str(bit_num)[-3], '\n')

#2
time = int(input("Введите количество секунд: "))
hrs = time // 3600
min = time % 3600 // 60
sec = time % 3600 % 60
print("Сейчас", hrs, "часов", min, "минут", sec, "секунд", '\n')

#3
a = int(input())
print(a % 2, '\n')

#4
X, Y, N = (input()).split()
price_r = int(X)
price_k = int(Y)
num_purch = int(N)
print(((price_r * 100 + price_k) * num_purch)
      // 100, "руб.", ((price_r * 100 + price_k)
                         * num_purch) % 100, "коп.", '\n')

#5
num = int(input())
print('(\\___/) ' * num)
print("(\"'.\'\") " * num)
print('(")_(") ' * num, '\n')

#6
K = int(input())
N = int(input())
R = int(input())
k = str(K)
m = k * N
M = int(m)
print(M * R, '\n')

#7
raw = input('Enter number:')
print(raw, '\n')

#8
import math as mth
a = int(input())
b = int(input())
c = int(input())
cos1 = (b**2+ c**2 - a**2) / (2 * b * c)
cos2 = (a**2+ c**2 - b**2) / (2 * a * c)
cos3 = (b**2+ a**2 - c**2) / (2 * b * a)
print(mth.degrees(mth.acos(cos1)))
print(mth.degrees(mth.acos(cos2)))
print(mth.degrees(mth.acos(cos3)), '\n')

#9
ATT = int(input())
COMP = int(input())
YDS = int(input())
TD = int(input())
INT = int(input())
a = ((COMP / ATT) - 0.3) * 5
b = ((YDS / ATT) - 3) * 0.25
c = (TD / ATT) * 20 + 2.375
d = (INT / ATT) * 25
answ = ((a + b + c - d) / 6) * 100
print(answ, '\n')

#10
X, Y = (input()).split()
x = int(X)
y = int(Y)
print((x % y) * (y % x) + 1, '\n')

#11
N = float(input())
hrs = (N * 43200 / 360) // 3600
mins = (N * 43200 / 360) % 3600 // 60
H = int(hrs)
M = int(mins)
print(H, M, '\n')

#12
import datetime as dt
current_date = dt.datetime.now()
print(current_date, '\n')

#13
import math as mt
lines = int(input())
column = int(input())
num = int(input())
s = lines * column
page = 1+ num // (s + 1)
lines_num = mt.ceil((num % (s + 1) + page - 1) / lines)
column_num = mt.ceil(num % (s + 1) + page - 1 - (lines_num - 1) * lines)
print("Страница", page, "столбец", lines_num, "строка", column_num)