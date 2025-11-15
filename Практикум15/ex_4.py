def sum_progress(a: int, r: int, n: int) -> int:
    '''
    a recursive function that finds
    the sum term of n numbers of
    an arithmetic progression
    :param a: a1
    :param r: step
    :param n: number of sequence
    :return: n-th number of sequence
    '''
    if n == 0:
        return a
    else:
        return a + sum_progress(a, r, n - 1) + r * n


def main() -> None:
    start_of_prg = int(input(f'Введите первый член'
                             f' арифметической прогрессии: '))
    step_of_prg = int(input(f'Введите шаг '
                            f'арифметической прогрессии: '))
    number = int(input(f'Введите номер члена: ')) - 1
    print(sum_progress(start_of_prg, step_of_prg, number))


if __name__ == '__main__':
    main()
