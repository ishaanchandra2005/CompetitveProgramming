t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    zeros = []
    # ikkada the main motive is that zeros filp cheste oka digit potundi
    for x in a:
        s = str(x)
        z = 0
        i = len(s) - 1
        while i >= 0 and s[i] == '0':
            z += 1
            i -= 1
        ans += len(s) - z
        zeros.append(z)
    # so no of zeros count chesi reverse lo sort chesi alternate ga assign cheyali
    zeros.sort(reverse = True)
    for i in range(1, n, 2):
        ans += zeros[i]
    if ans > m:
        print("Sasha")
    else:
        print("Anna")