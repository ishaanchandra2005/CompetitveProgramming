t = int(input())
for _ in range(t):
    u, n = map(int, input().split())
    if n % 4 == 0:
        print(u)
    elif n % 4 == 1:
        if u % 2 == 0:
            print(u - n)
        else:
            print(u + n)
    elif n % 4 == 2:
        if u % 2 == 0:
            print(u + 1)
        else:
            print(u - 1)
    else:
        if u % 2 == 0:
            print(u + n + 1)
        else:
            print(u - n - 1)