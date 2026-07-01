t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + arr[i]
    ans = 0
    for i in range(k + 1):
        left = 2 * i
        right = n - (k - i)
        curr = pref[right] - pref[left]
        ans = max(ans, curr)
    print(ans)






