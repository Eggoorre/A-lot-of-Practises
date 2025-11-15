def maxlist(a: list[int], max_val=None) -> int:
    '''
    recursive function finding max element in list
    :param a:
    :param max_val: memory of recursion
    :return: max element
    '''
    if not a:
        return max_val

    if max_val is None or a[0] > max_val:
        max_val = a[0]

    return maxlist(a[1:], max_val)


def main() -> None:
    num_list = list(map(int, input().split()))
    print(maxlist(num_list))


if __name__ == '__main__':
    main()
