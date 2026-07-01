t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(n // 2, n // 2)
    else:
        d = n
        x = 3
        while x * x <= n:
            if n % x == 0:
                d = x
                break
            x += 2
        a = n // d
        print(a, n - a)

