import math

t = int(input())
while t>0:
    s = str(input())
    for i in range(len(s)):
        if(i % 2 == 0):
            print(s[i]*int(s[i+1]),end='')
    print('\n')

    t-=1