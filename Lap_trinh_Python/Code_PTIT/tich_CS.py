for i in range(int(input())):
    n = int(input())
    s = str(n)
    tich = 1
    for i in range(len(s)):
        if(s[i] == '0'):
            continue
        tich *= int(s[i])
    print(tich)