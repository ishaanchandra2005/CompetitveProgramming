t = int(input())
for _ in range(t):
    n = input()
    ans = 10**9
    pairs = ["00", "25", "50", "75"]
    for pair in pairs:
        second = pair[1]
        first = pair[0]
        pos2 = -1
        pos1 = -1
        for i in range(len(n) - 1, -1, -1):
            if n[i] == second:
                pos2 = i
                break
        if pos2 == -1:
            continue
        for i in range(pos2 - 1, -1, -1):
            if n[i] == first:
                pos1 = i
                break
        if pos1 == -1:
            continue
        deletions = (len(n) - pos2 - 1) + (pos2 - pos1 - 1)
        ans = min(ans, deletions)
    print(ans)