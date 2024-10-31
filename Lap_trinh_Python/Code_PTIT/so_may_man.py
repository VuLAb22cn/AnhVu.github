t = int(input())
while(t > 0):
    n = (input())
    s = str(n)
    dem = 0

    for i in range(len(s)):
        if (s[i] == '4' or s[i] == '7'):
            dem += 1
        else:
            print("NO")
            break

    if( dem == len(s)):
        print("YES")
    
    t-=1

