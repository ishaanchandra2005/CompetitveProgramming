t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for stack in a, b, c:
        for book in stack:
            if book | x != x:
                break
            ans |= book
    if ans == x:
        print("YES")
    else:
        print("NO")
        