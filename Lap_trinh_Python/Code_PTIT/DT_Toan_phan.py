t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    a = [[0] * (m+2)] * (n+2)
    dt = 2 * m * n
    for i in range(1,n+1):
        a[i] = [0] + [int(x) for x in input().split()] + [0]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(a[i][j] == 0):
                dt -= 2
            if(a[i][j]  > a[i-1][j]):
                dt += a[i][j] - a[i-1][j]
            if(a[i][j] > a[i+1][j]):
                dt += a[i][j] - a[i+1][j]
            if(a[i][j] > a[i][j-1]):
                dt += a[i][j] - a[i][j-1]
            if(a[i][j] > a[i][j+1]):
                dt += a[i][j] - a[i][j+1]
    print(dt)
