n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
prev = [False] * (total + 1)
prev[0] = True
for coin in arr:
    curr = prev[:]
    for s in range(total + 1):
        if s - coin >= 0:
            curr[s] = curr[s] or prev[s - coin]
    prev = curr
ans = []
for s in range(1, total + 1):
    if prev[s]:
        ans.append(s)
print(len(ans))
print(*ans)