with open('input.txt', 'r', encoding='utf-8') as file:
    info = file.read()
    content = info.upper()
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(content)