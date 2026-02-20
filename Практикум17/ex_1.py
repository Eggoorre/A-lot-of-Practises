def main() -> None:
    '''
    main function getting text and making dict with
    counts of its words and sorting them in reverse
    and then printing words in reverse sequence
    :return: None
    '''
    text = input().split()
    dict_of_words = {word: text.count(word) for word in set(text)}
    sorted_dict = dict(sorted(dict_of_words.items(),
                              key=lambda el: el[1],
                              reverse=True))
    for word in sorted_dict.keys():
        print(word)


if __name__ == "__main__":
    main()
