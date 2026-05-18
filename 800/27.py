t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    two = 0
    for i in range(n):
        if arr[i] == 2:
            two += 1
    k = two // 2
    if two % 2 == 1:
        print(-1)
        continue
    if two == 0:
        print(1)
        continue
    for i in range(n):
        if arr[i] == 2:
            two -= 1
            if two == k:
                print(i + 1)
                break
