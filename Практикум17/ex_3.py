def create_words_pairs_list() -> list:
    '''
    function getting antonims and forming list from them
    :return: list[ant1, ant2]
    '''
    dict_list = []
    n = int(input())
    for pairs in range(n):
        ant_1, ant_2 = input().lower().split()
        dict_list.append((ant_1, ant_2))
    return dict_list


def main() -> None:
    '''
    main function
    :return: None
    '''
    dict_ant = dict(create_words_pairs_list())

    word_input = input().lower()

    for ant1, ant2 in dict_ant.items():
        if word_input == ant1:
            print(ant2)
        elif word_input == ant2:
            print(ant1)
    else:
        print(word_input)


if __name__ == '__main__':
    main()
