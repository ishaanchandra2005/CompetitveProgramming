t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = max(arr) - min(arr)
    print((d + 1) // 2)