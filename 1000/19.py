t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    temp = []
    for i in range(n):
        temp.append([arr[i], i])
    temp.sort(reverse=True)
    pos = [0] * n
    for i in range(n):
        if i % 2 == 0:
            p = i // 2 + 1
        else:
            p = -(i // 2 + 1)
        temp[i].append(p)
        pos[temp[i][1]] = p
    ans = 0
    for i in range(n):
        ans += 2 * abs(pos[i]) * arr[i]
    print(ans)
    print(0, *pos)