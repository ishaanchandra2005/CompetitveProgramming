t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if len(set(arr)) == 1:
        print("NO")
        continue
    arr.sort()
    k = arr.pop()
    arr.insert(0, k)
    print("YES")
    print(*arr)