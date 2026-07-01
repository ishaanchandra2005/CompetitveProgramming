t = int(input())
for _ in range(t):
    n, k, b, s = map(int, input().split())
    if s < k * b or s > k * b + n * (k - 1):
        print(-1)
        continue
    else:
        stuff = s - k * b
        ans = [0] * n
        ans[0] = k * b
        for i in range(n):
            x = min(stuff, k - 1)
            ans[i] += x
            stuff -= x
        print(*ans)