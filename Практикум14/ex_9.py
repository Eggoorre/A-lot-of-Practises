stop_counter = 0
words_list = []
while stop_counter < 1:
    word = input().lower().strip(',.:-?!')
    if word == '':
        stop_counter += 1
    else:
        words_list.append(word)

new_list = sorted(words_list, key=lambda x: words_list.count(x), reverse=True)
for word in new_list:
    print(word)
