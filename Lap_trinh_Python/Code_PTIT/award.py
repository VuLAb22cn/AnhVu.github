for i in range(int(input())):
    n = int(input())
    a,dem = {},0
    for i in range(n):
        num = int(input())
        if num in a :
            a[num] += 1
        else:
            a[num] = 1
        dem = max(dem,a[num])    
    result = 1001
    for i in a:
        if a[i] == dem :
            result = min(result,i)
    print(result)