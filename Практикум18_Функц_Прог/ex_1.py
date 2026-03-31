def is_upper_num(s: str, i: int, j: int) -> int:
    '''
    function returning num of upper letters in string from i to j el
    :param s: string
    :param i: start of searching
    :param j: end of searching
    :return: int
    '''
    return len(list(filter(str.isupper, s[i - 1: j + 1])))


def main() -> None:
    '''
    main function
    :return: None
    '''
    input_s = input(f'Введите строку: ')
    start_i = int(input(f'Введите начало поиска: '))
    end_j = int(input(f'Введите конец поиска: '))
    print(is_upper_num(input_s, start_i, end_j))


if __name__ == '__main__':
    main()
