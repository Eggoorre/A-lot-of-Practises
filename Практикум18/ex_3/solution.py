class NotSleeping:
    '''
    class making counting sheeps before sleeping

    Attributes:
        name(str): name of person
        count_sheeps(int): amount of sheep counted

    Methods:
        add_sheep(): adds one more sheep in count_sheeps, returns None
        lost(): making person to forget counted sheep, makes count_sheeps to 0, returns None
        get_count_sheeps(): returns num(int) of counted sheep
    '''

    def __init__(self, name: str, count_sheeps: int = 0):
        '''
        initialising person's sleeping
        :param name: person's name
        :param count_sheeps: amount of sheeps counted before
        '''
        self.name = name
        self.count_sheeps = count_sheeps

    def add_sheep(self) -> None:
        '''
        method adding sheep
        :return: None
        '''
        self.count_sheeps += 1

    def lost(self):
        '''
        method loosing all counts of sheep
        :return:
        '''
        self.count_sheeps = 0

    def get_count_sheeps(self) -> int:
        '''
        method returning num of counted sheep
        :return: num of counted sheep
        '''
        return self.count_sheeps
