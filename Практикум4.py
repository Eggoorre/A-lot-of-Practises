#1
password = input("Введите пароль: ")
if password == "пароль":
    print("Проходи!", '\n')
else:
    print("Доступ запрещён!", '\n')

#2
print("Какие два слова передал первой радиограммой Александр Попов?")
r1 = input("Первое слово: ")
r2 = input("Второе слово: ")
if r1 == "Генрих" and r2 == "Герц":
    print("Верно", '\n')
else:
    print("Неверно", '\n')

#3
print("Как зовут главного персонажа романов Яна Флеминга")
print("о вымышленном шпионе секретной разведывательной службы Великобритании?")
name = input("Имя персонажа: ")
if name == "Джеймс Бонд" or name == "Джеймс бонд":
    print("Верно", '\n')
elif name == "джеймс Бонд" or "джеймс бонд":
    print("Верно", '\n')
elif name == "Агент 007":
    print("Верно", '\n')
else:
    print("Неверно", '\n')

#4
print("Вы поедете на бал?")
answ = input("Ответ: ")
if  answ != ("да") and answ != ("нет"):
    print("Верно", '\n')
else:
    print("Неверно", '\n')

#5
a = int(input())
b = int(input())
if a > b:
    print(b, '\n')
else: print(a, '\n')

#6
a, b = input().split(':')
if a > b:
    print("1", '\n')
elif a == b:
    print("0", '\n')
else:
    print("2", '\n')

#7
K, A, S = map(int,input().split())
if K > A and K > S:
    print(K, '\n')
elif A > K and A > S:
    print(A, '\n')
else:
    print(S, '\n')

#8
name = input("Здравствуйте! Как вас зовут? ")
print("Очень приятно, ", name, "! Меня зовут Марк.", sep='')
age = int(input("Сколько вам лет?"))
if age > 81:
    print("Да, ", name, ", Вы старше меня на ", age - 81, " лет", sep='')
else:
    print("Да, ", name, ", Я старше вас на ", 81 - age, " лет", sep='')
interest = input("Вам нравится программировать? ")
if interest == "да" or interest == "Да":
    pt1 = ("Превосходно! Уверен, у вас получится написать")
    pt2 = ("множество полезных и хороших программ.")
    print(pt1, pt2, '\n')
else:
    print("Жаль. Я думал, Вы сможете написать интересную программу для меня.", '\n')

#9
answ1 = input("Собака короткошёрстной породы?")
if answ1 == "да":
    answ2 = input("Рост собаки менее 50 см?")
    if answ2 == "да":
        answ3 = input("У собаки короткий хвост?")
        if answ3 == "да":
            print("Английский бульдог", '\n')
        else:
            answ4 = input("У собаки длинные уши?")
            if answ4 == "да":
                print("гончая", '\n')
            else:
                answ5 = input("У собаки короткое тело?")
                if answ5 == "да":
                    print("мопс", '\n')
                else:
                    print("чихуахуа", '\n')
    else:
        answ6 = input("Собака весит более 50 кг?")
        if answ6 == "да":
            print("датский дог", '\n')
        else:
            print("фоксхаунд", '\n')
else:
    answ7 = input("Рост собаки менее 50 см?")
    if answ7 == "да":
        answ8 = int("У собаки доброжелательный характер?")
        if answ8 == "да":
            print("кокер-спаниэль", '\n')
        else:
            print("ирландский сеттер", '\n')
    else:
        answ9 = input("У собаки рост менее 70 см?")
        if answ9 == "да":
            answ10 = input("У собаки длинные уши?")
            if answ10 == "да":
                print("большой вандейский грифон", '\n')
            else:
                print("колли", '\n')
        else:
            answ11 = input("окрас рыжий с белыми отметинами?")
            if answ11 == "да":
                print("сенбернар", '\n')
            else:
                answ12 = input("белоснежный окрас?")
                if answ12 == "да":
                    print("ирландский волкодав", '\n')
                else:
                    print("ньюфаундлендё", '\n')

#10
a = int(input())
if a % 2 == 0:
    print("да")
else:
    print("нет")