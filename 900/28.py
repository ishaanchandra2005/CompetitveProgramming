t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    f = n * k
    while k > 0:
        f -= (n // 2) + 1
        s += arr[f]
        k -= 1
    print(s)