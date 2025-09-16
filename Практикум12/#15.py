def returnMatches(a, b):
    matches = set()
    for i in a:
        if i in b:
            matches.add(i)
    return len(matches) or 0


def bulls(a, b):
    bulls = 0
    for i in range(4):
        if int(a[i]) == int(b[i]):
            bulls += 1
    return bulls


number = input()
b = [str(x) for x in number]
print('\n' * 25)

for i in range(10):
    a = input()
    a_list = [str(x) for x in a]
    print(f'Быков:{bulls(a, b)} '
          f' Коров:{returnMatches(a, b) - bulls(a, b)}')
    if bulls(a, b) == len(b):
        print('Победа')
        break


else:
    print('Закончились ходы(')
