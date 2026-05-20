from datetime import datetime


class Date:
    """A class for storing and working with a date in the format 'dd.mm.yyyy'."""

    MONTHS = [
        'янв', 'фев', 'мар', 'апр', 'май', 'июн',
        'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'
    ]

    def __init__(self, date_str: str):
        """
        Creates a Date object.

        :param date_str: date in the format 'dd.mm.yyyy'
        """
        self.__date = None
        self.date = date_str

    @staticmethod
    def __is_valid(date_str: str) -> bool:
        """
        Checks the correctness of the date string.

        :param date_str: date string
        :return: True if the date is correct, otherwise False
        """
        try:
            datetime.strptime(date_str, '%d.%m.%Y')
            return True
        except:
            return False

    @property
    def date(self):
        """
        Returns the date in the format 'D month YYYY'.

        :return: a string with a date, or None if no date is specified
        """
        if self.__date is None:
            return None

        dt = datetime.strptime(self.__date, '%d.%m.%Y')
        month = self.MONTHS[dt.month - 1]
        return f'{dt.day} {month} {dt.year} г.'

    @date.setter
    def date(self, value: str):
        """
        Sets the correct date.

        :param value: date in the format 'dd.mm.yyyy'
        """
        if self.__is_valid(value):
            self.__date = value
        else:
            print('ошибка')
            self.__date = None

    def to_timestamp(self) -> int:
        """
        Returns the number of seconds since 01.01.1970.

        :return: timestamp or None if no date is set
        """
        if self.__date is None:
            return None

        dt = datetime.strptime(self.__date, '%d.%m.%Y')
        return int(dt.timestamp())

    def __get_dt(self):
        """
        Converts an internal date to a datetime object.

        :return: datetime or None
        """
        if self.__date is None:
            return None
        return datetime.strptime(self.__date, '%d.%m.%Y')

    def __str__(self):
        """String representation of the date"""
        return self.date if self.date is not None else 'None'

    def __eq__(self, other):
        """A test of equality"""
        return self.__get_dt() == other.__get_dt()

    def __ne__(self, other):
        """Checking for inequality"""
        return self.__get_dt() != other.__get_dt()

    def __lt__(self, other):
        """Less"""
        return self.__get_dt() < other.__get_dt()

    def __le__(self, other):
        """Less than or equal to"""
        return self.__get_dt() <= other.__get_dt()

    def __gt__(self, other):
        """More"""
        return self.__get_dt() > other.__get_dt()

    def __ge__(self, other):
        """Greater than or equal to"""
        return self.__get_dt() >= other.__get_dt()