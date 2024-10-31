def tong(n):
    s = 0
    for i in n:
        s += ord(i) - ord('0')
    return str(s)


n = input()
dem = 0
while len(n) > 1:
    dem += 1
    n = tong(n)
print(dem)  
