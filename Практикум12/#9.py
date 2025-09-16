t = 'Не кочегары мы не плотники но сожаленией горьких нет нет'
list = [x.lower() for x in t.split()]
for i in list:
    if list.count(i) == 2:
        break
print(i)