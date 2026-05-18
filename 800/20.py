t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for num in arr:
        ans.append(n + 1 - num)
    print(*ans)