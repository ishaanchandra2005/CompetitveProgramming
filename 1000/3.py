t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    people = []
    for i in range(n):
        people.append((b[i], a[i]))
    people.sort()
    left = n - 1
    cost = p
    for scost, x in people:
        if scost >= p:
            break
        take = min(left, x)
        cost += take * scost
        left -= take
    cost += left * p
    print(cost)