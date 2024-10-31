def demSo(a):
    n = len(a)
    s = [0] * n 
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if not stack:
            s[i] = i + 1
        else:
            s[i] = i - stack[-1]
        stack.append(i)
    
    return s

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    result = demSo(a)
    print(" ".join(map(str, result)))
