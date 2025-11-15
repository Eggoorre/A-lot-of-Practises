def combin(n: int, k: int) -> int:
    '''
    recursive function finding k combinations from n
    :param n: num of cases
    :param k: num of changings
    :return: num of combinations
    '''
    if k == n or k == 0:
        return 1
    if k != 1:
        return combin(n - 1, k) + combin(n - 1, k - 1)
    return n


def main() -> None:
    num_n = int(input(f'Введите количество всех элементов: '))
    num_k = int(input(f'Введите число перестановок: '))
    if num_k > num_n:
        print(f'Ошибка, число k не может быть больше n')
    else:
        print(combin(num_n, num_k))


if __name__ == '__main__':
    main()
