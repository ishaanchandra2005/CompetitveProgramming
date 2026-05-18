t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if c % 2 == 1:
        a += 1
    if a > b:
        print("First")
    else:
        print("Second")
        
    
    