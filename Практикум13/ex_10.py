def num_finder(a, b):
    digits_list = [1, 3, 4, 8, 9]
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        for j in str(i):
            if int(j) in digits_list:
                print(i)
                break


num_start = int(input())
num_end = int(input())
num_finder(num_start, num_end)