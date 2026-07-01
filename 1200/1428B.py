t = int(input())
for _ in range(t):
    n = int(input())
    s = input() 
    if '>' not in s or '<' not in s:
        print(n)
        continue
    ans = 0
    vis = [0] * n    
    for i in range(n):
        if s[i] == '-':
            vis[i] = 1
            vis[(i + 1) % n] = 1
    ans = sum(vis)
    print(ans)
            
            
        