n = int(input())

fl = [1] * 11
for i in range(1, 11):
    fl[i] = i * fl[i-1] 

print(fl[n])