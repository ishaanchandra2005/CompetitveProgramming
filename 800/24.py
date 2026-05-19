t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans ^= arr[i]
    if ans == 0:
        print(0)
        continue
    if n % 2 == 1:
        print(ans)
        continue
    else:
        print(-1)