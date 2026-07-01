t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = float('inf')
    for add in range(31):
        nb = b + add
        if nb == 1:
            continue
        cur = add
        x = a
        while x > 0:
            x //= nb
            cur += 1
        ans = min(ans, cur)
    print(ans)