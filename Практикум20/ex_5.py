class RomanNumber:
    '''
    Class that supports both Roman and integer representations
    '''

    ROM_TO_INT = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    INT_TO_ROM = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    REPEATABLE = {'I', 'X', 'C', 'M'}

    @staticmethod
    def is_int(value: int) -> bool:
        '''
        Check if value is a valid integer for Roman numerals.

        Args:
            value (int): Integer to validate.

        Returns:
            bool: True if value is in range [1, 3999], otherwise False.
        '''
        return isinstance(value, int) and 1 <= value <= 3999

    @staticmethod
    def is_roman(value: str) -> bool:
        '''
        Validate if a string is a correct Roman numeral.

        Args:
            value (str): String to validate.

        Returns:
            bool: True if string contains valid Roman numeral symbols
                  and follows repetition rules, otherwise False.
        '''
        if not value:
            return False

        if any(x not in RomanNumber.ROM_TO_INT for x in value):
            return False

        count = 1
        for i in range(1, len(value)):
            if value[i] == value[i - 1]:
                count += 1
                if value[i] not in RomanNumber.REPEATABLE or count > 3:
                    return False
            else:
                count = 1

        return True

    def __init__(self, value):
        '''
        Initialize RomanNumber object.

        Args:
            value (int | str): Integer or Roman numeral.

        Sets:
            int_value (int | None)
            rom_value (str | None)
        '''
        self.rom_value = None
        self.int_value = None

        if isinstance(value, int):
            if self.is_int(value):
                self.int_value = value
                self.rom_value = self.int_to_roman(value)
            else:
                print('ошибка')

        elif isinstance(value, str):
            if self.is_roman(value):
                self.rom_value = value
                self.int_value = self.roman_to_int(value)
            else:
                print('ошибка')

        else:
            print('ошибка')

    def roman_to_int(self, s: str) -> int:
        '''
        Convert Roman numeral to integer.

        Args:
            s (str): Roman numeral string.

        Returns:
            int: Integer representation of the Roman numeral.
        '''
        total = 0
        prev = 0

        for ch in reversed(s):
            val = self.ROM_TO_INT[ch]
            if val < prev:
                total -= val
            else:
                total += val
            prev = val

        return total

    def int_to_roman(self, num: int) -> str:
        '''
        Convert integer to Roman numeral.

        Args:
            num (int): Integer value.

        Returns:
            str: Roman numeral representation.
        '''
        result = []

        for value, symbol in self.INT_TO_ROM:
            while num >= value:
                result.append(symbol)
                num -= value

        return ''.join(result)

    def roman_number(self) -> str:
        '''
        Get Roman numeral representation.

        Returns:
            str: Roman numeral string.
        '''
        return self.rom_value

    def __repr__(self):
        '''
        Return string representation of the object.

        Returns:
            str: Roman numeral representation.
        '''
        return f'{self.rom_value}'


num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))
