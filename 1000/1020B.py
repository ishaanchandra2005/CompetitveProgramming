n = int(input())
a0 = [0]
a1 = list(map(int, input().split()))
arr = a0 + a1
ans = []
def dfs(x):
    if vis[x]:
        ans.append(x)
        return
    else:
        vis[x] = 1
        dfs(arr[x])
    return
    
for i in range(1, n + 1):
    if arr[i] == i:
        ans.append(i)
        pass
    else:
        vis = [0] * (n + 1)
        dfs(i)
print(*ans)