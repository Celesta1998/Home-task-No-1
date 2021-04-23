N=5
a = [input(str(b + 1) + '-ая: ') for b in range(N)]
max_len = max([len(b) for b in a])
[print(b+1,end =' ') for b in range(N) if len(a[b]) == max_len]
