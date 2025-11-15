def odd_list(a: list, n: int) -> list:
    '''
    recursive function returning list of odd numbers in a list
    :param a: nums_list
    :param n: amount of numbers
    :return: list of odd numbers
    '''
    if n == 0:
        return []
    else:
        nums_rest = odd_list(a[1:], n - 1)
        if a[0] % 2 == 0:
            return [a[0]] + nums_rest
        else:
            return nums_rest


def main() -> None:
    num_list = list(map(int, input(f'Введите список'
                                   f' целых чисел: ').split()))
    print(odd_list(num_list, len(num_list)))


if __name__ == '__main__':
    main()
