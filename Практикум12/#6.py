t = 'Слонята едят хлеб.'
list = [x.lower() for x in t.split()]
answ = list.reverse()
print(f'{' '.join(list)}.')