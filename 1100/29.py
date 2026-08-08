from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in range(0, n, 2):
        even = gcd(even, arr[i])
    for i in range(1, n, 2):
        odd = gcd(odd, arr[i])
    ok = True
    for i in range(1, n, 2):
        if arr[i] % even == 0:
            ok = False
            break
    if ok:
        print(even)
        continue
    ok = True
    for i in range(0, n, 2):
        if arr[i] % odd == 0:
            ok = False
            break
    if ok:
        print(odd)
    else:
        print(0)