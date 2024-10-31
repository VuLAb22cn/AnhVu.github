import math

def Dem(S,n):
    n = str(n)
    len_n = len(n)
    dem = 0
    i=0
    while(i <= len(S) - len_n):
        if(S[i:i+len_n] == n):
            dem += 1
            i += len_n
        else:
            i += 1
    return dem

for i in range(int(input())):
    S = str(input())
    n = int(input())
    dem = Dem(S,n)
    print(dem)