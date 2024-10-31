def count_inversions(arr):
    n = len(arr)
    count = 0
    # Duyệt tất cả các cặp (i, j) với i < j
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])  # số lượng phần tử
    A = list(map(int, data[1:]))  # dãy số
    
    # Đếm và in số lượng cặp nghịch thế
    result = count_inversions(A)
    print(result)

if __name__ == "__main__":
    main()

# Giải thích mã:
# Hàm count_inversions(arr):

# Nhận vào một dãy số arr.
# Sử dụng hai vòng lặp lồng nhau để kiểm tra tất cả các cặp (i, j) với i < j.
# Nếu arr[i] > arr[j], tăng biến đếm count lên 1.
# Hàm main():

# Đọc dữ liệu từ đầu vào chuẩn (thích hợp cho việc chạy trên các hệ thống có đầu vào từ tệp hoặc môi trường thi).
# Chuyển đổi dữ liệu đầu vào thành danh sách số nguyên.
# Gọi hàm count_inversions để đếm số lượng cặp nghịch thế và in kết quả.
# Hướng dẫn sử dụng:
# Nhập số lượng phần tử N: Ví dụ: 5.
# Nhập dãy số: Ví dụ: 3 1 4 2 5.
# Kết quả: Mã sẽ in số lượng cặp nghịch thế trong dãy số.