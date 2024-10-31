# import math
# def Dao(n):
#     tong = 0
#     while(n > 0):
#         tong = tong * 10 + n % 10
#         n//=10
#     return tong

# def solve(n):
#     tong = 0
#     for i in range(1,1001):
#         tong = tong + Dao(int(n))
#         if(tong % 7 == 0):
#             return tong
#         n = str(tong)
#     return -1
# for i in range(int(input())):
#     n = str(input())    
#     print(solve(n)) 
def solve(n):
    res = 0
    if int(n) % 7 == 0:
        return int(n)
    for i in range(1000):
        res = int(n) + int(n[::-1])
        if res % 7 == 0:
            return res
        n = str(res)
    return -1

for i in range(int(input())):
    print(solve(input()))