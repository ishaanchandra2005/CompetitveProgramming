from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mpA = defaultdict(int)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and A[j] == A[j + 1]:
            j += 1
        mpA[A[i]] = max(mpA[A[i]], j - i + 1)
        i = j + 1
    mpB = defaultdict(int)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and B[j] == B[j + 1]:
            j += 1
        mpB[B[i]] = max(mpB[B[i]], j - i + 1)
        i = j + 1
    ans = 0
    for ch in mpA:
        if ch in mpB:
            ans = max(ans, mpA[ch] + mpB[ch])
    ans = max(ans, max(mpA.values()), max(mpB.values()))
    print(ans)
