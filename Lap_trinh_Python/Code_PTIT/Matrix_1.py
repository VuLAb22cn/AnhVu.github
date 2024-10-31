import math

n = int(input())
a  = []
for i in range(n):
    num = list(map(int,input().split()))
    a.append(num)
k = int(input())
tongT = 0
tongD = 0
for i in range(n):
    for j in range(i+1,n):
        tongT += a[i][j]
for i in range(n):
    for j in range(i):
        tongD += a[i][j]
if(math.fabs(tongT-tongD) <= k):
    print("YES")
    print(int(math.fabs(tongT-tongD)))
else:
    print("NO")
    print(int(math.fabs(tongT-tongD)))
