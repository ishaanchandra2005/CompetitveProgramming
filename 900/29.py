# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     M = arr.index(max(arr))
#     ok = 0
#     if M != 0 and M != n - 1:
#         print("YES")
#         print(M, M + 1, M + 2)
#     else:
#         for i in range(n - 2):
#             for j in range(i + 1, n - 1):
#                 for k in range(j + 1, n):
#                     if arr[j] > arr[i] and arr[j] > arr[k]:
#                         print("YES")
#                         print(i + 1, j + 1, k + 1)
#                         ok = 1
#                         break
#                 if ok:
#                     break
#             if ok:
#                 break
#     if ok:
#         continue
#     print("NO")
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ok = 0
    for j in range(1, n - 1):
        if arr[j] > arr[j - 1] and arr[j] > arr[j + 1]:
            print("YES")
            print(j, j + 1, j + 2)
            ok = 1
            break
    if ok == 0:
        print("NO")