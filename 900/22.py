t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    z = 0
    o = 0
    for x in arr:
        if x == 0:
            z += 1
        elif x == 1:
            o += 1
    print(o * (2 ** z))