import math
l, r, x, y, k = map(int, input().split())
L = max(x, math.ceil(l / k))
R = min(y, r // k)
if L <= R:
    print("YES")
else:
    print("NO")