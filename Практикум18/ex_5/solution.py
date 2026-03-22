class Game:
    '''
    class making basketball game

    Attributes:
        commands(dict): dict of commands where key is command and its number
         and value commands name

    Methods:

        ball_thrown(): returning none, summing points to the team which won
        get_score(tuple): shows score of game
        get_winner(str): returning winner if it was in the game
    '''
    def __init__(self, commands: dict[str: str]) -> None:
        self.command1 = commands['command1']
        self.command2 = commands['command2']
        self.score = {self.command1: 0, self.command2: 0}

    def ball_thrown(self, command_num: int, points: int) -> None:
        '''
        method adding points to the team which won round
        :param command_num(int): command's number
        :param points(int): nimber of points to be added
        :return: None
        '''
        match command_num:
            case 1:
                self.score[self.command1] += points
            case 2:
                self.score[self.command2] += points

    def get_score(self) -> tuple[int, int]:
        '''
        method returning score where first el is team1 and second el is team2
        :return: tuple[int, int]
        '''
        score_com_1 = self.score[self.command1]
        score_com_2 = self.score[self.command2]

        return score_com_1, score_com_2

    def get_winner(self) -> str:
        '''
        method returning str of which team won
        if score is in the middle it prints draw
        :return: result of game
        '''
        if self.score[self.command1] > self.score[self.command2]:
            return self.command1
        if self.score[self.command1] < self.score[self.command2]:
            return self.command2
        if self.score[self.command1] == self.score[self.command2]:
            return 'Ничья'
