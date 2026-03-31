import json


def to_json(func):
    '''
    decorator that converts function result to JSON format string
    :param func: function with arbitrary arguments
    :return: wrapped function
    '''
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, ensure_ascii=False, default=str)

    return wrapper


def main() -> None:
    @to_json
    def cube(x):
        '''
        function returns cube of a number
        :param x: number
        :return: cube of the number
        '''
        return x ** 3

    @to_json
    def get_user(name, age):
        '''
        function returns user information as dictionary
        :param name: user name
        :param age: user age
        :return: dict with user data
        '''
        return {'Имя': name, 'Возраст': age}

    @to_json
    def get_data():
        '''
        function returns nested data structure with users list
        :return: dict with list of users
        '''
        return {
            "users": [
                {'Имя': 'Дмитрий', 'Возраст': 18},
                {'Имя': 'Василий', 'Возраст': 22}
            ]
        }

    print(cube(5))
    print(get_user('Владимир', 36))
    print(get_data())


if __name__ == '__main__':
    main()