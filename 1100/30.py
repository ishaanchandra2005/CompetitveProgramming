t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    def check(x):
        l = 0
        r = n - 1
        while l < r:
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            elif arr[l] == x:
                l += 1
            elif arr[r] == x:
                r -= 1
            else:
                return False
        return True

    l = 0
    r = n - 1
    while l < r and arr[l] == arr[r]:
        l += 1
        r -= 1
    if l >= r:
        print("YES")
    elif check(arr[l]) or check(arr[r]):
        print("YES")
    else:
        print("NO")



