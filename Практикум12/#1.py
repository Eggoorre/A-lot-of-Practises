t = input()
counter = 0
max = 0
for letter in t:
    if letter.isspace():
        counter += 1
        if counter > max:
            max = counter
    else:
        counter = 0
print(max)
