N, d = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
arr.sort(reverse = True)
u = 0
for x in arr:
    n = d // x + 1
    if u + n <= N:
        u += n
        ans += 1
    else:
        break
print(ans)
    
    