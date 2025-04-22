f = open('input.txt', 'r', encoding='utf-8')
o = open('output.txt', 'w', encoding='utf-8')
for line in f:
    if len(line) > 20:
        o.write(line)