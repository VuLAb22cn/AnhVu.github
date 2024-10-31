for i in range(int(input())):
    s = str(input())
    t = True
    for j in range(len(s)):
        if(s[j] != '0' and s[j] != '1' and s[j] != '2' ):
            t = False
            print("NO")
            break
    if(t == True):
        print("YES")