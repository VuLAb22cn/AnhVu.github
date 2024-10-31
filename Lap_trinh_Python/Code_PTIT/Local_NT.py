import math
def NT(n):
    if(n <= 1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i == 0):
                return False
    return True
def KtraD(n):
    s = str(n)
    for i in range(len(s)):
        if(NT(i)):
            if(NT(int(s[i])) == False):
                return False
    return True
def KtraS(n):
    s = str(n)
    for i in range(len(s)):
        if(NT(i) == False):
            if(NT(int(s[i]))):
                return False
    return True

for i in range(int(input())):
    n = int(input())
    if(KtraD(n) and KtraS(n)):
        print("YES")
    else:
        print("NO")