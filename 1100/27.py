t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    st = set(arr)
    ok = False
    for x in arr:
        if x + k in st:
            ok = True
            break
    if ok:
        print("YES")
    else:
        print("NO")




