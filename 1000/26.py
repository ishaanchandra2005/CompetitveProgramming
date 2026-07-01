t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    # ans = 1 + (k + k * y - x) // (x - 1) + k
    ans = 1 + (k + k * y - x + (x - 1) - 1) // (x - 1) + k
    print(ans)
