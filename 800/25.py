t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    k = 0
    if n == 1:
        print(1)
        continue
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            k += 1
        else:
            break
    ans = n - 2 * k
    print(ans)
    
    