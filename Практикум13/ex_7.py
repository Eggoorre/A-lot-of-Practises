import math


def common_multipliers(a, b, n):
    lcm = a * b // math.gcd(a, b)
    current = lcm
    while current <= n:
        print(current)
        current += lcm


num_a = int(input())
num_b = int(input())
num_n = int(input())

common_multipliers(num_a, num_b, num_n)
