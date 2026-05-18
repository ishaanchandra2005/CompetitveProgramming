t = int(input())
for _ in range(t):
    s, target = input().split()
    freq = [0] * 26
    for ch in target:
        freq[ord(ch) - ord('A')] += 1
    ans = []
    for i in range(len(s) - 1, -1, -1):
        if freq[ord(s[i]) - ord('A')] > 0:
            freq[ord(s[i]) - ord('A')] -= 1
            ans.append(s[i])
    ans.reverse()
    if ''.join(ans) == target:
        print("YES")
    else:
        print("NO")
        
    