import math

n = int(input())
a  = []
for i in range(n):
    num = list(map(int,input().split()))
    a.append(num)
k = int(input())
tong = 0
tongT = 0
tongG = 0
tongD = 0
for i in range(n):
    for j in range(n):
        tong += a[i][j]
for i in range(n):
    for j in range(n-i-1):
        tongT += a[i][j]
for i in range(n):
    for j in range(n):
        if(j == n-i-1):
            tongG += a[i][j]
tongD = tong - tongG - tongT
if(math.fabs(tongT-tongD) <= k):
    print("YES")
    print(int(math.fabs(tongT-tongD)))
else:
    print("NO")
    print(int(math.fabs(tongT-tongD)))

