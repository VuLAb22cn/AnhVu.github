from itertools import combinations

# Đọc dữ liệu đầu vào
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Loại bỏ các phần tử trùng lặp và sắp xếp danh sách
a = sorted(set(a))

# Tạo tất cả các tổ hợp chập k từ danh sách đã lọc
result = combinations(a, k)

# In kết quả
for combo in result:
    print(" ".join(map(str, combo)))
