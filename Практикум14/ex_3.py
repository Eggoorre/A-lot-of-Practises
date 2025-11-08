sentence = input()

words_with_marks = sentence.split()

words_without_marks = [x.strip('.,:;?!-()') for x in words_with_marks]

print(words_without_marks)
