import math

def NT(n):
    if(n <=1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i == 0):
                return False
            
    return True
def KTra(n):
    s = len(n)
    dem1=0
    dem2=0
    if(NT(s)):
        return True
    for i in range(s):
        if(NT(int(n[i]))):
            dem1 += 1
        else:
            dem2 += 1
    if(dem1 > dem2):
        return True
    return False

for i in range(int(input())):
    s = input()
    dem1=0
    dem2=0
    for i in range(len(s)):
        if(NT(int(s[i]))):
            dem1 += 1
        else:
            dem2 += 1
    if(NT(len(s)) and (dem1 > dem2)):
        print("YES")
    else:
        print("NO")