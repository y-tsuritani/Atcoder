n = "1000010000100001"

split_list = n.split('00')
print(split_list)
not_blank_list = [x for x in split_list if x != '']
count = len(not_blank_list)-1
for s in split_list:
    if len(s):
        count += len(s)
    else:
        count += 1
print(count)

