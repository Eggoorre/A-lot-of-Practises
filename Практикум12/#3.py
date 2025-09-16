t = input()
list = [l for l in t.lower() if l.isalpha()]
answ = set(list)
print(len(answ) - 1)
