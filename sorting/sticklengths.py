n = int(input())
arr = list(map(int, input().split()))
arr.sort()
med = arr[n // 2]
ans = 0
for i in range(n):
    ans += abs(arr[i] - med)
print(ans)