t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue
    if a % b != 0 and b % a != 0:
        print(-1)
        continue
    k = 0
    if a > b:
        while a > b and a % 2 == 0:
            a //= 2
            k += 1
    else:
        while a < b:
            a *= 2
            k += 1
    if a != b:
        print(-1)
        continue
    ans = 0
    ans += k // 3
    k %= 3
    ans += k // 2
    k %= 2
    ans += k
    print(ans)