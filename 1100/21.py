from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    bleh = [-1] * 1001
    for i in range(n):
        bleh[arr[i]] = i
    ans = -1
    for i in range(1001):
        if bleh[i] == -1:
            continue
        for j in range(1001):
            if bleh[j] == -1:
                continue
            if gcd(i, j) == 1:
                ans = max(ans, bleh[i] + bleh[j] + 2)
    print(ans)