class Point:
    '''
    class representing a point on a plane

    Attributes:
        x_coord(int): x coordinate of the point
        y_coord(int): y coordinate of the point

    Methods:
        __str__(): returns string representation of point in format (x, y)
        get_x(): returns x coordinate
        get_y(): returns y coordinate
        distance(other): returns distance(float) between two points
        sum(other): returns tuple(int, int) of summed coordinates of two points
    '''

    def __init__(self, coords: tuple[int, int] = (0, 0)) -> None:
        '''
        initializing point coordinates

        :param coords: tuple of x and y coordinates
        '''
        self.x_coord = coords[0]
        self.y_coord = coords[1]

    def __str__(self) -> str:
        '''
        method returning string representation of point

        :return: str
        '''
        return str(f'{(self.x_coord, self.y_coord)}')

    def get_x(self) -> int:
        '''
        method getting x coordinate
        :return: int
        '''
        return self.x_coord

    def get_y(self) -> int:
        '''
        method getting y coordinate
        :return: int
        '''
        return self.y_coord

    def distance(self, other: 'Point') -> float:
        '''
        method returning distance between two points
        :param other: other point
        :return: float num
        '''
        return ((self.x_coord - other.x_coord) ** 2 +
                (self.y_coord - other.y_coord) ** 2) ** 0.5

    def sum(self, other: 'Point') -> tuple[int, int]:
        '''
        method returning sum of two points
        :param other: other point
        :return: tuple of new point made of sum of coordinates of points
        '''
        return self.x_coord + other.x_coord, self.y_coord + other.y_coord
