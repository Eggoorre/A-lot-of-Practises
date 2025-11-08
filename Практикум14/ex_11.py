nums_list = list(map(int,
                     input(f'Введите набор чисел: ').split()))

stop_counter = 0
while stop_counter < 1:
    command = input(f'Введите команду: ')
    if command[0] == 'R':
        new_list = (nums_list[-int(command[1]):] +
                    nums_list[:-int(command[1])])
        print(new_list)
        stop_counter += 1

    elif command[0] == 'L':
        new_list = (nums_list[int(command[1]):] +
                    nums_list[:int(command[1])])
        print(new_list)
        stop_counter += 1
    else:
        print(f'Ошибка, введите правильную команду')
