t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    mp = {}
    for i in range(n):
        if s[i] not in mp:
            mp[s[i]] = 1
        else:
            mp[s[i]] += 1
    f = 0
    for ch in mp:
        if mp[ch] % 2 ==1:
            f += 1
    if f - 1 > k:
        print("NO")
    else:
        print("YES")
            
        