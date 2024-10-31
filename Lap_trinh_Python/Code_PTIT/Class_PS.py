import math

class PhanSo():
    def __init__(self,ts,ms):
        self.ts = ts
        self.ms = ms
    def UCLN(self,a,b):
        if(a == 0 or b == 0):
            return (a+b)
        else:
            return self.UCLN(b,a%b)
    def PSTG(self):
        uc = self.UCLN(self.ts,self.ms)
        self.ts /= uc
        self.ms /= uc
        return self.ts,self.ms
    
ts,ms = map(int,input().split())
s = PhanSo(ts,ms)
c,d = s.PSTG()
print(int(c),int(d),sep="/")