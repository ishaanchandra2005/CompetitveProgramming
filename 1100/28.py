t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    i = n - 2
    k = 1
    while i >= 0:
        if arr[i] == arr[n - 1]:
            k += 1
            i -= 1
        else:
            ans += 1
            i -= k
            k *= 2
    print(ans)


