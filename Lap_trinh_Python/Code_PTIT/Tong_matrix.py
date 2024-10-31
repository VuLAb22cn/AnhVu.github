from shapely.geometry import Polygon

def Dien_tich(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        triangles = []
        
        for _ in range(N):
            x1, y1, x2, y2, x3, y3 = map(int, data[index:index+6])
            index += 6
            triangles.append(Polygon([(x1, y1), (x2, y2), (x3, y3)]))
        
        union_area = Polygon()
        for triangle in triangles:
            union_area = union_area.union(triangle)
        
        results.append(f"{union_area.area:.6f}")
    
    for result in results:
        print(result)

solve()
