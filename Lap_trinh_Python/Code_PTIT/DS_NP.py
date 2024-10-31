import math

n = int(input())
A = list(map(int,input().split()))
dem = 0
for i in range(len(A) - 1):
    if(A[i] != A[i+1]):
        dem +=1
print(dem)