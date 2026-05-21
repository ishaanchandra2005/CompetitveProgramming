t = int(input())
for _ in range(t):
    s = list(input())
    if s[0] != s[-1]:
        s[-1] = s[0]      
    print("".join(s))