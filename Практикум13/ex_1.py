def letters(sen):

    vowels = [str(a) for a in str(sen) if a.lower() in
              ['а', 'у', 'е', 'о', 'ы', 'и', 'я', 'ю', 'э', 'ё']]

    consonants = [str(a) for a in str(sen) if a.lower() in
                  ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
                   'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'щ']]

    print(f'Кол-во гласных: {len(vowels)}\n'
          f'Кол-во согласных: {len(consonants)}')

sentence = input()
letters(sentence)