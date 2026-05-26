t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    m = 0
    M = 0
    s = 0
    for i in range(n):
        if arr[i] % x == 0:
            M += arr[i] // x
        else:
            M += arr[i] // x + 1
        s += arr[i]
    if s % x == 0:
        m = s // x
    else:
        m = s // x + 1
    print(m, M)
    
        
    