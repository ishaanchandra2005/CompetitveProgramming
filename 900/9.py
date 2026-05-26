from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    g = 0
    for i in range(n):
        g = gcd(g, abs(arr[i] - (i + 1)))
    print(g)