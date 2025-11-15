def mod_number(dividend: int, divisor: int) -> int:
    '''
    recursive function finding what remains after dividing
    :param dividend:
    :param divisor:
    :return: remainder
    '''
    if dividend - divisor < divisor:
        return dividend - divisor
    else:
        return mod_number(dividend - divisor, divisor)


def main() -> None:
    num_a = int(input(f'Введите делимое: '))
    num_b = int(input(f'Введите делитель: '))
    print(mod_number(num_a, num_b))


if __name__ == '__main__':
    main()
