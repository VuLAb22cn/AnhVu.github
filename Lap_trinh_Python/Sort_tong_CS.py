import math

def tongCS(n):
    tong = 0
    while (n>0):
        tong = tong + (n%10)
        n//=10
    return tong
def KTra(a):
    return(tongCS(a),a)
    
for j in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(key=KTra)
    print(" ".join(map(str,a)))