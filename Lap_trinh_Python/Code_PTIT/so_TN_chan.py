import math
def TN(n):
    tong = 0
    m = n
    while(n > 0):
        tong = tong * 10 + n % 10
        n//=10
    if(tong == m):
        return True
    return False

def KTra1(n):
    
    while n > 0:
        if (n % 10) % 2 != 0:
            return False 
        n //= 10
    return True

def KTra2(n):
    s = str(n)
    if(len(s) % 2 != 0):
        return False
    return True

A = []
def add(start, end):
    for i in range(start, end, 2):
        if (TN(i) and KTra1(i) and KTra2(i)):
            A.append(i)

add(22, 100)
add(1000, 10000)
add(100000, 1000000)

for i in range(int(input())):
    n = int(input())
    for i in A:
        if(i >= n):
            break
        else:
            if(TN(i) and KTra1(i) and KTra2(i)):
                print(i,end=" ")
    print("\n")