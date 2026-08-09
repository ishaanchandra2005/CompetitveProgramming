t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    gaps = []
    for i in range(1, len(arr)):
        gaps.append(arr[i] - arr[i - 1] - 1)
    gaps.append(n - arr[-1] + arr[0] - 1)
    gaps.sort(reverse=True)
    # print(gaps)
    days = 0
    ans = n
    for g in gaps:
        g -= 2 * days
        if g <= 0:
            continue
        if g == 1:
            ans -= 1
            days += 1
        else:
            ans -= g - 1
            days += 2
    print(ans)
