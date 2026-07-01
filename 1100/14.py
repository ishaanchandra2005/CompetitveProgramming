t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = 0
    while a[l] == b[l]:
        l += 1
    r = n - 1
    while a[r] == b[r]:
        r -= 1
    while l > 0 and b[l - 1] <= b[l]:
        l -= 1
    while r < n - 1 and b[r] <= b[r + 1]:
        r += 1
    print(l + 1, r + 1)