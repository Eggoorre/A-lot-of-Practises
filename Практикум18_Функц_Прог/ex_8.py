from functools import wraps
from datetime import datetime


def exceptions_log(func):
    '''
    decorator that logs exceptions raised during function execution to a file
    :param func: function with arbitrary arguments
    :return: wrapped function
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open('errors.log', 'a', encoding='utf-8') as f:
                f.write(f'{datetime.now()} : {type(e).__name__}: {e}\n')
            # function returns None if exception occurs

    return wrapper


@exceptions_log
def divide(a, b):
    '''
    function divides two numbers
    :param a: dividend
    :param b: divisor
    :return: result of division
    '''
    return a / b


if __name__ == '__main__':
    print(divide(10, 0))