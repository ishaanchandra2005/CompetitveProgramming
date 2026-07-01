t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    st = set()
    for x in arr:
        st.add(x % 2)
    if len(st) == 2:
        print(2)
        continue
    for i in range(2, 61):
        k = 2 ** i
        st = set()
        for x in arr:
            st.add(x % k)
        if len(st) == 2:
            print(k)
            break