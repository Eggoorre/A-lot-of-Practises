def function1(x: int, start_num=2) -> bool:
    '''
    recursive function analyzing whether x is prime
    :param x: num
    :param start_num: runner
    :return: True or False
    '''
    if x < 2:
        return False
    if x % start_num == 0:
        return False
    if start_num >= int(x ** 0.5) + 1 and x % start_num != 0:
        return True
    return function1(x, start_num + 1)


def main() -> None:
    number = int(input(f'Введите число: '))
    print(f'{function1(number)}')

if __name__ == '__main__':
    main()
