import math

def kiem_tra(n):
    s = str(n)
    for i in range(len(s)-1):
        if(int(s[i]) > int(s[i+1])):
            return False
        
    return True
        
        
t = int(input())
while(t>0):
    n = int(input())
    if(kiem_tra(n) == True) :
        print("YES")

    else:
        print("NO")

    t-=1