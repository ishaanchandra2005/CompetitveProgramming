t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    pref = [0] * n
    seen = set()
    for i in range(n):
        seen.add(s[i])
        pref[i] = len(seen)
    suff = [0] * n
    seen.clear()
    for i in range(n - 1, -1, -1):
        seen.add(s[i])
        suff[i] = len(seen)
    ans = 0
    for i in range(n - 1):
        ans = max(ans, pref[i] + suff[i + 1])
    print(ans)