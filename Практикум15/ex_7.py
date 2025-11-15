def nod(a: int, b: int) -> int:
    '''
    recursive function finding nod for a and b
    :param a: first num
    :param b: second num
    :return: nod
    '''
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return nod(b, a % b)

def main() -> None:
    num_a = int(input(f'Введите число a: '))
    num_b = int(input(f'Введите число b: '))
    print(nod(num_a, num_b))


if __name__ == '__main__':
    main()
