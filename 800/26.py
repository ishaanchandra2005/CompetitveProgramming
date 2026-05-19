import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    beautiful = False
    for i in range(n):
        for j in range(i + 1, n):
            if math.gcd(arr[i], arr[j]) <= 2:
                beautiful = True
                break
        if beautiful:
            break
    if beautiful:
        print("YES")
    else:
        print("NO")