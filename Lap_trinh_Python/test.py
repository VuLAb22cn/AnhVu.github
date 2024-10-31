import math
def NT(n):
    if(n <= 1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i == 0):
                return False
    return True


m,n = map(int,input().split())



a = []
fA = []

for i in range(m):    
    row = list(map(int, input().split()))
    a.append(row)
    fA.append([0]*n)



for i in range(m):
    for j in range(n):
        if(NT(a[i][j])):
            fA[i][j] = 1
for i in range(m):
    for j in range(n):
        print(fA[i][j],end=" ")
    print("\n")

   
