def sum_of_parts(num):
    while len(num) > 1: 
        n = len(num)            
        mid = n // 2
        dau = num[:mid]
        sau = num[mid:] 
        
        left_num = int(dau)
        right_num = int(sau)
        total = left_num + right_num
        
        print(total)        
        num = str(total)

num = input()
sum_of_parts(num)
