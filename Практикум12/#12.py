name = input().lower()
symbols_set = set()
for i in range(26):
    symbols_set.add(chr(ord('A') + i).lower())
for i in range(9):
    symbols_set.add(chr(ord('0') + i).lower())
symbols_set.add('_')
sorted_sym = sorted(symbols_set)
for letter in name:
    if (letter not in sorted_sym) \
            or (name[0] in sorted_sym[:10]):
        print(f'Строка не может быть именем в Python')
        break
else:
    print(f'Строка может быть именем в Python')
