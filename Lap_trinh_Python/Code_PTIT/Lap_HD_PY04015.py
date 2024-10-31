idx = 1
class KhachHang:
    tongtien = 0
    def __init__(self,ID, name, dau,cuoi):
        self.ID = ID
        self.name = name
        self.dau = dau
        self.cuoi = cuoi
        self.sokhoi = self.cuoi - self.dau
        if self.sokhoi <= 50:
            self.tong = self.sokhoi * 100
            self.tong += self.tong * 0.02
        elif self.sokhoi > 50 and self.sokhoi < 100:
            self.tong = (self.sokhoi - 50) * 150 + 50 * 100
            self.tong += self.tong * 0.03
        else:
            self.tong = 50 * 100 + 50 * 150 + (self.sokhoi - 100) * 200
            self.tong += self.tong * 0.05
        self.tongtien = round(self.tong) 
    def getInfo(self):
        return "{} {} {}".format(self.ID,self.name,self.tongtien)
def cmp(a):
    return ( a.tongtien )

List = []
for i in range(int(input())):
    ID = "KH{:02d}".format(i+1)
    name    =   input()
    dau     =  int(input())
    cuoi    =  int(input())
    List.append(KhachHang(ID,name,dau,cuoi))
List.sort(key = cmp,reverse=True)
for a in List:
    print(a.getInfo())

