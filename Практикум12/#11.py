cities = input().split()
cities = [city.lower() for city in cities]
for i in range(len(cities)):
    if cities[i][-1] in ['ъ', 'ь', 'ы']:
        cities[i] = cities[i][:-1]
for i in range(1, len(cities)):
    if cities[i][0] != cities[i - 1][-1]:
        print('Играйте по правилам!')
        break
else:
    if len(cities) % 2 == 0:
        print(f'Победил игрок 2')
    else:
        print(f'Победил игрок 1')