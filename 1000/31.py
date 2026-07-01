n = int(input())
s = input()
ok = True
for i in range(n - 1):
    if s[i] > s[i + 1]:
        print("YES")
        print(i + 1, i + 2)
        ok = False
        break
if ok:
    print("NO")
