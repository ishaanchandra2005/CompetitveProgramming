t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = -1 
# ikkada usually (1 << 30) - 1 anedhi AND ki identity element
    for i in range(n):
        if arr[i] != i:
            if ans == -1:
                ans = i
            else:
                ans &= i
    if ans == -1:
        ans = 0
    print(ans)
