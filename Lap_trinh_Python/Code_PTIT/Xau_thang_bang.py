import math

for i in range(int(input())):
    s1 = str(input())
    s2 = ''.join(reversed(s1))
    ok = True
    for i in range(1,len(s1)-2):
        if(math.fabs(ord(s1[i]) - ord(s1[i-1])) != math.fabs(ord(s2[i]) - ord(s2[i-1]))):
            ok = False
            print("NO")
            break
        else:
            continue
    if(ok):
        print("YES")
