t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    if arr[0] != 0:
        ans += 1
    for i in range(1, n):
        if arr[i] != 0 and arr[i - 1] == 0:
            ans += 1
    if ans >= 2:
        ans = 2
    print(ans)
        
            