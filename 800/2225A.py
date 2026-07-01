t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y - x <= x:
        print("NO")
    else:
        print("YES")