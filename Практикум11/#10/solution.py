import datetime as dt

f = open('input.txt', 'r', encoding='utf-8')
o = open('output.txt', 'w', encoding='utf-8')
lines_list = []
current_year =(f'.{dt.datetime.today().year}')
for line in f:
    line = line.strip()
    lines_list.append(line)
current_date = dt.datetime.strptime(
    str(lines_list[0])
    + str(current_year),
    '%d.%m.%Y').date()

for i in lines_list:
    if i != lines_list[0] and i != lines_list[1]:
        box_num = i.split()[0]
        date = dt.datetime.strptime(
            str(i.split()[1]
                + current_year),
            '%d.%m.%Y').date()
        time_difference = current_date - date
        if time_difference > dt.timedelta(days=3):
            answ = (f'{box_num} \n')
            o.write(answ)

