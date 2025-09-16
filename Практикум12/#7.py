t = 'Барбарики разбились въехав в бетон'
list = [x.lower() for x in t.split()]
list_num = []
for i in list:
    list_num.append(len(i))
print(min(list_num))