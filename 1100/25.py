t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    cycle = []
    seen = set()
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            cycle.append(ch)
    j = 0
    ok = True
    for ch in s:
        if ch != cycle[j]:
            ok = False
            break
        j = (j + 1) % len(cycle)
    if ok:
        print("YES")
    else:
        print("NO")

