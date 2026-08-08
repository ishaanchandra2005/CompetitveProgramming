t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if '0' not in s:
        print(n * n)
        continue
    s = s + s
    m = len(s)
    i = 0
    x = 0
    while i < m:
        j = i
        k = 0
        while j < m and s[j] == '1':
            k += 1
            j += 1
        x = max(x, k)
        i = j + 1
    a = (x + 1) // 2
    b = x + 1 - a
    ans = a * b
    print(ans)


