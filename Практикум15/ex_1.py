def pownum(a: int, n: int) -> int:
    '''
    recursive function that multiplies a n times
    :param a:
    :param n: num of times
    :return: a ** n
    '''
    if n == 1:
        return a
    else:
        return pownum(a, n - 1) * a


def main()-> None:
    number = int(input(f'Введите число: '))
    times = int(input(f'Введите степень: '))
    print(pownum(number, times))


if __name__ == '__main__':
    main()