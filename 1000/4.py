t = int(input())
for _ in range(t):
    n = int(input())
    m1 = []
    m2 = []
    for i in range(n):
        m = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        m1.append(arr[0])
        m2.append(arr[1])
    ans = min(m1)
    m2.sort()
    ans += sum(m2[1 : ])
    print(ans)
        
            