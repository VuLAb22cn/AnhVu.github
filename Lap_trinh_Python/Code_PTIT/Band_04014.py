class Student:
    def __init__(self,ID, Name, p):
        self.ID = "HS0" + str(ID)
        self.Name = Name
        self.diemTB = p[0] * 2.0 + p[1] * 2.0
        for i in range(2, 10):
            self.diemTB += p[i]
        self.diemTB = self.diemTB / 10 / 1.2
        if self.diemTB >= 9.0:
            self.xepLoai = "XUAT SAC"
        elif self.diemTB >= 8.0:
            self.xepLoai = "GIOI"
        elif self.diemTB >= 7.0:
            self.xepLoai = "KHA"
        elif self.diemTB >= 5.0:
            self.xepLoai = "TB"
        else:
            self.xepLoai = "YEU"
    def getInfo(self):
        return "{} {} {:.2f} {}".format(self.ID, self.Name, self.diemTB, self.xepLoai)

def cmp(HS):
    return (HS.diemTB, (-1) * HS.ID)

band = []

for i in range(int(input())):    
    band.append(Student(i+1, str(input(), list(map(float, input().split())))))

band.sort(key=cmp, reverse=True)

for i in band:
    print(i.getInfo())

