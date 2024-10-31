import math

class PhanSo2():
    def __init__(self,ts,ms):
        self.ts = ts
        self.ms = ms
    def UCLN(self,a,b):
        if(a == 0 or b == 0):
            return (a+b)
        else:
            return self.UCLN(b,a%b)
    def BCNN(self,a,b):
        return (a*b)/self.UCLN(a,b)
    def PSTG(self):
        uc = self.UCLN(self.ts,self.ms)
        self.ts /= uc
        self.ms /= uc
        return self.ts,self.ms
    
ts1,ms1,ts2,ms2 = map(int,input().split())
s = PhanSo2(ts1,ms1)
s2 = PhanSo2(ts2,ms2)
tu = s.ts*s2.ms + s2.ts*s.ms
mau = s.ms * s2.ms
t = PhanSo2(tu,mau)
p1,p2 = t.PSTG()
print(int(p1),int(p2),sep="/")