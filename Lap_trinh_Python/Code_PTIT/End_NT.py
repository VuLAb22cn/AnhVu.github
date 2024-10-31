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
    s = str(n)
    t = s[len(s)-4]+s[len(s)-3]+s[len(s)-2]+s[len(s)-1]
    if(NT(int(t))):
        print("YES")
    else:
        print("NO")