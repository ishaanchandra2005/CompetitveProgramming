t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    k = max(h) - min(h) + 1
    print(k)
    