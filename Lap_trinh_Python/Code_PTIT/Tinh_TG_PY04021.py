from datetime import datetime

class ThoiGian:
    def __init__(self, ma, name, vao, ra):
        self.ma = ma
        self.name = name
        self.vao = vao
        self.ra = ra
        self.tg = datetime.strptime(self.ra, '%H:%M') - datetime.strptime(self.vao, '%H:%M')
    
    def total_minutes(self):
        return self.tg.total_seconds() // 60
List = []
for i in range(input()):
    ma = input().strip()
    name = input().strip()
    vao = input().strip()
    ra = input().strip()
    List.append(ThoiGian(ma,name,vao,ra))
List.sort(key=lambda a: -a.total_minutes())
for i in List:
    gio, remainder = divmod(i.total_minutes(), 60)
    phut = remainder
    print(f"{i.ma} {i.name} {int(gio)} gio {int(phut)} phut")
