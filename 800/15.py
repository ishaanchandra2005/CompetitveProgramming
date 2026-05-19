t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    o = 0
    for i in range(n):
        if arr[i] % 2 == 1:
            o += 1
    if o % 2 == 0:
        print("YES")
    else:
        print("NO")