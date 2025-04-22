import os

target_dir = "simple"
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

output_filename = 'output.txt'
with open(output_filename, 'w', encoding='utf-8') as o:
    for i, line in enumerate(lines, 1):
        if i % 2 == 0:
            o.write(line)

destination = os.path.join(target_dir, output_filename)
os.rename(output_filename, destination)