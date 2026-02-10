from itertools import permutations


def lexic_seq() -> None:
    '''
    function printing permutated list made of set
    :return: None
    '''
    nums_set = set(map(int, input().split()))
    for p in permutations(sorted(nums_set)):
        print(p)


def main() -> None:
    '''
    main function
    :return: None
    '''
    lexic_seq()


if __name__ == "__main__":
    main()
