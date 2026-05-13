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
        return isinstance(value, int) and 1 <= value <= 3999

    @staticmethod
    def is_roman(value: str) -> bool:
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

    def __init__(self, value=None):
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

    def roman_to_int(self, s: str) -> int:
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
        result = []

        for value, symbol in self.INT_TO_ROM:
            while num >= value:
                result.append(symbol)
                num -= value

        return ''.join(result)

    def roman_number(self) -> str:
        return self.rom_value

    def __repr__(self):
        return f'{self.rom_value}'

    @staticmethod
    def _error():
        print('ошибка')
        return RomanNumber()

    def _get_other(self, other):
        if isinstance(other, RomanNumber):
            return other.int_value
        elif isinstance(other, int):
            return other
        return None

    def __add__(self, other):
        val = self._get_other(other)
        if val is None:
            return NotImplemented
        result = self.int_value + val
        return RomanNumber(result) if self.is_int(result) else self._error()

    def __sub__(self, other):
        val = self._get_other(other)
        if val is None:
            return NotImplemented
        result = self.int_value - val
        return RomanNumber(result) if self.is_int(result) else self._error()

    def __mul__(self, other):
        val = self._get_other(other)
        if val is None:
            return NotImplemented
        result = self.int_value * val
        return RomanNumber(result) if self.is_int(result) else self._error()

    def __truediv__(self, other):
        val = self._get_other(other)
        if val in (None, 0):
            return self._error()
        result = self.int_value / val
        if result.is_integer():
            result = int(result)
            return RomanNumber(result) if self.is_int(result) else self._error()
        return self._error()

    def __floordiv__(self, other):
        val = self._get_other(other)
        if val in (None, 0):
            return self._error()
        result = self.int_value // val
        return RomanNumber(result) if self.is_int(result) else self._error()

    def __mod__(self, other):
        val = self._get_other(other)
        if val in (None, 0):
            return self._error()
        result = self.int_value % val
        return RomanNumber(result) if self.is_int(result) else self._error()

    def __pow__(self, other):
        val = self._get_other(other)
        if val is None:
            return NotImplemented
        result = self.int_value ** val
        return RomanNumber(result) if self.is_int(result) else self._error()

    def __iadd__(self, other):
        return self._assign(self + other)

    def __isub__(self, other):
        return self._assign(self - other)

    def __imul__(self, other):
        return self._assign(self * other)

    def __itruediv__(self, other):
        return self._assign(self / other)

    def __ifloordiv__(self, other):
        return self._assign(self // other)

    def __imod__(self, other):
        return self._assign(self % other)

    def __ipow__(self, other):
        return self._assign(self ** other)

    def _assign(self, other):
        self.int_value = other.int_value
        self.rom_value = other.rom_value
        return self


a = RomanNumber('XI')
b = RomanNumber('VII')
c = a + b
print(c)
d = RomanNumber('XII')
print(c - d)
e = RomanNumber('XXXIV')
f = e * a
print(f)
print(f / RomanNumber('II'))
g = f / b
print(g.rom_value)
print(f // b)
print(f % b)
print(RomanNumber('II') ** RomanNumber('X'))
a -= b
print(a)
b += RomanNumber('XX')
print(b)
b /= RomanNumber('III')
print(b)
b *= a
print(b)
b /= RomanNumber('X')
print(b)
e //= RomanNumber('X')
print(e)
e %= RomanNumber('II')
print(e)
