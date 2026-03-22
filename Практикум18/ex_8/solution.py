class MorseMsg:
    '''
    A class for decoding Morse code messages into English or Russian text,
    and analyzing the decoded result.

    Attributes:
        msg (str): Original Morse code message (symbols separated by spaces).
        msg_eng_decode (list[str]): List of decoded English characters.
        msg_ru_decode (list[str]): List of decoded Russian characters.
    '''

    def __init__(self, msg: str) -> None:
        '''
        Initialise MorseMsg object
        :param msg: message in Morse code
        '''
        self.msg = msg
        self.msg_eng_decode = []
        self.msg_ru_decode = []

    def __str__(self) -> str:
        '''
        Return string representation of the object

        :return: Original Morse code message
        '''
        return self.msg

    def eng_decode(self) -> str:
        '''
        Decode Morse code message into English text.

        Notes:
            - Unknown Morse sequences are replaced with '?'.
            - Result is also stored in self.msg_eng_decode.
        :return: str of decoded msg
        '''
        morse_dict = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
            '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
            '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
            '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z'
        }

        for letter in self.msg.strip().split():
            self.msg_eng_decode.append(morse_dict.get(letter, '?'))

        return ''.join(self.msg_eng_decode)

    def ru_decode(self) -> str:
        '''
        Decode Morse code message into English text.

        Notes:
            - Unknown Morse sequences are replaced with '?'.
            - Result is also stored in self.msg_eng_decode.
        :return: str of decoded msg
        '''
        morse_dict = {
            '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
            '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
            '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
            '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
            '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
            '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь',
            '..-..': 'Э', '..--': 'Ю', '.-.-': 'Я'
        }

        for letter in self.msg.strip().split():
            self.msg_ru_decode.append(morse_dict.get(letter, '?'))

        return ''.join(self.msg_ru_decode)

    def get_vowels(self, lang: str) -> list:
        '''
        Getting vowels from the translated messages with choosing language
        :param lang(str): language to choose
        :return: list of vowels of chosen language
        '''
        vowels_to_print_rus = []
        vowels_to_print_eng = []
        match lang:
            case 'eng':
                for letter in self.msg_eng_decode:
                    if letter.lower() in {'a', 'e', 'i', 'o', 'u', 'y'}:
                        vowels_to_print_eng.append(letter)
                return vowels_to_print_eng
            case 'ru':
                for letter in self.msg_ru_decode:
                    if letter.lower() in {'а', 'о', 'у', 'ы', 'э',
                                          'я', 'ё', 'ю', 'е'}:
                        vowels_to_print_rus.append(letter)
                return vowels_to_print_rus

    def get_consonants(self, lang: str) -> list:
        '''
        Getting consonants from the translated messages with choosing language
        :param lang(str): language to choose
        :return: list of consonants of chosen language
        '''
        consonants_to_print_rus = []
        consonants_to_print_eng = []
        match lang:
            case 'eng':
                for letter in self.msg_eng_decode:
                    if letter.lower() in {'b', 'c', 'd', 'f', 'g', 'h',
                                          'j', 'k', 'l', 'm', 'n', 'p',
                                          'q', 'r', 's', 't', 'v', 'x',
                                          'z'}:
                        consonants_to_print_eng.append(letter)
                return consonants_to_print_eng
            case 'ru':
                for letter in self.msg_ru_decode:
                    if letter.lower() in {'б', 'в', 'г', 'д', 'ж', 'з', 'й',
                                          'к', 'л', 'м', 'н', 'п', 'р', 'с',
                                          'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'}:
                        consonants_to_print_rus.append(letter)
                return consonants_to_print_rus
