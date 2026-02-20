def create_words_pairs_list() -> list:
    '''
    function getting rus and eng words and forming list from them
    :return: list[rus_word: eng_word]
    '''
    dict_list = []
    n = int(input(f'Введите количество пар слов словаря: '))
    for pairs in range(n):
        rus_word, eng_word = input().lower().split()
        dict_list.append((rus_word, eng_word))
    return dict_list


def main():
    '''
    main function
    :return:
    '''
    dict_of_words = dict(create_words_pairs_list())

    input_line = input().lower().split()
    new_words = [dict_of_words.get(word, word) for word in input_line]

    new_text = ' '.join(new_words)
    print(new_text)


if __name__ == "__main__":
    main()
