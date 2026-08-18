t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = n + 1
    y = n + 1
    ans = 0
    for i in range(n):
        if arr[i] <= x:
            x = arr[i]
        elif arr[i] <= y:
            y = arr[i]
        else:
            ans += 1
            if x < y:
                x = arr[i]
            else:
                y = arr[i]
        if x > y:
            x, y = y, x
    print(ans)

