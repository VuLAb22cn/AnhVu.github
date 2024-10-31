import math
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    dem = 0
    for i in range(n):
        if(a[i] > b[i]):
            print("NO")
            break
        else:
            dem += 1
    if(dem == n):
        print("YES")