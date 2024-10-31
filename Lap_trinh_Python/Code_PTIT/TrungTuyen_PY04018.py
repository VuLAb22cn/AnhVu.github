mon = ['TOAN', 'LY', 'HOA']
congdiem = [2, 1.5, 1, 0]

class GV :
    def __init__(self, id, ten, ma, d1, d2) :
        self.id = 'GV0' + str(id)
        self.ten = ten
        self.mon = mon[ord(ma[0]) - ord('A')]
        self.diem = 2 * d1 + d2 + congdiem[int(ma[1]) - 1]
    if self.diem >= 18:
            self.status = "TRUNG TUYEN"
        else:
            self.status = "LOAI"
    def getInfo(self):
        return "{} {} {} {:.1f} {}".format(self.id,self.ten,self.mon,self.diem,self.status)

def cmp(a):
    return a.diem

List = []
for i in range(int(input())):
    List.append(GV(i+1,input(),input(),float(input()),float(input())))
List.sort(key=cmp,reverse=True)
for i in List:
    print(i.getInfo())
