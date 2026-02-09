def main() -> None:
    sl_fav_list = input(f'Введите предпочтения Сладкоежкина: ').split()
    friends_fav_list = []
    friends_finale = set()
    friends_num = int(input(f'Введите кол-во друзей Сладкоежкина: '))

    for friend in range(friends_num):
        friends_fav_list.append(input(f'Введите предпочтения {friend + 1}'
                                      f'-го друга Сладкоежкина: ').split())

    for el in friends_fav_list:
        friends_finale.update(el)

    sl_favs_ego = [x for x in sl_fav_list if x not in friends_finale]

    print(f'Количество наименований продуктов,'
          f' нравящихся только Сладкоежкину: {len(sl_favs_ego)}')


if __name__ == "__main__":
    main()
