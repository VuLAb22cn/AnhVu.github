import math

def UCLN(a,b):
    if(a==0 or b == 0):
        return (a+b)
    else:
        return UCLN(b,a%b)  

def NT(n):
    if(n <=1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i == 0):
                return False
            
    return True

t = int(input())
for i in range(t):
    n = int(input())
    dem = 0
    for j in range(1,n):
        if(UCLN(j,n) == 1):
            dem+=1
    if(NT(dem)):
        print("YES")
    else:
        print("NO")
