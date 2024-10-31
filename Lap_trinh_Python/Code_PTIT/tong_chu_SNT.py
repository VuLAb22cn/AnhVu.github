import math

def NT(n):
    if(n<2):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i == 0):
                return False
    return True

for i in range(int(input())):
    n = int(input())
    s = str(n)
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    if(NT(tong)):
        print("YES")
    else:
        print("NO")
