#1
t = 'уга буга  уга бугагага     ы'
counter = 0
max = 0
for letter in t:
    if letter.isspace():
        counter += 1
        if counter > max:
            max = counter
    else:
        counter = 0
print(max)

#2
t = 'уга бугааааааа  уга бугаыыыыга     ы'
counter = 1
max_count = 1
l_list = []
for l in t:
    l_list.append(l)
for i in range(1, len(l_list)):
    if l_list[i] == l_list[i - 1]:
        counter += 1
        if counter > max_count:
            max_count = counter
    else:
        counter = 1
print(max_count)


#3
t = 'уга бугааааааа  уга бугаыыыыга     ы'
list = [l for l in t.lower() if l.isalpha()]
answ = set(list)
print(len(answ))


#4
t = 'уга бугааааааа  уга ббугаыыыыга     ы'
list = []
for i in t:
    if t.count(i) == 3:
        break
print(i)


#5
t = 'уга бугааааааа  уга бугаыыыыга     ы'
w = 'боооо шооооо коооо лок лок лок'
o = 'куу кааа рееее куууууу'
t_list = []
w_list = []
o_list = []
answ = []
for i in t:
    t_list.append(i)
for j in t:
    w_list.append(j)
for k in t:
    o_list.append(k)
for i in t:
    if i not in w and i not in o:
        answ.append(i)
print(*set(answ), sep=', ')


#6
t = 'Слонята едят хлеб'
list = [x.lower() for x in t.split()]
answ = list.reverse()
print(f'{' '.join(list)}.')

#7
t = 'Барбарики разбились выехав бетон'
list = [x.lower() for x in t.split()]
list_num = []
for i in list:
    list_num.append(len(i))
print(min(list_num))

#8
t = 'Ребята давайте жить дружно'
list = [x.lower() for x in t.split()]
list_num = []
for i in list:
    list_num.append(len(i))
answ = dict(zip(list, list_num))
sorted_answ = sorted(answ.items(), key=lambda item: item[1])
for i in range(0, len(list)):
    print(sorted_answ[i][0], end=' ')

#9
t = 'Не кочегары мы не плотники но сожаленией горьких нет нет'
list = [x for x in t.split()]
for i in list:
    if list.count(i) == 2:
        break
print(i)

#10
t = 'Я люблю мороженое и кофе'
list = [x for x in t.split()]
for i in list:
    k = [x for x in i]
    if i != list[0] and len(k) == len(set(k)):
        print(i)

#11
cities = input().split()
cities = [city.lower() for city in cities]
for i in range(1, len(cities)):
    if cities[i][0] != cities[i - 1][-1]:
        print('Играйте по правилам!')
        break
else:
    if len(cities) % 2 == 0:
        print(f'Победил игрок 2')
    else:
        print(f'Победил игрок 1')


#12
import keyword

name = input("Введите строку: ")

if name.isidentifier() and not keyword.iskeyword(name):
    print("Это допустимое имя в Python")
else:
    print("Это недопустимое имя в Python")



#13
counter = 0
while True:
    counter += 1
    num = str(input())
    list = [int(x) for x in num]
    if (len(list) % 2 == 0) and (sum(list[0:(len(list) // 2)]) ==
                                 sum(list[(len(list) // 2):len(list)])):
        break
print(counter)



#14
answer = input()
hint = input()
answ_l = [x for x in answer]
word = [y for y in len(answ_l) * '*']
print('\n' * 25)
print(hint)
print(word)
for i in range(1, 10):
    a = int(input(f'Буква или слово(0 - буква, 1 - слово)?'))
    if a == 0:
        letter = input()
        for j in range(0, len(word)):
            if letter == answ_l[j]:
                word[j] = letter
    elif a == 1:
        win_answ = input()
        if win_answ == answer:
            print(f'Поздравляем! Вы победили!')
            break
    print(*word, sep='')
else:
    print('Закончились ходы(')


#15
answer = input()
answ_l = [int(x) for x in answer]
print('\n' * 25)

for i in range(1, 10):
    guess = input()
    guess_l = [int(x) for x in guess]

    count_bull = 0
    count_cow = 0

    used_answer = [False] * len(answ_l)
    used_guess = [False] * len(guess_l)

    for j in range(len(answ_l)):
        if guess_l[j] == answ_l[j]:
            count_bull += 1
            used_answer[j] = True
            used_guess[j] = True

    for j in range(len(guess_l)):
        if used_guess[j]:
            continue
        for k in range(len(answ_l)):
            if not used_answer[k] and guess_l[j] == answ_l[k]:
                count_cow += 1
                used_answer[k] = True
                break

    print(f'Быков: {count_bull} Коров: {count_cow}')

    if count_bull == len(answ_l):
        print('Победа!')
        break
else:
    print('Закончились ходы(')



#16
def check_parentheses(text):
    stack = []
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

text = input("Введите текст: ")
if check_parentheses(text):
    print("Скобки расставлены правильно.")
else:
    print("Скобки расставлены неправильно.")
