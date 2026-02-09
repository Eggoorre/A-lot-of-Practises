def sl_favs() -> None:
    '''
    function finding only Sladkoezhkins favourites
    and printing len of set with them
    :return: None
    '''
    sl_fav_set = set(input(f'Введите предпочтения Сладкоежкина: ').split())

    friends_fav_set = set()
    friends_num = int(input(f'Введите кол-во друзей Сладкоежкина: '))

    for friend in range(friends_num):
        friends_fav_list = input(f'Введите предпочтения {friend + 1}'
                                 f'-го друга Сладкоежкина: ').split()
        for fav in friends_fav_list:
            friends_fav_set.add(fav)

    sl_favs_ego = [x for x in sl_fav_set if x not in friends_fav_set]

    print(f'Количество наименований продуктов,'
          f' нравящихся только Сладкоежкину: {len(sl_favs_ego)}')


def main() -> None:
    '''
    main function
    :return: None
    '''
    sl_favs()


if __name__ == "__main__":
    main()
