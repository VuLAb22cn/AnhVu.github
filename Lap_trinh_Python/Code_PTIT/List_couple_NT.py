import math 
def ucln(a,b):
    if(a == 0 or b == 0):
        return (a+b)
    else:
        return ucln(b,a%b)
def Ktra(n,m):
    if ucln(n,m) == 1:
        return True
    return False

n = int(input())
a = list(map(int,input().split()))
a.sort()
for i in range(len(a) - 1):
    for j in range(i+1,len(a)):
        if(Ktra(a[i],a[j])):
            print(a[i]," ",a[j])
        
        
