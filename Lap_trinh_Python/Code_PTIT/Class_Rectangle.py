import math

class Rectangle:
    def __init__(self,d,r,c):
        self.d = d
        self.r = r
        self.c = c
    def perimeter(self):
        d = ( self.d + self.r ) * 2
        return d
    def area(self):
        s = ( self.d * self.r )
        return s
    def color(self):
        return self.c.lower().capitalize()
    


arr = list(input().split())
r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
if(int(arr[0]) <= 0 or int(arr[1]) <= 0):
    print("INVALID")
else:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))