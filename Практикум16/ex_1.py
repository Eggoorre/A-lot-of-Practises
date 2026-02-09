def main() -> None:
    nums_list = list(map(int, input(f'Введите последовательность'
                                    f' натуральных чисел: ').split()))
    num = int(input(f'Введите число для проверки: '))
    if num in set(nums_list):
        print(f'Число есть в списке')
    else:
        print(f'Числа нет в списке')


if __name__ == "__main__":
    main()
