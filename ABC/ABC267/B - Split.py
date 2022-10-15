s = input()
l = [0]
for x in s:
    l.append(x)
l = list(map(int, l))

if l[1] == 1:
    print('No')
    exit()
    
l = [[l[7]],[l[4]], [l[2], l[8]],[l[1], l[5]], [l[3], l[9]], [l[6]], [l[10]]] 

# print(l)
flag = False

for i in range(7):
    if sum(l[i]) >= 1:
        # print(f'i={i}')
        for j in range(i+1,7):
            # print(f'j={j}')
            if sum(l[j]) == 0:
                for k in range(j+1,7):
                    # print(f'k={k}')
                    if sum(l[k]) >= 1:
                        flag = True

if flag: print('Yes')
else: print('No')