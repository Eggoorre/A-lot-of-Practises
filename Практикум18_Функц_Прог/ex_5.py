from functools import reduce


def if_square(x) -> bool:
    '''
    function checking is num is square or not
    :param x:
    :return:
    '''
    s = int(x ** 0.5)
    return s * s == x


def multiplication(a: int, b: int, c: int) -> int:
    '''
    function finding nums which divide on c and are squared
    and returning their multiplication
    :param a: start
    :param b: end
    :param c: num
    :return: muliplication of nums
    '''
    nums = filter(lambda x: if_square(x) and x % c == 0, range(a, b + 1))
    return reduce(lambda x, y: x * y, nums)


def main() -> None:
    '''
    main function
    :return: None
    '''
    a_input = int(input())
    b_input = int(input())
    c_input = int(input())
    print(multiplication(a_input, b_input, c_input))


if __name__ == '__main__':
    main()
