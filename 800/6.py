from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = list(Counter(arr).values())
    if len(freq) > 2:
        print("NO")
    elif len(freq) == 1:
        print("YES")
    elif abs(freq[0] - freq[1]) <= 1:
        print("YES")
    else:
        print("NO")
            