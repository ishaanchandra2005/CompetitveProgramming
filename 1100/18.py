t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] += i + 1
    arr.sort()
    ans = 0
    for i in range(n):
        if k >= arr[i]:
            k -= arr[i]
            ans += 1
        else:
            break
    print(ans)


