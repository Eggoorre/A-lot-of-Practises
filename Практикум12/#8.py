t = 'Ребята давайте жить дружно'
answ = []
for line in sorted(t.split(), key=len):
    answ.append(line.lower())
print(*answ)
