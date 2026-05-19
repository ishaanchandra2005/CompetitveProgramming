t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(*arr)
        continue
    for i in range(n):
        if arr[i] == 1:
            arr[i] += 1
    for i in range(n - 1):
        if arr[i + 1] % arr[i] == 0:
            arr[i + 1] += 1
    print(*arr)