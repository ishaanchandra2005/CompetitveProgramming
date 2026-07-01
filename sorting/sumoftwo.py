n, target = map(int, input().split())
arr = list(map(int, input().split()))
mp = {}
if target == 1:
    print("IMPOSSIBLE")
else: 
    for i in range(n):
        need = target - arr[i]
        if need in mp:
            print(mp[need] + 1, i + 1)
            break
        mp[arr[i]] = i
    else:
        print("IMPOSSIBLE")
