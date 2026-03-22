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
        return f'{(self.x_coord, self.y_coord)}'

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


class Segment:
    '''
    class making segment made of two points

    Arguments:
        point1(Point): object which shows start of segment
        point2(Point): object which shows end of segment
    Methods:
        __str__: returning str version of segment
    '''

    def __init__(self, point1: Point, point2: Point) -> None:
        '''
        initialising segment and finding if
        it intersects coordinate plane once
        :param point1: one point where segments stats
        :param point2: other point where segment ends
        '''

        x1 = point1.x_coord
        y1 = point1.y_coord
        x2 = point2.x_coord
        y2 = point2.y_coord

        self.segm = ((x1, y1), (x2, y2))

        if ((y1 == 0) or (y2 == 0) or (y1 * y2 < 0)) and x1 * x2 > 0:
            self.one_intersection = True

        elif ((x1 == 0) or (x2 == 0) or (x1 * x2 < 0)) and y1 * y2 > 0:
            self.one_intersection = True

        else:
            self.one_intersection = False

    def __str__(self) -> str:
        '''
        returning str form of segment
        :return: string
        '''
        return f'{self.segm}'


class СoordinateSystem:
    '''
    class making coordinate system made of segments

    Methods:
        add_segment(): adds Segment in the list of segments
        axis_intersection(): finds the num of segments
        intersecting coordinate plane once
    '''

    def __init__(self):
        '''
        initialising CoordinateSystem
        '''
        self.segments_not_to_show = []
        self.segments = []

    def __str__(self):
        '''
        returning str version of CoordinateSystem
        :return: string
        '''
        return f'{self.segments}'

    def add_segment(self, segment: Segment) -> None:
        '''
        adding one more segment in CoordinateSystem
        :param segment:
        :return: None
        '''
        to_show = segment.segm
        self.segments.append(to_show)
        self.segments_not_to_show.append(segment)

    def axis_intersection(self) -> int:
        '''
        finding num of once intersecting coordinate plane segments in CoordinateSystem
        :return: int
        '''
        return sum(1 for seg in self.segments_not_to_show if seg.one_intersection)
