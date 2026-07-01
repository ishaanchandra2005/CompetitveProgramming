t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    stack = []
    stack.append(s[0])
    for i in range(1, n):
        if s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    ans = len(stack) // 2
    print(ans)