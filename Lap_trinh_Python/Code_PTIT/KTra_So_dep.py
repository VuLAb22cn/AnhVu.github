def solve(n):
    if n[0] == n[1]:
        return "NO"
    for i in range(2, len(n)):
        if n[i] != n[i & 1]:#
            return "NO"
    return "YES"

for i in range(int(input())):
    print(solve(input()))

#Biểu thức i & 1 trả về chỉ số 0 hoặc 1
#(bởi vì i & 1 sẽ là 0 nếu i là số chẵn và 1 nếu i là số lẻ).
# Điều này giúp so sánh ký tự n[i] với ký tự đầu tiên hoặc thứ hai
# của chuỗi n dựa trên chỉ số chẵn hoặc lẻ.