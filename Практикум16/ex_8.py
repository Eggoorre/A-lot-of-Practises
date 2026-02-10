from itertools import combinations


def sub_sets(s: set[int]) -> None:
    '''
    function finding printing all sub sets
    :param s: set which is being used
    :return: None
    '''
    for r in range(len(s) + 1):
        for sub_set in combinations(s, r):
            print(set(sub_set))


def main() -> None:
    '''
    main function
    :return: None
    '''
    sequence = set(map(int, input().split()))
    sub_sets(sequence)


if __name__ == "__main__":
    main()
