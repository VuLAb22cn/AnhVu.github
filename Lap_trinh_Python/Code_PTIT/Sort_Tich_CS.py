import math

def TichCS(n):
    tich = 1
    while( n > 0):
        tich = tich * (n%10)
        n//=10
    return tich
def Ktra(n):
    return (TichCS(n),n)
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(key=Ktra)
    print(" ".join(map(str,a)))