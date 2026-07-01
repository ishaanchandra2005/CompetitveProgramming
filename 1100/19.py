t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    nig = 0
    s = 0
    for i in range(n):
        if arr[i] < 0:
            nig += 1
        s += abs(arr[i])
    if nig % 2 == 0:
        print(s)
    else:
        minig = float('inf')
        for i in range(n):
            minig = min(minig, abs(arr[i]))
        print(s - 2 * minig)