a = input()
a_new = ""
for b in a:
    if b not in a_new and b != ' ':
        a_new += b
print(a_new)