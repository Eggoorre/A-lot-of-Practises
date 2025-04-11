
#1
n, d, r = map(int, input().split(' '))
print(l := ((n * 2 * r) + (2 * d)))

#2
num = int(input())
x = num
while x>2:
    x = num**0.5
    print(f'{x:5.3f}')
    num = x


#3
num = int(input())
group = 1
while True:
    group += 1
    num_1 = num % group
    if num_1 == 0:
        break
print(group)


#4
counter = 0
while True:
    n = int(input())
    if n % 4 == 0 and n != 0:
        counter += 1
    if n == 0:
        break
print(counter)

#5
def is_palindrome(s):
    return s == s[::-1]


for N in range(100000, 1000000):
    s = str(N)

    if not is_palindrome(s[1:]):
        continue

    s_plus_1 = str(N + 1)
    if len(s_plus_1) == 6 and not is_palindrome(s_plus_1[1:]):
        continue

    s_plus_2 = str(N + 2)
    if len(s_plus_2) == 6:
        middle_4 = s_plus_2[1:5]
        if not is_palindrome(middle_4):
            continue
    else:
        continue

    s_plus_3 = str(N + 3)
    if len(s_plus_3) == 6 and not is_palindrome(s_plus_3):
        continue

    print(N)
    break

#6
for i in range(10,100):
    if i ** 2 % 100 == i:
        break
print(f'{i:>3}\n*{i}\n___\n{i**2}')

#7
for i in range(10000, 99999):
    m = i // 10000
    o = i % 10000 // 1000
    n = i % 1000 // 100
    e = i % 100 // 10
    y = i % 10

    if len({m, o, n, e, y}) != 5:
        continue

    for s in range(1, 10):
        for d in range(1, 10):
            for r in range(1, 10):
                if (s == d or s == r or d == r or
                        s in {m, o, n, e, y} or
                        d in {m, o, n, e, y} or
                        r in {m, o, n, e, y}):
                    continue

                send = s * 1000 + e * 100 + n * 10 + d
                more = m * 1000 + o * 100 + r * 10 + e

                if send + more == i:
                    print(f"SEND = {send}, MORE = {more}, MONEY = {i}")

#8
num = int(input())
counter = 0
for i in range(1, num):
    for j in range(1, i):
        if j**2 + i**2 == num:
            counter += 1
        elif i == j:
            counter -= 1
print(counter)

#9
summ = 0
n = int(input())
for i in range(0, n + 1):
    summ += i
print(summ * 4)


#10
