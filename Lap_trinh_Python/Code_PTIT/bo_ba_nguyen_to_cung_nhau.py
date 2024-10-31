import math

def UCLN(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())

results = []
for i in range(a, b-1):
    for j in range(i+1, b):
        if UCLN(i, j) != 1:
            continue
        for k in range(j+1, b+1):
            if UCLN(i, k) == 1 and UCLN(j, k) == 1:
                results.append(f"({i}, {j}, {k})")

print("\n".join(results))
#Trong vòng lặp kia ta Bỏ Qua Các Tổ Hợp Không Hợp Lệ Sớm: Trong vòng lặp đầu tiên,
#chỉ tiếp tục kiểm tra các tổ hợp (i, j, k) nếu UCLN(i, j) == 1. 
#Điều này giúp giảm số lần kiểm tra không cần thiết.
#Lưu Kết Quả Vào Danh Sách: Lưu các kết quả hợp lệ vào danh sách
#và in tất cả kết quả sau khi hoàn thành, giúp giảm số lượng phép toán in ra từng bước.