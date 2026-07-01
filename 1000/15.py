t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    b = 0
    w = 0
    for i in range(k):
        if s[i] == 'W':
            w += 1
    X = w
    for i in range(n - k):
        if s[i] == 'W':
            w -= 1
        if s[k + i] == 'W':
            w += 1
        X = min(X, w)
    print(X)