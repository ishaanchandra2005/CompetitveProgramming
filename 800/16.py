t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr != sorted(arr):
        print(0)
        continue
    bleh = float('inf')
    for i in range(n - 1):
        k = arr[i + 1] - arr[i]
        bleh = min(bleh, k)
    print(bleh // 2 + 1)