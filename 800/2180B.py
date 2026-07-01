t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    s = ''
    for x in arr:
        s = min(s + x, x + s)
    print(s)
        
    