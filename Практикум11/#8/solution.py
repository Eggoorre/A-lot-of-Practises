with open('input.txt', 'r', encoding='utf-8') as f:
    steps_list = [int(line.strip()) for line in f]

months = [
    (steps_list[:31], 31),
    (steps_list[31:59], 28),
    (steps_list[59:90], 31),
    (steps_list[90:120], 30),
    (steps_list[120:151], 31),
    (steps_list[151:181], 30),
    (steps_list[181:212], 31),
    (steps_list[212:243], 31),
    (steps_list[243:273], 30),
    (steps_list[273:304], 31),
    (steps_list[304:334], 30),
    (steps_list[334:365], 31)
]

with open('output.txt', 'w', encoding='utf-8') as o:
    for days, divisor in months:
        avg = sum(days) / divisor
        o.write(f"{avg:.2f}\n")