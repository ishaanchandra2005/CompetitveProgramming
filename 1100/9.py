from math import sqrt
t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    sides = list(map(int, input().split()))
    def check(x):
        s = 0
        for side in sides:
            s += (side + 2 * x) * (side + 2 * x)
            if s > c:
                return c + 1
        return s
    l = 0
    r = int(sqrt(c))
    while l <= r:
        mid = (l + r) // 2
        k = check(mid)
        if k > c:
            r = mid - 1
        elif k < c:
            l = mid + 1
        else:
            print(mid)
            break


        
