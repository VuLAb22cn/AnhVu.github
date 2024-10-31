import math

class ThiSinh:
    def __init__(self,name,ns,m1,m2,m3):
        self.name = name
        self.ns = ns
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def getName(self):
        return self.name
    def getNS(self):
        return self.ns
    def getTong(self):
        return (self.m1+self.m2+self.m3)
    
name = str(input())
ns = str(input())
m1 = float(input())
m2 = float(input())
m3 = float(input())
TS = ThiSinh(name,ns,m1,m2,m3)
print(TS.name,TS.ns,end=" ")
print(f"{(m1+m2+m3):.1f}")