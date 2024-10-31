import math

def nguyen_to(n):
    if(n <= 1):
        return False
    else:
        for i in range (2,int(math.sqrt(n))+1):
            if(n % i == 0):
                return False

    return True

def UCLN(a,b):
    if(b == 0):
        return a
    else :
        return UCLN(b, a%b)
    
t = int(input())
while(t > 0):
    a,b = list(map(int,input().split()))
    c = UCLN(a,b)
    sum = 0

    while(c > 0):
        sum += c%10
        c//=10
    if(nguyen_to(sum)):
        print("YES")
    else:
        print("NO")

    t-=1