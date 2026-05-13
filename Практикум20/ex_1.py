class Circle:
    '''
    A class representing a circle.

    Attributes:
        pi (float): Mathematical constant π used for calculations.
        all_circles (list): A list storing radii of all created Circle instances.
    '''

    pi = 3.1415
    all_circles = []

    def __init__(self, r=1):
        '''
        Initialize a Circle instance.

        Args:
            r (float, optional): Radius of the circle. Defaults to 1.
        '''
        self.radius = r
        Circle.all_circles.append(self.radius)

    def __str__(self):
        '''
        Return a string representation of the circle.

        Returns:
            str: The radius of the circle as a string.
        '''
        return f'{self.radius}'

    def area(self):
        '''
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        '''
        return Circle.pi * (self.radius ** 2)

    @classmethod
    def total_area(cls):
        '''
        Calculate the total area of all created circles.

        Returns:
            float: The sum of areas of all circles.
        '''
        return sum((x ** 2) * cls.pi for x in cls.all_circles)


c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)

print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))