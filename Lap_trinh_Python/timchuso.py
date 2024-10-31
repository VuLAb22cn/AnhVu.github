import math

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    # Tính giá trị của (3 + sqrt(5))^n
    m = (3 + math.sqrt(5)) ** n
    # Lấy phần nguyên của m
    m_int = int(m)
    # Lấy 3 chữ số cuối cùng của phần nguyên
    last_three_digits = m_int % 1000
    # Định dạng kết quả để luôn có 3 chữ số
    result = str(last_three_digits).zfill(3)
    print(f"Case #{t}: {result}")
