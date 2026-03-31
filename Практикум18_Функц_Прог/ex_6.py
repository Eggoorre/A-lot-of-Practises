def show_result(func):
    '''
    decorator printing result of function with one arg
    :param func: function with one arg
    :return: wrapped function
    '''

    def wrapper(x):
        result = func(x)
        print(result)

        return result

    return wrapper


@show_result
def cube(n) -> int:
    '''
    function returns cube of a num
    :param n: num
    :return: cube of a num
    '''
    return n ** 3


if __name__ == '__main__':
    cube(3)
