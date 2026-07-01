t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mp = {}
    for val in arr:
        if val in mp:
            mp[val] += 1
        else:
            mp[val] = 1
    ok = 0
    for num in mp.values():
        if num == 1:
            ok = 1
            break
    if ok:
        print(-1)
        continue
    i = 0
    x = 1
    ans = []
    while i < n - 1:
        if arr[i] != arr[i + 1]:
            ans.append(x)
            x = i + 2
        else:
            ans.append(i + 2)
        i += 1
    ans.append(x)
    print(*ans)
    
        