n = int(input())
a = list(map(float,input().split()))
a.sort()
tong = 0
dem =0
for i in a:
    if i != a[0] and i != a[-1]:
        tong += i
        dem += 1
diem_TB = tong/dem
print(f"{diem_TB:.2f}")
