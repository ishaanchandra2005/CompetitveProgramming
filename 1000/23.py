def check(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

t = int(input())
for _ in range(t):
    d = int(input())
    a = d + 1
    while not check(a):
        a += 1
    b = a + d
    while not check(b):
        b += 1
    print(a * b)
        
    
    