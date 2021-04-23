a = input()
b = len(a)
c = 0
ind = 0
count = 0
for d in range(b):
    if a[d] != ' ':
        count += 1
    else:
        if count > c:
            c = count
            ind = d - count
            count = 0
if count > c:
    c = count
    ind = d - count + 1
    print(a[ind:ind+c])
