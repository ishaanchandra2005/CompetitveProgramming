t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    arr.sort()
    mp = {}
    for ch in arr:
        if ch in mp:
            mp[ch] += 1
        else:
            mp[ch] =                        
    # print(mp)
    x = sorted(mp.keys())
    ans = mp[x[0]]
    k = len(mp)
    for i in range(k - 1):
        if x[i] + 1 == x[i + 1]:
            ans += max(0, mp[x[i + 1]] - mp[x[i]])
        else:
            ans += mp[x[i + 1]]
    print(ans)
