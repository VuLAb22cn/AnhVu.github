import math

def chia_10(n):
    sum = 0
    while(n > 0):
        sum += n%10
        n//=10
    if(sum % 10 == 0):
        return True
    else:
        return False
    
def cach_2(n):
    s = str(n)
    for i in range(len(s)-1):
        if(int(s[i+1]) - int(s[i]) == 2):
            return True
        else:
            return False
        
t = int(input())
while t > 0 :
    n = int(input())
    if (chia_10(n) == True) and (cach_2(n) == True):
        print("YES")
    else:
        print("NO")

    t-=1