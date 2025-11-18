def ten_to_bin(x: int, bin_list=None):
    '''
    recursive function finding bin version of ten digit num
    :param x:
    :param bin_list: our answer
    which will be reversed because of algorithm
    :return: list of binary num
    '''
    if bin_list is None:
        bin_list = []

    if x == 0:
        if bin_list == []:
            bin_list.append(0)
        return bin_list[::-1]

    bin_list.append(x % 2)
    return ten_to_bin(x // 2, bin_list)


def main() -> None:
    number = int(input(f'Введите число: '))
    bin_num_res = ten_to_bin(number)
    print(''.join(map(str, bin_num_res)))


if __name__ == '__main__':
    main()
