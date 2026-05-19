t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = 0
    for i in range(n - 1):
        if arr[i] % 2 == arr[i + 1] % 2:
            k += 1
    print(k)
    