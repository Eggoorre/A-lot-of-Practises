def ten_to_n(x: int, n:int, bin_list=None):
    '''
    recursive function which is changing
    10 digit system into n digit system
    :param x:
    :param n: n digit system
    :param bin_list: our answer
    which will be reversed because of algorithm
    :return: reversed bin_list
    '''
    if bin_list is None:
        bin_list = []

    if x == 0:
        if not bin_list:
            bin_list.append(0)
        return bin_list[::-1]

    bin_list.append(x % n)
    return ten_to_n(x // n, n, bin_list)


def main() -> None:
    number = int(input(f'Введите число: '))
    num_system = int(input(f'Введите систему исчисления: '))
    bin_num_res = ten_to_n(number, num_system)
    print(f'Число {number} в {num_system}-ричной системе будет числом:'
          f' {'|'.join(map(str, bin_num_res))}')


if __name__ == '__main__':
    main()
