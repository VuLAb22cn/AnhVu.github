import math

t = int(input())
for i in range(1,t+1,1):
    n = int(input())
    print(1,end=' ')
    for i in range(2,int(math.sqrt(n)),1):
        if(n%i == 0):
            dem=0
            while(n%i == 0):
                dem+=1
                n//=i
            print(" *",end=' ')
            print(str(i)+'^'+str(dem),end='')
            
    if(n>1):
        print(" *",end=' ')
        print(str(n)+"^"+str(1),end='')
    print("\n")