t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(2 * i + 1)
    print(*arr)