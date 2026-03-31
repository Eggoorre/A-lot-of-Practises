def sum_multipliers(a: int, b: int, c: int, d: int) -> int:
    '''
    function finding sum of nums dividing on c and d
    :param a: interval start
    :param b: interval end
    :param c: multiplier 1
    :param d: multiplier 2
    :return: sum of nums
    '''
    return sum(filter(lambda x: x % c == 0 and x % d == 0,
                      range(a, b + 1)))


def main() -> None:
    '''
    main function
    :return: None
    '''
    a_input = int(input())
    b_input = int(input())
    c_input = int(input())
    d_input = int(input())
    print(sum_multipliers(a_input, b_input, c_input, d_input))


if __name__ == '__main__':
    main()