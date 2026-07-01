def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = []
        for i in range(n):
            candidates = []
            for j in range(i + 1, n):
                s = a[i] + a[j]
                candidates.append(s // 2)
                candidates.append(s // 2 + 1)
            if not candidates:
                ans.append(0)
                continue
            best = 0
            for k in candidates:
                cnt = 0
                for j in range(i + 1, n):
                    if abs(a[i] - k) > abs(a[j] - k):
                        cnt += 1
                best = max(best, cnt)
            ans.append(best)
        print(*ans)