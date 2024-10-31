import math

def NT(n):
    if(n <= 1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i == 0):
                return False
    return True

for i in range(int(input())):
    n = int(input())
    dem1 = 0 
    dem2 = 0
    s = str(n)
    for i in range(len(s)):
        if(NT(int(s[i]))):
            dem1 += 1
        else:
            dem2 += 1
    if( NT(len(s)) and dem1 > dem2):
        print("YES")
    else:
        print("NO")