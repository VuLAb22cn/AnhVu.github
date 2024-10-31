import math
def NT(n):
    if(n <= 1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i == 0):
                return False
    return True

n = int(input())
a = list(map(int,input().split()))
dem = {}
for i in a:
    if NT(i):  
        if i in dem:
            dem[i] += 1
        else:
            dem[i] = 1

for i in a:
    if i in dem and dem[i] != 0:
        print(i, dem[i])
        dem[i] = 0