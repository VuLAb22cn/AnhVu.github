
for t in range(int(input())):
    n = int(input())    
    a = list(map(int,input().split()))
    b = {}
    for j in a:        
        if j in b :
            b[j] += 1
        else:
            b[j] = 1
    max_count = 0
    candidate = -1
    for num, count in b.items():
        if count > max_count:
            max_count = count
            candidate = num
    if (max_count <= n//2):
        print("NO")
    else:
        print(candidate)