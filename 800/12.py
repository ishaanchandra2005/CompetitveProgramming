t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    ans.append(arr[0])
    for i in range(1, n):
        if arr[i - 1] <= arr[i]:
            ans.append(arr[i])
            continue
        else:
            ans.append(1)
            ans.append(arr[i])
    print(len(ans))
    print(*ans)
        