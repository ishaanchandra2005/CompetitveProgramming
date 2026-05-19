t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n == 1:
        print("YES")
    else:
        if k >= 2:
            print("YES")
        elif k == 1 and arr == sorted(arr):
            print("YES")
        else:
            print("NO")