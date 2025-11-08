sentence = input()

words_with_marks = sentence.split()

unique_words_without_marks = list(set(x.strip('.,:;?!-()')
                                      for x in words_with_marks))

print(unique_words_without_marks)
