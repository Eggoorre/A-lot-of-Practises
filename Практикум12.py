#1
'''
t = input()
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
t = input()
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
t = input()
list = [l for l in t.lower() if l.isalpha()]
answ = set(list)
print(len(answ) - 1)


#4
t = 'уга бугааааааа  уга ббугаыыыыга     ы'
list = []
for i in t:
    if t.count(i) == 3:
        break
print(i)


#5
a = input('Введите слово a')
b = input('Введите слово b')
c = input('Введите слово c')

a_list = []
b_list = []
c_list = []

answ_a = []
answ_b = []
answ_c = []

for i in a:
    a_list.append(i)

for j in b:
    b_list.append(j)

for k in c:
    c_list.append(k)

for i in a_list:
    if (i not in b_list) and ( i not in c_list):
        answ_a.append(i)

for i in b_list:
    if (i not in a_list) and ( i not in c_list):
        answ_b.append(i)

for i in c_list:
    if (i not in b_list) and ( i not in a_list):
        answ_c.append(i)

print('Для a:',*set(answ_a), sep=' ')
print('Для b:',*set(answ_b), sep=' ')
print('Для с:',*set(answ_c), sep=' ')


#6
t = 'Слонята едят хлеб.'
list = [x.lower() for x in t.split()]
answ = list.reverse()
print(f'{' '.join(list)}.')

#7
t = 'Барбарики разбились въехав в бетон'
list = [x.lower() for x in t.split()]
list_num = []
for i in list:
    list_num.append(len(i))
print(min(list_num))

#8
t = 'Ребята давайте жить дружно'
answ = []
for line in sorted(t.split(), key=len):
    answ.append(line.lower())
print(*answ)

#9
t = 'Не кочегары мы не плотники но сожаленией горьких нет нет'
list = [x.lower() for x in t.split()]
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
for i in range(len(cities)):
    if cities[i][-1] in ['ъ', 'ь', 'ы']:
        cities[i] = cities[i][:-1]
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
name = input().lower()
symbols_set = set()
for i in range(26):
    symbols_set.add(chr(ord('A') + i).lower())
for i in range(9):
    symbols_set.add(chr(ord('0') + i).lower())
symbols_set.add('_')
sorted_sym = sorted(symbols_set)
for letter in name:
    if (letter not in sorted_sym) \
            or (name[0] in sorted_sym[:10]):
        print(f'Строка не может быть именем в Python')
        break
else:
    print(f'Строка может быть именем в Python')



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
print(*word, sep='')
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
def returnMatches(a, b):
    matches = set()
    for i in a:
        if i in b:
            matches.add(i)
    return len(matches) or 0


def bulls(a, b):
    bulls = 0
    for i in range(4):
        if int(a[i]) == int(b[i]):
            bulls += 1
    return bulls


number = input()
b = [str(x) for x in number]
print('\n' * 25)

for i in range(10):
    a = input()
    a_list = [str(x) for x in a]
    print(f'Быков:{bulls(a, b)} '
          f' Коров:{returnMatches(a, b) - bulls(a, b)}')
    if bulls(a, b) == len(b):
        print('Победа')
        break


else:
    print('Закончились ходы(')



#16
text = input()
brackets_list = [x for x in text if x == '(' or x == ')']
if len(brackets_list) % 2 != 0:
    print('Неправильная постановка скобок!')

else:
    counter = 0
    for bracket in brackets_list:
        if bracket == '(':
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            break
    if counter == 0:
        print('Постановка скобок верна')
    else:
        print('Неправильная постановка скобок!')



#17
'''
#18
