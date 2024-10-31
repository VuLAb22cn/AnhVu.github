import math

def KTra(n):
    s = str(n)
    if(len(s) % 2 == 0):
        return False
    if(s[0] == s[1]):
        return False
    for i in range(0,len(s)-2,2):
        if(s[i] != s[i+2]):
            return False
    
    return True

for i in range(int(input())):
    n = int(input())
    if(KTra(n) == True):
        print("YES")
    else:
        print("NO")
