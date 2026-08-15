# t=int(input())
# for _ in range(t):
#     n=int(input())
#     s=input().strip()
#     if n % 2 == 0:
#         c0 = [0] * 26
#         c1 = [0] * 26
#         for i in range(n):
#             x = ord(s[i]) - 97
#             if i % 2 == 0:
#                 c0[x]+=1
#             else:
#                 c1[x]+=1
#         print(n- max(c0) - max(c1))
#         continue
#     p1 = [[0]*26 for _ in range(n + 1)]
#     p2 = [[0]*26 for _ in range(n + 1)]
#     for i in range(n):
#         p1[i + 1] = p1[i][:]
#         p2[i + 1] = p2[i][:]
#         x = ord(s[i]) - 97
#         if i % 2 == 0: 
#             p1[i + 1][x] += 1
#         else:
#             p2[i + 1][x] += 1
#     s1=[[0] * 26 for _ in range(n + 1)]
#     s2=[[0] * 26 for _ in range(n + 1)]
#     for i in range(n - 1, -1, -1):
#         s1[i] = s1[i + 1][:]
#         s2[i] = s2[i + 1][:]
#         x = ord(s[i]) - 97
#         if i % 2 == 0:
#             s1[i][x] += 1
#         else:
#             s2[i][x] += 1
#     # print(p1)
#     # print(p2)
#     # print(s1)
#     # print(s2)
#     ans = n
#     for i in range(n):
#         e = 0
#         o = 0 
#         for c in range(26):
#             e = max(e,p1[i][c] + s2[i+1][c])
#             o = max(o,p2[i][c] + s1[i+1][c])
#         cost = n - e - o
#         ans=min(ans, cost)
#     print(ans)
import sys
input=sys.stdin.readline
from array import array

t=int(input())
for _ in range(t):
    n=int(input())
    s=input().strip()

    if n%2==0:
        c0=[0]*26
        c1=[0]*26
        for i in range(n):
            x=ord(s[i])-97
            if i%2==0: c0[x]+=1
            else: c1[x]+=1
        print(n-max(c0)-max(c1))
        continue

    p1=array('i',[0])*(26*(n+1))
    p2=array('i',[0])*(26*(n+1))
    for i in range(n):
        base_prev=i*26
        base_cur=(i+1)*26
        p1[base_cur:base_cur+26]=p1[base_prev:base_prev+26]
        p2[base_cur:base_cur+26]=p2[base_prev:base_prev+26]
        x=ord(s[i])-97
        if i%2==0: p1[base_cur+x]+=1
        else: p2[base_cur+x]+=1

    s1=array('i',[0])*(26*(n+1))
    s2=array('i',[0])*(26*(n+1))
    for i in range(n-1,-1,-1):
        base_next=(i+1)*26
        base_cur=i*26
        s1[base_cur:base_cur+26]=s1[base_next:base_next+26]
        s2[base_cur:base_cur+26]=s2[base_next:base_next+26]
        x=ord(s[i])-97
        if i%2==0: s1[base_cur+x]+=1
        else: s2[base_cur+x]+=1

    ans=n
    for i in range(n):
        e=0
        o=0
        bp=i*26
        bs=(i+1)*26
        for c in range(26):
            e=max(e,p1[bp+c]+s2[bs+c])
            o=max(o,p2[bp+c]+s1[bs+c])
        cost=n-e-o
        ans=min(ans,cost)

    print(ans)
