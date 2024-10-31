a,K,N = list(map(int,input().split()))

A=[]

t = K - (a%K)
N-=a

while( t <= N):
    A.append(t)
    t+=K

if(len(A) == 0):
    print(-1)

else:
    for i in A:
        print(i,end=' ')