answer = input()
hint = input()
answ_l = [x for x in answer]
word = [y for y in len(answ_l) * '*']
print('\n' * 25)
print(hint)
print(*word, sep='')
for i in range(1, 10):
    a = int(input(f'Буква или слово(0 - буква, 1 - слово)?'))
    if a == 0:
        letter = input()
        for j in range(0, len(word)):
            if letter == answ_l[j]:
                word[j] = letter

    elif a == 1:
        win_answ = input()
        if win_answ == answer:
            print(f'Поздравляем! Вы победили!')
            break
    print(*word, sep='')

else:
    print('Закончились ходы(')