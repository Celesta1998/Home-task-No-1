from random import randint
a = input()
c = len(a)
for e in range(5):
  d = randint(2,7)
  b = ''
  f = 0
  while f<d:
    g = randint(0,c-1)
    if a[g] != ' ':
      b += a[g]
      f += 1
  print(b)