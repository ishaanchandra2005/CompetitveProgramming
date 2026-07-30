t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    diff = []
    for i in range(n):
        diff.append(y[i] - x[i])
    diff.sort()
    # print(diff)
    neg = []
    pos = []
    for i in range(n):
        if diff[i] < 0:
            neg.append(diff[i])
        else:
            pos.append(diff[i])
    # print(neg)
    pos.sort(reverse = True)
    # print(pos)
    ans = 0
    i = 0
    j = 0
    while i < len(neg) and j < len(pos):
        if pos[j] >= abs(neg[i]):
            ans += 1
            i += 1
            j += 1
        else:
            i += 1
    ans = ans + (len(pos) - j) // 2
    print(ans)



