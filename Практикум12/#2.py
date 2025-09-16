t = input()
counter = 1
max_count = 1
l_list = []
for l in t:
    l_list.append(l)
for i in range(1, len(l_list)):
    if l_list[i] == l_list[i - 1]:
        counter += 1
        if counter > max_count:
            max_count = counter
    else:
        counter = 1
print(max_count)
