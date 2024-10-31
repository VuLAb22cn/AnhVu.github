import math

def TongCS(n):
    s = str(n)
    tong = 0
    for i in range(len(s)):
        if(i % 2 == 0):
            tong += int(s[i])
    return tong

def TichCS(n):
    s = str(n)
    tich = 1
    vt = False
    for i in range(len(s)):
        if(i % 2 == 1):
            if(int(s[i]) != 0):
                vt = True
                tich *= int(s[i])
            else:
               continue
    if(vt == False):
        return 0
    else:
        return tich
    
for i in range(int(input())):
    n = int(input())
    tong = TongCS(n)
    tich = TichCS(n)
    print(tong,tich,sep=" ")