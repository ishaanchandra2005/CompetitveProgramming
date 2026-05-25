t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0, 0)
    else:
        d = abs(a - b)
        print(d, min(a % d, d - (a % d)))