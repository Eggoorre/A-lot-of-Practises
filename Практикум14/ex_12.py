def num_of_hole_let(line):
    list_of_letters = [x.lower for x in line if x in
                       ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']]
    return len(list_of_letters)


def num_of_not_hole_let(line):
    list_of_letters = [x.lower for x in line if x not in
                       ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q', ' ']]
    return len(list_of_letters)


input_line = input()
lst_of_2_or_mr_hl_lts = []

for word in input_line.split():
    if num_of_hole_let(word) >= 2:
        lst_of_2_or_mr_hl_lts.append(word)

print(f'Число букв с отверстиями: {num_of_hole_let(input_line)}\n'
      f'Число букв без отверстий: {num_of_not_hole_let(input_line)}\n'
      f'Список слов с отверстиями: {lst_of_2_or_mr_hl_lts}')
