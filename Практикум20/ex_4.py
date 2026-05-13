class RomanNumber:
    '''A class for working with Roman numerals: validation and conversion to decimal numbers.'''

    VALID = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}

    REPEATABLE = {'I', 'X', 'C', 'M'}

    SUBTRACTABLE = {
        'I': {'V', 'X'},
        'X': {'L', 'C'},
        'C': {'D', 'M'}
    }

    @staticmethod
    def is_roman(value: str) -> bool:
        '''
        Checks whether a string is a valid Roman numeral.

        Rules:
        - only symbols I, V, X, L, C, D, M are allowed
        - I, X, C, M can be repeated at most 3 times in a row
        - subtraction rules must be valid (e.g. IV, IX, XL, etc.)
        '''
        if not value:
            return False

        if any(x not in RomanNumber.VALID for x in value):
            return False

        count = 1
        for i in range(1, len(value)):
            if value[i] == value[i - 1]:
                count += 1
                if value[i] not in RomanNumber.REPEATABLE or count > 3:
                    return False
            else:
                count = 1

        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(value) - 1):
            cur, nxt = value[i], value[i + 1]
            if nums[cur] < nums[nxt]:
                if cur not in RomanNumber.SUBTRACTABLE or nxt not in RomanNumber.SUBTRACTABLE[cur]:
                    return False

        return True

    def __init__(self, num: str):
        '''
        Creates a RomanNumber instance.

        If the input string is invalid, the value is set to None.
        '''
        if not self.is_roman(num):
            self.rom_value = None
            print('Ошибка')
        else:
            self.rom_value = num

    def __repr__(self):
        '''
        Returns a string representation of the object.
        '''
        return f'{self.rom_value}'

    def decimal_number(self):
        '''
        Converts the Roman numeral to its decimal representation.

        Returns:
            int: decimal value of the Roman numeral
            None: if the value is invalid
        '''
        if not self.rom_value:
            return None

        nums_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}

        total = 0
        prev = 0

        for el in reversed(self.rom_value):
            value = nums_dict[el]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total


num_1 = RomanNumber('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('XXIV')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('MMMCMLXXXVI'))
print(RomanNumber.is_roman('MMМMMLXXXVI'))
