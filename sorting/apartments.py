n, m, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()
i = 0
j = 0
ans = 0
while i < n and j < m:
    if abs(arr1[i] - arr2[j]) <= k:
        ans += 1
        i += 1
        j += 1
    elif arr2[j] < arr1[i] - k:
        j += 1
    else:
        i += 1
print(ans)