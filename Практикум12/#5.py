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
