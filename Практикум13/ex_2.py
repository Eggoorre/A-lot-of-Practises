def fib_seq(n):
    num_1 = 1
    num_2 = 1
    for i in range(n):
        fib_sum = num_1 + num_2
        num_1 = num_2
        num_2 = fib_sum
        i += 1
        print(num_2)


number = int(input()) - 2
if number == -1:
    print(1)
elif number >= -2:
    print('1\n1')
fib_seq(number)