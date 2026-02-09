def main() -> None:
    curses_list = []
    result = []
    n = int(input(f'Введите число студентов: '))
    for stud in range(n):
        curses_list.append(input(f'Введите курсы выбранные'
                                 f' {stud + 1}-ым студентом: ').split())

    for el in curses_list:
        result.extend(el)

    print(f'{len(set(result))} курсов всего было выбрано')


if __name__ == "__main__":
    main()
