def simmetr(s: str, i: int, j: int, ) -> bool:
    '''
    recursive function checking the symmetry of string
    :param s: string which is being checked
    :param i: start of checking
    :param j: end  of checking
    :return: True or False
    '''
    if j <= i:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)


def main() -> None:
    string = input(f'Введите строку: ')
    start = int(input(f'Введите начало промежутка: '))
    end = int(input(f'Введите конец промежутка: '))
    print(simmetr(string, start, end))


if __name__ == '__main__':
    main()
