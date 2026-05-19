t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    neg = arr.count(-1)
    ans = 0
    while s < 0:
        s += 2
        neg -= 1
        ans += 1
    if neg % 2 == 1:
        ans += 1
    print(ans)
        