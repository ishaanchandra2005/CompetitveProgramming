t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x, y = map(int, input().split())
    val = (x2 - x1)*(y - y1) - (y2 - y1)*(x - x1)
    if val > 0:
        print("LEFT")
    elif val < 0:
        print("RIGHT")
    else:
        print("TOUCH")
