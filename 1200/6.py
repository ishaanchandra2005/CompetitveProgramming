t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [arr[0]]
    y = [arr[0]]
    
    for x in arr[1 : ]:
        if x != y[-1]:
            y.append(x)
            
    ans = [y[0]]
    for x in y[1 : ]:
        while len(ans) >= 2:
            a = ans[-2]
            b = ans[-1]
            if a <= b <= x:
                ans.pop()
            elif a >= b >= x:
                ans.pop()
            else:
                break
        ans.append(x)
    print(len(ans))
        






    