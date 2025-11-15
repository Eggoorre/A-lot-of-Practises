def ind_maxlist(a: list[int], index=0, max_val=None, max_index=None) -> int:
    '''
    recursive function finding index of max element in list
    :param a: list
    :param index: index which is changing
    :param max_val: max element in list
    :param max_index: index of max element in list
    :return: max index of max element in list
    '''
    if index == len(a):
        return max_index + 1

    if max_val is None or a[index] > max_val:
        max_val = a[index]
        max_index = index

    return ind_maxlist(a, index + 1, max_val, max_index)


def main() -> None:
    num_list = list(map(int, input(f'Введите список'
                                   f' целых чисел: ').split()))
    print(ind_maxlist(num_list))


if __name__ == '__main__':
    main()
