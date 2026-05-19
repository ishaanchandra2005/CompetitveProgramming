t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    b = []
    c = []
    if arr[0] == arr[-1]:
        print(-1)
        continue
    b.append(arr[0])
    for i in range(1, n):
        if arr[0] == arr[i]:
            b.append(arr[i])
        else:
            c.append(arr[i])
    print(len(b), len(c))
    print(*b)
    print(*c)