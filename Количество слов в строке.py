a = input()
count = 0
flag = 0
for b in range(len(a)):
    if a[b] != ' ' and flag == 0:
        count += 1
        flag = 1
    else:
        if a[b] == ' ':
            flag = 0
print(count)