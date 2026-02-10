def eratosf_num(n: int) -> set[int]:
    '''
    function finding primes with eratosfens algorithm using sets
    :param n: limit of finding primes
    :return: set of primes
    '''
    if n <= 2:
        return set()

    primes = set(range(2, n))

    count_prime = 2

    while count_prime ** 2 < n:
        if count_prime in primes:
            miltiplies = set(range(count_prime ** 2, n, count_prime))
            primes -= miltiplies
        count_prime += 1

    return primes


def main() -> None:
    '''
    main function
    :return: None
    '''
    num = int(input(f'Введите число: '))

    print(eratosf_num(num))


if __name__ == "__main__":
    main()
