import random


class NavalBattle:
    '''
    A class representing the game 'Battleship'.

    Class attributes:
        playing_field (list[list[int | str]] | None):
            A 10x10 game field where:
                0 — empty cell
                1 — ship (hidden)
                'o' — miss
                player's symbol — hit
            None means the field has not been initialized.

    Instances of this class represent players.
    '''

    playing_field = None

    def __init__(self, symbol):
        '''
        Initialize a player.

        Args:
            symbol (str): symbol used to mark this player's successful hits.
        '''
        self.symbol = symbol

    @staticmethod
    def show():
        '''
        Display the current game field.

        Hidden cells (0 and 1) are shown as '~'.
        Missed shots are shown as 'o'.
        Successful hits are shown using player symbols.

        Prints:
            The visual representation of the field or
            'игровое поле не заполнено' if the field is not initialized.
        '''
        if NavalBattle.playing_field is None:
            print('игровое поле не заполнено')
            return

        for row in NavalBattle.playing_field:
            line = ''
            for cell in row:
                if cell == 0 or cell == 1:
                    line += '~ '
                else:
                    line += str(cell) + ' '
            print(line.strip())

    def shot(self, x, y):
        '''
        Perform a shot at the given coordinates.

        Coordinates are 1-based (top-left corner is (1, 1)).

        Args:
            x (int): column index (1–10)
            y (int): row index (1–10)

        Behavior:
            - If the field is not initialized, prints 'игровое поле не заполнено'
            - If coordinates are invalid, prints 'некорректные координаты'
            - If the cell was already targeted, prints 'ошибка'
            - If a ship is hit, marks it with player's symbol and prints 'попал'
            - If no ship is present, marks 'o' and prints 'мимо'
        '''
        if NavalBattle.playing_field is None:
            print('игровое поле не заполнено')
            return

        x -= 1
        y -= 1

        if not (0 <= x < 10 and 0 <= y < 10):
            print('некорректные координаты')
            return

        cell = NavalBattle.playing_field[y][x]

        if cell not in (0, 1):
            print('ошибка')
            return

        if cell == 1:
            NavalBattle.playing_field[y][x] = self.symbol
            print('попал')
        else:
            NavalBattle.playing_field[y][x] = 'o'
            print('мимо')

    @classmethod
    def new_game(cls):
        '''
        Initialize a new game field and randomly place ships.

        Ships configuration:
            - 1 ship of length 4
            - 2 ships of length 3
            - 3 ships of length 2
            - 4 ships of length 1

        Ships are placed either horizontally or vertically.
        Ships cannot touch each other, even diagonally.

        Result:
            Updates cls.playing_field with a valid random configuration.
        '''
        cls.playing_field = [[0] * 10 for _ in range(10)]

        cls.place_ships(4, 1)
        cls.place_ships(3, 2)
        cls.place_ships(2, 3)
        cls.place_ships(1, 4)

    @classmethod
    def place_ships(cls, length, count):
        '''
        Place a given number of ships of a specific length on the field.

        Args:
            length (int): length of the ship
            count (int): number of ships to place

        Behavior:
            Repeatedly attempts random placement until all ships are placed.
        '''
        placed = 0
        while placed < count:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            horizontal = random.choice([True, False])

            if cls.can_place(x, y, length, horizontal):
                for i in range(length):
                    nx = x + (i if horizontal else 0)
                    ny = y + (0 if horizontal else i)
                    cls.playing_field[ny][nx] = 1
                placed += 1

    @classmethod
    def can_place(cls, x, y, length, horizontal):
        '''
        Check whether a ship can be placed at the given position.

        Args:
            x (int): starting column (0-based)
            y (int): starting row (0-based)
            length (int): ship length
            horizontal (bool): orientation of the ship

        Returns:
            bool: True if placement is valid, False otherwise

        Conditions:
            - Ship must be within field boundaries
            - Ship must not overlap existing ships
            - Ships must not touch each other, even diagonally
        '''
        for i in range(length):
            nx = x + (i if horizontal else 0)
            ny = y + (0 if horizontal else i)

            if not (0 <= nx < 10 and 0 <= ny < 10):
                return False

            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    cx, cy = nx + dx, ny + dy
                    if 0 <= cx < 10 and 0 <= cy < 10:
                        if cls.playing_field[cy][cx] == 1:
                            return False

        return True


player1 = NavalBattle('#')
player1.shot(6, 2)
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
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1, 1)
player1.shot(1, 1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)
