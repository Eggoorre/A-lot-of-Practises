def numbers(x: int) -> None:
    '''
    recursive function printing number
     from the end to the start
    :param x: number
    :return: no return
    '''
    x = str(x)

    if len(x) == 1:
        print(x)
        return
    print(x[-1])

    numbers(int(x[:-1]))


def main() -> None:
    number = int(input(f'Введите число: '))
    numbers(number)


if __name__ == '__main__':
    main()
