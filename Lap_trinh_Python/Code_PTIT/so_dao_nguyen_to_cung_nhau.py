import math

def UCLN(a,b):
    if(a==0 or b == 0):
        return (a+b)
    else:
        return UCLN(b,a%b)  


t = int(input())
for i in range(1,t+1):
    n = int(input())
    t = 0
    a = n
    while(n > 0):
        t = t*10 + n%10
        n//=10
    if(UCLN(a,t) == 1):
        print("YES")
    else:
        print("NO")
    
