import math

t = int(input())
while t > 0:
    s1 = input().strip()  # Đọc chuỗi s1 và loại bỏ khoảng trắng thừa
    s2 = ''.join(reversed(s1))  # Đảo ngược chuỗi s1 để tạo s2
    dem = True  # Biến để theo dõi xem tất cả khoảng cách có giống nhau không
    
    for i in range(1, len(s1)):
        # Tính khoảng cách giữa các ký tự liền kề trong s1 và s2 dựa trên mã ASCII
        distance_s1 = abs(ord(s1[i]) - ord(s1[i - 1]))   #ord là gọi để mấy mã ascii theo kí tự tương ứng
        distance_s2 = abs(ord(s2[i]) - ord(s2[i - 1]))
        
        if distance_s1 != distance_s2:
            dem = False
            print("NO")
            break
    
    if dem:
        print("YES")
    
    t -= 1
