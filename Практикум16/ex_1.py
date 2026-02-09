def num_check() -> None:
    '''
    function checking if num is in input num list
    :return: None
    '''
    nums = list(map(int, input(f'Введите последовательность'
                               f' натуральных чисел: ').split()))
    num = int(input(f'Введите число для проверки: '))
    if num in set(nums):
        print(f'Число есть в списке')
    else:
        print(f'Числа нет в списке')


def main() -> None:
    '''
    main function
    :return: None
    '''
    num_check()


if __name__ == "__main__":
    main()
