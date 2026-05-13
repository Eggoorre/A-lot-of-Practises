class NavalBattle:
    '''
    A class representing the game 'Battleship'.

    Class attributes:
        playing_field (list[list[int | str]]): a 10x10 game field where:
            0 — empty cell
            1 — ship (hidden from players)
            'o' — miss
            player's symbol — hit

    Instances of this class represent players.
    '''

    playing_field = [[0] * 10 for _ in range(10)]

    def __init__(self, symbol):
        '''
        Initialize a player.

        Args:
            symbol (str): the symbol used to mark this player's successful hits
        '''
        self.symbol = symbol

    @staticmethod
    def show():
        '''
        Display the game field.

        Hidden cells (0 and 1) are shown as '~'.
        Missed shots are shown as 'o'.
        Successful hits are shown using the corresponding player's symbol.
        '''
        for row in NavalBattle.playing_field:
            line = ''
            for cell in row:
                if cell == 0 or cell == 1:
                    line += '~'
                else:
                    line += str(cell)
            print(line.strip())

    def shot(self, x, y):
        '''
        Make a shot at the given coordinates.

        Coordinates start from (1, 1) at the top-left corner.

        Args:
            x (int): column number (1–10)
            y (int): row number (1–10)

        Prints:
            'hit' if a ship is hit
            'miss' if no ship is at the position
            'already shot' if the cell was already targeted
            'invalid coordinates' if input is out of bounds
        '''
        x -= 1
        y -= 1

        cell = NavalBattle.playing_field[y][x]

        if cell == 1:
            NavalBattle.playing_field[y][x] = self.symbol
            print('попал')
        elif cell == 0:
            NavalBattle.playing_field[y][x] = 'o'
            print('мимо')
        else:
            print('уже обстрелян')


NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1 = NavalBattle('#')
player2 = NavalBattle('*')
NavalBattle.show()
player1.shot(6, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)
player2.show()
player1.shot(1, 1)
NavalBattle.show()
