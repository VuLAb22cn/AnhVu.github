a = []
while (len(a) < 10):
    sums = (input().split())
    a.extend(map(int,sums))
b = [0] * 42
for i in a:
    b[i % 42] = 1
print(sum(b))
