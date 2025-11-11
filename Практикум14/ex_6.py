num = int(input())
divs_set = set()
for i in range(2, int((abs(num) ** 0.5)) + 1):
    divs_set.add(1)
    if abs(num) % i == 0:
        divs_set.add(i)
        divs_set.add(num // i)
    divs_set.add(abs(num))
print(list(divs_set))
