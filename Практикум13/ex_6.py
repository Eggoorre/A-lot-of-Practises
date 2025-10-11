def length(string):
    if len(string) >= 160:
        return string[:159]
    return string


message = input('Введите сообщение: ')
print(length(message))
