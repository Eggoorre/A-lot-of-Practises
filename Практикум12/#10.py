t = 'Я люблю мороженое и кофе'
list = [x for x in t.split()]
for i in list:
    k = [x for x in i]
    if i != list[0] and len(k) == len(set(k)):
        print(i)
