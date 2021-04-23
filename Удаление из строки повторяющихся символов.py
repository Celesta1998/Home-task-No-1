a = input()
a_new = ''
for b in range(len(a)):
    if a_new.find(a[b]) == -1 and a[b] != ' ':
        a_new += a[b]
print(a_new)
