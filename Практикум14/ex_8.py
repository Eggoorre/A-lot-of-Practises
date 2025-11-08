def str_sort(line: str):
    symbols_list = [x for x in line]
    symbols_list.sort()
    return ''.join(symbols_list)


input_line = input()
print(str_sort(input_line))
