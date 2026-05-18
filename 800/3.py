t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    k = 0
    for i in range(len(s)):
        if s[i] == '.':
            k += 1
    if '...' in s:
        print(2)
    else:
        print(k)