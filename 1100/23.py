t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    ans = []
    ok = True
    for i in range(1, n + 1):
        x = ((l + i - 1) // i) * i
        if x > r:
            ok = False
            break
        ans.append(x)
    if ok:
        print("YES")
        print(*ans)
    else:
        print("NO")