n = int(input())


set_of_chuc = set()


for _ in range(n):
    chuc = input().strip() 
    set_of_chuc.add(chuc)  


print(len(set_of_chuc))
