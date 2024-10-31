import math

def UCLN(a,b):
    if(a==0 or b == 0):
        return (a+b)
    else:
        return UCLN(b,a%b)    
    

n,k  = map(int,input().split())
start = 10**(k-1)
end = 10**k-1
dem = 0
for i in range(start, end+1):
    if(UCLN(n,i) == 1):
        print(i,end=' ')
        dem+=1
        if(dem == 10):
            print("\n")
            dem = 0

print("\n")