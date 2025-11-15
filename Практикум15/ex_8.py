def fib(k: int) -> int:
    '''
    recursive function finding k element of fibonacci sequence
    :param k:
    :return:
    '''
    if k == 1:
        return 1
    elif k <= 0:
        return 0
    else:
        return fib(k - 1) + fib(k - 2)


def main() -> None:
    num = int(input(f'Введите число: '))
    print(fib(num))


if __name__ == '__main__':
    main()
