import math
t = int(input())
for _ in range(t):
    n = int(input())
    lcm = 1
    ans = 0
    k = 1
    while True:
        lcm = (lcm * k) // math.gcd(lcm, k)
        if n % lcm == 0:
            ans = k
            k += 1
        else:
            break
    print(ans)
        
            
    
    