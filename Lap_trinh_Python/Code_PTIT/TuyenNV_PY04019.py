class NV:
    def __init__(self,id,name,lt,th):
        self.id = 'TS0' + str(id)
        self.name = name
        self.lt = lt
        self.th = th
        if(self.lt > 10 and self.th > 10):
            self.lt = self.lt / 10
            self.th = self.th / 10
        self.tb = (self.lt + self.th) / 2
        if(self.tb > 9.5):
            self.xeploai = "XUAT SAC"
        elif(self.tb >= 8 and self.tb <= 9.5):
            self.xeploai = "DAT"
        elif (self.tb >= 5 and self.tb < 8):
            self.xeploai = "CAN NHAC"
        elif (self.tb > 0 and self.tb < 5):
            self.xeploai = "TRUOT"
        
    def getInfo(self):
        return "{} {} {:.2f} {}".format(self.id,self.name,self.tb,self.xeploai)

def cmp(a):
    return (a.tb)

List = []

for i in range(int(input())):
    name = input()
    lt = float(input())
    th = float(input())
    List.append(NV(i+1,name,lt,th))

List.sort(key=cmp,reverse= True)
for i in List:
    print(i.getInfo())
