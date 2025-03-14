#1
print("Hello, Python!"'\n')

#2
print("Привет, Python!")
print("Hello, Python!")
print("Bonjour, Python!")
print("Hej, Python!")
print("Hola, Python!"'\n')

#3
print("Привет,", "Python!", '\n', sep=' ')

#4
print(chr(40), chr(92), chr(95)*3, chr(47), chr(41), sep='')
print(chr(40), chr(61), chr(39), chr(46), chr(39), chr(61), chr(41), sep='')
print(chr(40), chr(34), chr(41), chr(95), chr(40), chr(34), chr(41), '\n', sep='')

#5
print("Привет, Python!", "Hello, Python!", "Bonjour, Python!", "Hej, Python!", "Hola, Python!", '\n', sep='\n')

#6
Name_ask = input("Как Вас зовут? ")
print("Здраствуйте,", Name_ask, '\n')

#7
Name_ask = input("Как Вас зовут? ")
print("Здраствуйте,", Name_ask, '\n')
Activity = input("Что Вам нравится? ")
print("Отлично!", Activity, "- хорошее увлечение", '\n')

#8
Login = input("Логин: ")
Password = input("Пароль: ")
NewPassword = input("Новый пароль: ")
print("Пользователь", Login, "поменял пароль на", NewPassword, '\n')

#9
print("Введите плей-лист папы:")
song1 = input()
song2 = input()
song3 = input()
song4 = input()
song5 = input()
print("Плей-лист мамы:", '\n', song5, '\n', song4, '\n', song3, '\n', song2, '\n', song1, '\n')

#10
number = input("Номер рейса: ")
company_name_rus = input("Название авиакомпании(на русском языке): ")
company_name_eng = input("Название авиакомпании(на английском языке): ")
Arrival_city_rus = input("Город прилёта(на русском языке): ")
Arrival_city_eng = input("Город прилёта(на английском языке): ")
print("Заканчивается посадка на рейс", number, company_name_rus, "до", Arrival_city_rus)
print("This is the final boarding call for", company_name_eng, "flight", number, "to", Arrival_city_eng, '\n')

#11
username = input("Как вас зовут? ")
print("Привет, ", username, "!", sep='')

#12
all_watch = input("Введите общую стоимость часов: ")
a = int(all_watch)
b = 96 # Количество серебрянных часов
c = 6 # Количество золотых часов
d = 48 # Цена серебрянных часов
e = (b * d)
f = (a - e)
g = (f / c)
print(g)

#13
import math as mt

a = input()
b = input()
r1 = int(a)
r2 = int(b)
S_1 = ((pow(r1, 2)) * mt.pi)
S_2 = ((pow(r2, 2)) * mt.pi)
S_3 = S_1 - S_2
if S_3 < 0:
    S_finale = S_3 * (-1)
else:
    S_finale = S_3
print(S_finale)

#14
num = input("Введите число: ")
x = int(num)
answ = ((((x + 2) * 3) - 6)/3) - 4
print(answ)

#15
length = input("Введите длину: ")
ln = float(length)
d = ln / 2.54
f = d / 12
y = f / 3
m = y / 1760
print(y, "ярдов")
print(m, "мили")
print(f, "футов")
print(d, "дюймов")
