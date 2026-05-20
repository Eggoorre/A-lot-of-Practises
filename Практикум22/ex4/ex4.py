import math


def _fmt(value):
    return int(value) if value.is_integer() else value


class GeometricObject:
    """Base class for geometric shapes."""

    def __init__(self, x=0.0, y=0.0, color="black", filled=False):
        self.__x = float(x)
        self.__y = float(y)
        self.color = color
        self.filled = filled

    def set_coordinate(self, x, y):
        """Set the coordinates of the shape."""
        self.__x = float(x)
        self.__y = float(y)

    def set_color(self, color):
        """Set the color of the shape."""
        self.color = color

    def set_filled(self, filled):
        """Set whether the shape is filled."""
        self.filled = filled

    def get_x(self):
        """Return the x coordinate."""
        return self.__x

    def get_y(self):
        """Return the y coordinate."""
        return self.__y

    def get_color(self):
        """Return the color of the shape."""
        return self.color

    def is_filled(self):
        """Return True if the shape is filled."""
        return self.filled

    def __str__(self):
        """Return a string representation for print()."""
        return f"({self.__x}, {self.__y})\ncolor: {self.color}\nfilled: {self.filled}"

    def __repr__(self):
        """Return a string representation for collections."""
        filled_str = "filled" if self.filled else "no filled"
        return f"({_fmt(self.__x)}, {_fmt(self.__y)}) {self.color} {filled_str}"


class Circle(GeometricObject):
    """Circle class inherited from GeometricObject."""

    def __init__(self, x=0.0, y=0.0, radius=0.0, color="black", filled=False):
        super().__init__(x, y, color, filled)
        self.__radius = 0.0
        self.radius = radius

    @property
    def radius(self):
        """Return the radius of the circle."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle if it is not negative."""
        if value >= 0:
            self.__radius = float(value)

    def get_area(self):
        """Return the area of the circle."""
        return math.pi * self.__radius ** 2

    def get_perimetr(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius

    def get_diametr(self):
        """Return the diameter of the circle."""
        return 2 * self.__radius

    def __str__(self):
        """Return a string representation for print()."""
        return f"radius: {self.__radius}\n" + super().__str__()

    def __repr__(self):
        """Return a string representation for collections."""
        return f"radius: {_fmt(self.__radius)} " + super().__repr__()


class Rectangle(GeometricObject):
    """Rectangle class inherited from GeometricObject."""

    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, color="black", filled=False):
        super().__init__(x, y, color, filled)
        self.width = 0.0
        self.height = 0.0
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        """Set the width of the rectangle if it is not negative."""
        if width >= 0:
            self.width = float(width)

    def set_height(self, height):
        """Set the height of the rectangle if it is not negative."""
        if height >= 0:
            self.height = float(height)

    def get_width(self):
        """Return the width of the rectangle."""
        return self.width

    def get_height(self):
        """Return the height of the rectangle."""
        return self.height

    def get_area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def get_perimetr(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation for print()."""
        return f"width: {self.width}\nheight: {self.height}\n" + super().__str__()

    def __repr__(self):
        """Return a string representation for collections."""
        return f"width: {_fmt(self.width)} height: {_fmt(self.height)} " + super().__repr__()