f = open('input.txt', 'r', encoding='utf-8')
lines = f.readlines()
o = open('input.txt', 'w', encoding='utf-8')
for line in lines:
    if int(line) != 100:
        o.write(line)