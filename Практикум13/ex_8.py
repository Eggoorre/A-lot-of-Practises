def time_change(a):
    t = a.split()
    calendar_time = t[0].split(sep='/')

    months = str(calendar_time[0])
    days = str(calendar_time[1])
    years = str(calendar_time[2])

    clock_time = t[1].split(sep=':')

    hours = int(clock_time[0])
    minutes = int(clock_time[1])
    seconds = int(clock_time[2])

    if (int(months) > 12 or int(days) > 31 or hours >= 24
            or minutes >= 60 or seconds >= 60):
        print(f'Допущена ошибка в вводе времени')

    elif hours >= 12:
        new_hours = str(hours - 12) + 'PM'
        print(f'{days}.{months}.{years[-2:]}'
              f' {new_hours}:{minutes}:{seconds}')
    elif hours < 12:
        new_hours = str(hours) + 'AM'
        print(f'{days}.{months}.{years[-2:]}'
              f' {new_hours}:{minutes}:{seconds}')


date = input(f'Введите дату: ')
time_change(date)
