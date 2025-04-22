f = open('input.txt', 'r', encoding='utf-8')
o = open('output.txt', 'w', encoding='utf-8')
line_list = []
try:
    for line in f:
        line_list.append(line)
    if (len(line_list) - 1) == int(line_list[0]):
        o.write('YES')
    else:
        o.write('NO')
except ValueError:
    o.write('ERROR')