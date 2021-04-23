print('Строка: ')
a = input()
print('Её заменяемая подстрока: ')
a_old = input()
print('Новая подстрока: ')
a_new = input()

b = a.find(a_old)
while b != -1:
    c = len(a_old)
    a = a[0:b] + a_new + a[b+c:]
    b = a.find(a_old)

print(a)