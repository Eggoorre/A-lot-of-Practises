def change_r(numbers_list: list[int], n: int) -> list[int]:
    '''
    function shifting list elements to the right n times
    :param numbers_list: list which is being changed
    :param n: number of shifts
    :return: numbers_list
    '''
    n %= len(numbers_list)
    for _ in range(n):
        numbers_list = (numbers_list[-1:] + numbers_list[:-1])
    return numbers_list


def change_l(numbers_list: list[int], n: int) -> list[int]:
    '''
    function shifting list elements to the left n times
    :param numbers_list: list which is being changed
    :param n: number of shifts
    :return: numbers_list
    '''
    n %= len(numbers_list)
    for _ in range(n):
        numbers_list = (numbers_list[1:] + numbers_list[:1])
    return numbers_list


def main_funct() -> None:
    '''
    main function printing result of shifting list n times
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


if __name__ == "__main__":
    main_funct()
