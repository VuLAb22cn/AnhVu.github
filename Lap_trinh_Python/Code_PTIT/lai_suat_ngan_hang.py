import math

t = int(input())
while(t > 0):
    n=float(input())
    x=float(input())
    m=float(input())

    x/=100
    soNam = ( math.log(m/n,1+x))
    
   
    if(soNam != int(soNam)):
        print(int(soNam)+1)
    else:
        print(soNam)

    t-=1

