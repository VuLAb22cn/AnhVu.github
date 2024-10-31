import math

def UCLN( a, b):
    if (a == 0 or b == 0):
        return (a+b)
    else:
        return UCLN(b,a%b)

for i in range(int(input())):
    a = int(input())
    b = int(input())
    result = UCLN(a,b)
    print(result)