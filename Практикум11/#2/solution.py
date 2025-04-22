f = open('input.txt', 'r', encoding='utf-8')
r = open('output.txt', 'w', encoding='utf-8')
for line in f:
    line = line.strip()
    if line.startswith('a') or line.startswith('A'):
        r.write(line + '\n')