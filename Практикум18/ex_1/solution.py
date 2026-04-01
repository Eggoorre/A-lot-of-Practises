class Dog:
    '''
    class, making dog

    Attributes:
        name(str): dog name

    Methods:
        say(): dog barking, returning None
    '''

    def __init__(self, name: str) -> None:
        '''
        initialising dog

        args:
            name(str): dog's name
        '''
        self.name = name

    def __str__(self) -> str:
        '''
        Method returning str name of dog
        :return: dog name
        '''
        return self.name

    def say(self) -> None:
        '''
        Printing the sound Dog makes
        :return: None
        '''
        print('"Гав!"')
