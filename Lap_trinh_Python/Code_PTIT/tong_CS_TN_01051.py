import math

def TNghich(n):
    t = n
    tong = 0
    while(n > 0):
        tong = tong*10 + n%10
        n//=10
    a = str(tong)
    if(tong == t and len(a) > 1):
        return True
    return False

for i in range(int(input())):
    n = int(input())
    s = str(n)
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    if(TNghich(tong)):
        print("YES")
    else:
        print("NO")