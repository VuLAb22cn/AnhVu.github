import math

fA = [0,1,1]
for i in range(3,93):
    fA.append((fA[i-1]+fA[i-2]))

for i in range(int(input())):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        print(fA[i],end=" ")
    print()