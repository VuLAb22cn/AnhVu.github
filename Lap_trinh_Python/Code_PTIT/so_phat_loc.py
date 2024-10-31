import math

def so_phat_loc(n):
    s = str(n)

    if(s[len(s)-2] + s[len(s)-1] != '86'):
        return False
    
    return True

t = int(input())
while(t > 0):
    n=int(input())
    if(so_phat_loc(n)):
        print("YES")
    else:
        print("NO")

    t-=1
    