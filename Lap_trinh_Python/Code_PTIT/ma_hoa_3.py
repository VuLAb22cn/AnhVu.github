def encode_drm(s):
    n = len(s)    
    nua_dau = s[:n//2]
    nua_sau = s[n//2:]
    
    def calculate_rotation_value(half):
        return sum(ord(char) - ord('A') for char in half)
    
    quay_dau = calculate_rotation_value(nua_dau)
    quay_sau = calculate_rotation_value(nua_sau)
    
    def rotate_half(half, quay):
        quay %= 26  
        return ''.join(chr((ord(char) - ord('A') + quay) % 26 + ord('A')) for char in half)
    
    a = rotate_half(nua_dau, quay_dau)
    b = rotate_half(nua_sau, quay_sau)
    
    result = []
    for i in range(len(a)):       
        char_first = a[i]
        char_second = b[i]
        rotation_value = ord(char_second) - ord('A')
        merged_char = chr((ord(char_first) - ord('A') + rotation_value) % 26 + ord('A'))
        result.append(merged_char)
    
    return ''.join(result)

T = int(input())
for _ in range(T):
    string_to_encode = input().strip() 
    encoded_string = encode_drm(string_to_encode)
    print(encoded_string)
