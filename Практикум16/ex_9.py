from itertools import combinations


def k_sub_sets_list(s: set[int], k: int) -> list[set[int]]:
    '''
    function returning list of sub sets with len k from the main set
    :param s: main set
    :param k: len of sub_set
    :return: list of sets with numbers in it
    '''
    answ_list = []
    if len(s) < k:
        return []

    for sub_set in combinations(sorted(s), k):
        answ_list.append(set(sub_set))

    return answ_list


def main() -> None:
    '''
    main function
    :return: None
    '''
    sequence = set(map(int, input(f'Введите множество чисел: ').split()))
    el_length = int(input(f'Введите длину подмножества: '))
    answer = k_sub_sets_list(sequence, el_length)
    print(answer)


if __name__ == '__main__':
    main()
