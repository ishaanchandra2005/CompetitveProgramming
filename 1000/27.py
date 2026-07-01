t = int(input())
for _ in range(t):
    n = int(input())
    def check(x):
        temp = x
        while temp:
            d = temp % 10
            if d and x % d:
                return False
            temp //= 10
        return True
    i = n
    while i != 0:
        if check(i):
            print(i)
            break
        i += 1
    
        