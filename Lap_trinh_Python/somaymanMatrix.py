N, M = map(int, input().split())
matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

max_value = -1
min_value = float('inf')

for i in range(N):
    for j in range(M):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]

lucky_number = max_value - min_value

positions = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] == lucky_number:
            positions.append((i, j))

if positions:
    print(lucky_number)
    for pos in positions:
        print(f"Vi tri [{pos[0]}] [{pos[1]}]")
else:
    print("NOT FOUND")
