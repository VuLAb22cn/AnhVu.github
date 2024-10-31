class HangHoa:
    def __init__(self,ma,ten,soluong,dongia,chietkhau):
        self.ma = ma
        self.ten = ten
        self.soluong = soluong
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tien = self.dongia * self.soluong - self.chietkhau
    def __str__(self):
        return f"{self.ma} {self.ten} {self.soluong} {self.dongia} {self.chietkhau} {self.tien}"
    
List = []
for i in range(int(input())):
    ma = input().strip()
    ten = input().strip()
    soluong = int(input())
    dongia = int(input())
    chietkhau = int(input())
    List.append(HangHoa(ma,ten,soluong,dongia,chietkhau))
List = sorted(List, key=lambda a: (-1) * a.tien)
print(*List,sep="\n")
