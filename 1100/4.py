t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pref = [0] * n
    pref[0] = arr[0]
    for i in range(1, n):
        if arr[i] % 2 != arr[i - 1] % 2:
            pref[i] = max(0, pref[i - 1]) + arr[i]
        else:
            pref[i] = arr[i]
    print(max(pref)) 