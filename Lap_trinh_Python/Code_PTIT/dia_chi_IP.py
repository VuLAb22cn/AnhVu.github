def is_valid_ip(ip):
    parts = ip.split('.')    
    if len(parts) != 4:
        return "NO"    
    for part in parts:
        if not part.isdigit() or part == "":
            return "NO"        
        num = int(part)        
        if num < 0 or num > 255 or (len(part) > 1 and part[0] == '0'):
            return "NO"    
    return "YES"

T = int(input())
for _ in range(T):
    address = input().strip()
    result = is_valid_ip(address)
    print(result)
