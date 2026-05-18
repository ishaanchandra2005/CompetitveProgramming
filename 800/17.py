t = int(input())
for _ in range(t):
    n, k, x = list(map(int, input().split()))
    if n % 2 != 0 and k == 2 and x == 1:
        print('NO') 
    elif k == 1 and x == 1:
        print('NO')
    else:
        if x != 1:
            print('YES')
            arr = []
            for i in range(n):
                arr.append(1)
            print(len(arr))
            print(*arr)   
        else:
            print('YES')
            arr = []  
            if n % 2 == 0:
                for i in range(n // 2):
                    arr.append(2)
            else:
                arr.append(3)
                for i in range((n - 3) // 2):
                    arr.append(2)        
            print(len(arr))
            print(*arr)        
    