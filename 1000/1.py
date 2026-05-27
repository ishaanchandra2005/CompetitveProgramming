t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    z = s.count('0')
    o = s.count('1')
    x = 0
    if o == z:
        print(0)
        continue
    if n == 1:
        print(1)
        continue
    for i in range(n):
        if s[i] == '1' and z > 0:
            z -= 1
            x += 1
        elif s[i] == '0' and o > 0:
            o -= 1
            x += 1
        else:
            break
    print(n - x)