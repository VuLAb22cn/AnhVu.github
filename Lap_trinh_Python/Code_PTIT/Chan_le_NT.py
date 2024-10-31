import math

def NT(n):
    if(n <= 1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i == 0):
                return False
            
    return True
def KTraChan(n):
    s = str(n)    
    for i in range(len(s)):
        if(i % 2 == 0):
            if(int(s[i]) % 2 != 0):
                return False            
    return True
def KTraLe(n):
    s = str(n)    
    for i in range(len(s)):
        if(i % 2 == 1):
            if(int(s[i]) % 2 == 0):
                return False            
    return True
def KtraTong(n):
    s = str(n)  
    tong = 0  
    for i in range(len(s)):
        tong += int(s[i])
    if(NT(tong)):
        return True          
    return False

for i in range(int(input())):
    n = int(input())
    if(KTraChan(n) and KTraLe(n) and KtraTong(n)):
        print("YES")
    else:
        print("NO")