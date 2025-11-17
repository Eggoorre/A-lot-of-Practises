def ten_to_n(x: int, n:int) -> str:
    '''
    recursive function which is changing
    10 digit system into n digit system
    :param x:
    :param n: n digit system
    :return: x in base n in string format
    '''
    digits = "0123456789ABCDEF"

    if x < n:
        return digits[x]

    return ten_to_n(x // n, n) + digits[x % n]


def main() -> None:
    number = int(input('Введите число: '))
    num_system = int(input('Введите систему исчисления: '))

    print(f'Число {number} в {num_system}-ричной системе: '
          f'{ten_to_n(number, num_system)}')


if __name__ == '__main__':
    main()
