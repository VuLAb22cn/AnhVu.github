n = int(input())
a = list(map(int,input().split()))
b = [0] * 30001
for i in range(n):
    b[a[i]] = 1
for i in range(1,30001):
    if b[i] == 0:
        print(i)
        break