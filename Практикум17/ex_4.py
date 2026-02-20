def create_words_pairs_list() -> list:
    '''
    function getting antonims and forming list from them
    :return: list
    '''
    els_list = []
    n = int(input())
    for line in range(n):
        abils = input().lower().split()
        els_list.append((abils[0], abils[1:]))
    return els_list

def main() -> None:

    dict_els = dict(create_words_pairs_list())
    word_check = input().lower()
    for stat, el_list in dict_els.items():
        if word_check in el_list:
            print(stat)
            break
    else:
        print(f'Предмет не принадлежит ни к одному типу')


if __name__ == '__main__':
    main()