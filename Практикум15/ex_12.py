def ind_maxlist(a: list[int], x:int, index=0) -> int:
    '''
    recursive function asking if x in a
    :param a: list
    :param x: num which is being searched
    :param index: num which is running through list
    :return: yes or no (1 or 0)
    '''
    if index == len(a):
        return 0

    if a[index] == x:
        return 1

    return ind_maxlist(a, x, index + 1)


def main() -> None:
    num_list = list(map(int, input(f'Введите список'
                                   f' целых чисел: ').split()))
    num_x = int(input(f'Введите число которое ищите: '))
    print(ind_maxlist(num_list, num_x))


if __name__ == '__main__':
    main()
