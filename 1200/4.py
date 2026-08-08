# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     x = len(a)
#     a.sort()
    # print(a)
# 0 -2 0 3 5
# 0 -2 3 4 5
# -2 -2 -2 -2 0 0 0 3 3 4
# -2 -2 -2 -2 0 0 0 0 0 3
# 0 0 0 -2 3
# -2 -2 -2 -2 0 0 0 0 0 0 
# freq anedhi (n - 1) kanna entha peddadhi aithe anni extra reps of that guy
    # ans = []
    # if len(set(a)) == 1:
    #     for i in range(n):
    #         ans.append(a[0])
    #     print(*ans)
    #     continue
    # mp = {}
    # for i in range(x):
    #     if a[i] in mp:
    #         mp[a[i]] += 1
    #     else:
    #         mp[a[i]] = 1
    # # print(mp)
    # ans = []
    # k = 0
    # for x in mp:
    #     ans.append(x)
    #     k += 1
    #     if mp[x] > n -1 - k:
    #         for _ in range(mp[x] - (n - k) - 1):
    #             ans.append(x)
    # # print(ans)
    # f = ans[-1]
    # if len(ans) < n:
    #     ans.append(f + 1)
    # print(*ans)
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    k = n - 1
    i = 0
    ans = []
    while k > 0:
        ans.append(arr[i])
        i += k
        k -= 1
    ans.append(10 ** 9)
    print(*ans)
        