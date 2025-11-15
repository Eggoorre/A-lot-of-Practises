def degree5(n: int, counter_degree=0) -> int:
    '''
    recursive function finding a degree of a num
    :param n:
    :param counter_degree: counter of degree of num
    :return: counter_degree or -1 if num is not any degree of 5
    '''
    if n == 1:
        return counter_degree
    elif n // 5 < 1 or n % 5 != 0:
        return -1
    else:
        return degree5(n // 5, counter_degree + 1)


def main() -> None:
    num = int(input(f'Введите число: '))
    print(degree5(num))


if __name__ == '__main__':
    main()
