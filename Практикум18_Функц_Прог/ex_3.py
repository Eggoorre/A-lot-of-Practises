def nums_sum(a: int, b: int, c: int, d: int) -> int:
    '''
    function finding sum of nums which not divide on c and end on d
    :param a: start
    :param b: end
    :param c: num1
    :param d: num2
    :return: sum of nums found
    '''
    return sum(
        map(lambda x: x,
            filter(lambda x: x % c != 0 and x % 10 == d,
                   range(a, b + 1)))
    )

def main() -> None:
    '''
    main function
    :return: None
    '''
    a_input = int(input())
    b_input = int(input())
    c_input = int(input())
    d_input = int(input())
    print(nums_sum(a_input, b_input, c_input, d_input))


if __name__ == '__main__':
    main()