t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 9:
        print(n)    
    elif n < 1000:
        print(9 + (n // 10))
    elif n < 1000:
        print(18 + (n // 100))
    elif n < 10000:
        print(27 + (n // 1000))
    elif n < 100000:
        print(36 + (n // 10000))
    else:
        print(45 + (n // 100000))
            
        