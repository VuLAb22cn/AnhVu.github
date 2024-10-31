import math

def NT(n):
    if(n <= 1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+ 1):
            if (n % i == 0):
                return False
    return True
def get_NT(n):
    NTo = []
    num = 2
    while len(NTo) < n :
        if(NT(num)):
            NTo.append(num)
        num += 1
    return NTo

n,x = map(int,input().split())
mangNT = get_NT(n)
print(x,end=" ")
for i in mangNT:
    x += i
    print(x,end=" ")