t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    bottom = list(map(int, input().split()))
    up = list(map(int, input().split()))
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    a1 = abs(bottom[1] - bottom[bottom[0]]) * h
    a2 = abs(up[1] - up[up[0]]) * h
    a3 = abs(left[1] - left[left[0]]) * w
    a4 = abs(right[1] - right[right[0]]) * w
    ans = max(a1, a2, a3, a4)
    print(ans)
    