t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    a = False
    for num in arr:
        if num == k:
            print("YES")
            a = True
            break
    if not a:
        print("NO")