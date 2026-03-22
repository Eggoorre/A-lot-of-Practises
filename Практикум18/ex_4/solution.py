class User:
    '''
    class making users info

    Attributes:
        id(int): users id
        nick_name(str): users nickname
        first_name(str): users firstname
        last_name(str, optional): users lastname
        middle_name(str, optional): users middle name
        gender(str, optional): users gender

    Methods:
        update(): returns updated info
    '''

    def __init__(self, id: int, nick_name: str, first_name: str,
                 last_name: str = None, middle_name: str = None, gender: str = None) -> None:
        '''
        initialisation of users info
        :param id:
        :param nick_name:
        :param first_name:
        :param last_name: optional
        :param middle_name: optional
        :param gender: optional
        '''
        self.id = id
        self.nick_name = nick_name

        self.name_parts = [last_name, first_name, middle_name]
        self.name = f'NAME: {" ".join(el for el in self.name_parts if el)}'

        self.gender = gender if gender else None

    def __str__(self) -> str:
        '''
        returns full users info
        :return: full_user info
        '''
        full_user = ['ID: ' + str(self.id), 'LOGIN: ' + self.nick_name, self.name]
        if self.gender is not None:
            full_user.append(f'GENDER: {self.gender}')

        return ' '.join(full_user)

    def __repr__(self) -> str:
        '''
        returns users nickname, used in debugging and list of users
        :return: nick_name(str)
        '''
        return self.nick_name

    def update(self, id: int = 0, nick_name: str = '', first_name: str = '',
               last_name: str = '', middle_name: str = '', gender: str = '') -> None:
        '''
        updating user's info
        :param id:
        :param nick_name:
        :param first_name:
        :param last_name:
        :param middle_name:
        :param gender:
        :return: None
        '''

        if id != 0:
            self.id = id
        if nick_name != '':
            self.nick_name = nick_name
        if last_name != '':
            self.name_parts[0] = last_name
        if first_name != '':
            self.name_parts[1] = first_name
        if middle_name != '':
            self.name_parts[2] = middle_name

        self.name = f'NAME: {" ".join(el for el in self.name_parts if el)}'

        if gender != '':
            self.gender = gender
