def change_r(numbers_list, n):
    '''
    function shifting list elements to the right on n points
    :param numbers_list:
    :param n:
    :return: numbers_list_new
    '''
    numbers_list_new = (numbers_list[-n:] +
                        numbers_list[:-n])
    return numbers_list_new


def change_l(numbers_list, n):
    '''
    function shifting list elements to the left on n points
    :param numbers_list:
    :param n:
    :return: numbers_list_new
    '''
    numbers_list_new = (numbers_list[n:] +
                        numbers_list[:n])
    return numbers_list_new


def main_funct():
    '''
    main function printing result of shifting list on n points
    '''
    nums_list = list(map(int,
                         input(f'Введите набор чисел: ').split()))
    command = input(f'Введите команду: ')

    command_num_list = [x for x in command if x.isdigit()]
    command_num = int(''.join(command_num_list))

    if command[0] == 'R':
        nums_list = change_r(nums_list, command_num)
    elif command[0] == 'L':
        nums_list = change_l(nums_list, command_num)
    else:
        print(f'Введите правильную команду')

    print(nums_list)


main_funct()
