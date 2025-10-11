def seconds_left(a):
    t = a.split()
    calendar_time = t[0].split('/')
    months = int(calendar_time[0])
    days = int(calendar_time[1])
    years = int(calendar_time[2])

    clock_time = t[1].split(':')
    hours = int(clock_time[0])
    minutes = int(clock_time[1])
    seconds = int(clock_time[2])

    seconds_in_day = seconds + minutes * 60 + hours * 3600

    if (months > 12 or months < 1 or hours >= 24 or minutes >= 60 or seconds >= 60):
        return 'Ошибка'

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if days < 1 or days > days_in_month[months - 1]:
        return 'Ошибка'

    month_days_list = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    seconds_total = ((days - 1) * 86400 + month_days_list[months - 1]
                     * 86400 + seconds_in_day)

    return seconds_total


date = input(f'Введите дату и время: ')
print(seconds_left(date))