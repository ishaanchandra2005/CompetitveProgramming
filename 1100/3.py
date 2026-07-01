t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = []
    for i in range(n):
        k.append([arr[i], i])
    k.sort()
    pref = [0] * n
    pref[0] = k[0][0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + k[i][0]
    reach = [0] * n
    reach[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        if pref[i] >= k[i + 1][0]:
            reach[i] = reach[i + 1]
        else:
            reach[i] = i
    ans = [0] * n
    for i in range(n):
        ans[k[i][1]] = reach[i]
    print(*ans)

