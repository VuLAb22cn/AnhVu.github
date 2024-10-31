import math

def UCLN(a,b):
    if(a==0 or b == 0):
        return (a+b)
    else:
        return UCLN(b,a%b)

n = int(input())
a = list(map(int,input().split()))
a.sort()
for i in range(n-1):
    for j in range(i+1,n):
        if UCLN(a[i],a[j])==1:
            print(a[i],a[j])
