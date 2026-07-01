t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    mx = n * (n - 1) // 2
    possible_edges = (n - 1 <= m <= mx)
    if n == 1:
        if m == 0 and k > 1:
            print("YES")
        else:
            print("NO")
    elif not possible_edges:
        print("NO")
    elif m == mx:
        if k > 2:
            print("YES")
        else:
            print("NO")
    else:
        if k > 3:
            print("YES")
        else:
            print("NO")