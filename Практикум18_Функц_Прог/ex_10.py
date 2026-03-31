import time
from functools import wraps


def time_try_restrict(time_limit: float, max_calls: int, period: float):
    '''
    function including decorator attempting to do function
    :param time_limit: limit of procedure
    :param max_calls: amount of calls
    :param period: period
    :return: decorator
    '''

    def decorator(func):
        '''
        decorator attempting to use func
        :param func: function
        :return: wrapper
        '''
        call_times = []

        @wraps(func)
        def wrapper(*args, **kwargs):

            now = time.time()

            call_times[:] = [t for t in call_times if now - t < period]

            if len(call_times) >= max_calls:
                raise Exception(
                    f'Call limit exceeded: {max_calls} calls per {period} sec'
                )

            call_times.append(now)

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            if end - start > time_limit:
                raise Exception(
                    f'Time limit exceeded: {time_limit} sec'
                )

            return result

        return wrapper

    return decorator


@time_try_restrict(time_limit=2, max_calls=2, period=10)
def request_api(user_id):
    '''
    function requesting users api and knowing his status
    :param user_id:
    :return:
    '''
    print(f'Request for user {user_id}')
    return {'status': 'ok'}


if __name__ == '__main__':
    request_api(1)
    request_api(2)
    request_api(3)
