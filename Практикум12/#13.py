counter = 0
while True:
    counter += 1
    num = str(input())
    list = [int(x) for x in num]
    if (len(list) % 2 == 0) and (sum(list[0:(len(list) // 2)]) ==
                                 sum(list[(len(list) // 2):len(list)])):
        break
print(counter)
