t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    ans = []
    x = 0

    for i in range(n - 1, -1, -1):

        cur = a[i]

        if x == 1:
            cur = -cur

        if cur > 0:
            ans.append(i + 1)

            if x == 0:
                x = 1
            else:
                x = 0

    ans.reverse()

    print(len(ans))

    if len(ans) > 0:
        print(*ans)