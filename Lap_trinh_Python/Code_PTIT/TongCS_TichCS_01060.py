import math

def TongCS(n):
    s = str(n)
    tong = 0
    for i in range(len(s)):
        if(i % 2 == 1):
            tong += int(s[i])
    return tong

def TichCS(n):
    s = str(n)
    tich = 1
    for i in range(len(s)):
        if(i % 2 == 0):
            if(int(s[i]) != 0):
                tich *= int(s[i])
            else:
               continue
    return tich
    
for i in range(int(input())):
    n = int(input())
    tong = TongCS(n)
    tich = TichCS(n)
    print(tich,tong,sep=" ")