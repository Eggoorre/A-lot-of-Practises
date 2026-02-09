def courses() -> None:
    '''
    function getting names of courses and printing len of courses set
    :return: None
    '''
    courses_set = set()
    n = int(input(f'Введите число студентов: '))
    for student in range(n):
        courses_list = input(f'Введите курсы {student + 1}-го студента: ').split()
        for course in courses_list:
            courses_set.add(course)
    print(f'Количество выбранных курсов - {len(courses_set)}')


def main() -> None:
    '''
    main function
    :return: None
    '''
    courses()


if __name__ == "__main__":
    main()
