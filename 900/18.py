t = int(input())
results = []
for _ in range(t):
    a, b, c = map(int, input().split())
    answer = False
    new_a = 2 * b - c
    if new_a > 0 and new_a % a == 0:
        answer = True
    new_b = (a + c) // 2
    if (a + c) % 2 == 0 and new_b > 0 and new_b % b == 0:
        answer = True
    new_c = 2 * b - a
    if new_c > 0 and new_c % c == 0:
        answer = True
    if answer:
        results.append("YES")
    else:
        results.append("NO")
for x in results:
    print(x)
    
    