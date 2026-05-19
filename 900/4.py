t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = b
    for x in arr:
        ans += min(x, a - 1)
    print(ans)