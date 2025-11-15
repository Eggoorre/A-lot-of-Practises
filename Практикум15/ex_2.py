def count(n: int) -> int:
    '''
    a recursive function that counts
    the number of digits in a number
    :param n: number
    :return: len(n)
    '''
    if len(str(n)) == 1:
        return 1
    else:
        return count(int(str(n)[:-1])) + 1


def main()-> None:
    number = int(input(f'Введите число: '))
    print(count(number))


if __name__ == '__main__':
    main()
