a = input()
let_a = 0
let_b = 0
for c in a:
    if 'a' <= c <= 'z':
        let_a += 1
    else:
        if 'A' <= c <= 'Z' :
            let_b += 1
print(let_a)
print(let_b)