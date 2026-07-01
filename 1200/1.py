t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    A = []
    for i in range(n):
        A.append((a[i], i))
    A.sort(reverse=True)
    A = A[:3]
    
    B = []
    for i in range(n):
        B.append((b[i], i))
    B.sort(reverse=True)
    B = B[:3]
    
    C = []
    for i in range(n):
        C.append((c[i], i))
    C.sort(reverse=True)
    C = C[:3]
    
    ans = 0
    for x, i in A:
        for y, j in B:
            for z, k in C:
                if i == j or j == k or i == k:
                    continue
                ans = max(x + y + z, ans)
    print(ans)