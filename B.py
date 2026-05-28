t = int(input())

for _ in range(t):

    n = int(input())

    arr = list(map(int, input().split()))

    desc = []

    for i in range(n - 1):

        if arr[i] > arr[i + 1]:
            desc.append(i)

    if len(desc) == 0:
        print("YES")
        continue

    kmin = 0

    for d in desc:
        kmin = max(kmin, arr[d] - arr[d + 1])

    kmax = float('inf')

    ok = 1

    for i in range(len(desc) - 1):

        l = desc[i] + 1
        r = desc[i + 1]

        best = -1

        for j in range(l - 1, r):

            if arr[j + 1] > arr[j]:
                best = max(best, arr[j + 1] - arr[j])

        if best == -1:
            ok = 0
            break

        kmax = min(kmax, best)

    last = desc[-1]

    for i in range(last + 1, n - 1):

        if arr[i] > arr[i + 1]:
            ok = 0
            break

    if ok == 1 and kmin <= kmax:
        print("YES")
    else:
        print("NO")