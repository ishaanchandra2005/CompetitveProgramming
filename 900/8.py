t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    k = 2
    ans = 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            k += 1
            ans = max(ans, k)
        else:
            k = 2
    print(ans)
    
    
    