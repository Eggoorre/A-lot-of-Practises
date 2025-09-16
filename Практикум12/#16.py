text = input()
brackets_list = [x for x in text if x == '(' or x == ')']
if len(brackets_list) % 2 != 0:
    print('Неправильная постановка скобок!')

else:
    counter = 0
    for bracket in brackets_list:
        if bracket == '(':
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            break
    if counter == 0:
        print('Постановка скобок верна')
    else:
        print('Неправильная постановка скобок!')