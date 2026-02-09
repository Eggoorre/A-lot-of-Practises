def is_el_in() -> None:
    '''
    function printing answer if num is in set1 & set2
    :return: None
    '''
    set_1 = set(input().split())
    set_1_int = set(int(x) for x in set_1)

    set_2 = set(input().split())
    set_2_int = set(int(x) for x in set_2)

    set_betw = set_2_int & set_1_int

    num = int(input())

    if num in set_betw:
        print(f'Значение принадлежит пересечению множеств')
    else:
        print(f'Значение не принадлежит пересечению множеств')


def main() -> None:
    '''
    main function
    :return: None
    '''
    is_el_in()


if __name__ == "__main__":
    main()
