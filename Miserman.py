

n, m = map(int, input().split())

grid = []
for row in range(n):
    aRow = [int(x) for x in input().split()]
    grid.append(aRow)


for row in reversed(range(n-1)):
    for col in range(m):
        lo = max(0, col-1)
        hi = min(m-1, col+1) + 1
        grid[row][col] = grid[row][col] + min(grid[row+1][lo:hi])

print(min(grid[0]))


