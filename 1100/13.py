from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    g = 0
    for i in range(n // 2):
        g = gcd(g, abs(arr[i] - arr[n - 1 - i]))
    print(g)