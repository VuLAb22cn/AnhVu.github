for i in range(int(input())):
    n = int(input())
    s = str(n)
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    if(tong % 3 == 0):
        print("YES")
    else:
        print("NO")