def dfs(w, h, dist , grid, breadth, length):
    mx = 2147483647
    print(f"on {w} {h}")
    if(w < 0 or w == breadth or  h < 0 or h == length or grid[w][h] == -1 or grid[w][h] == -2):
        print(f"on {w} {h} returning mx")
        return mx
    val = grid[w][h]
    if val != mx and val != 0:
        print(f"on {w} {h} returning {val}")
        return val
    grid[w][h] = -2 # doing this to block the cell
    u, d, l, r = mx, mx, mx, mx
    u = dfs(w-1, h, dist+1 , grid, breadth, length)
    d = dfs(w+1, h, dist+1, grid, breadth, length)
    l = dfs(w, h-1, dist+1, grid, breadth, length)
    r = dfs(w, h+1, dist+1, grid, breadth, length)
    
    print(f"on {w} {h} u{u} d{d} l{l} r{r}")

    grid[w][h] = min(u+1 ,d+1 ,l+1 ,r+1 , dist+1, grid[w][h])
    
    print(f"on {w} {h} setting {grid[w][h]}")
    
    return grid[w][h]


def islandsAndTreasure( grid) -> None:
    breadth = len(grid)
    length = len(grid[0])

    for i in range(breadth):
        for j in range(length):
            if grid[i][j] == 0:
                dfs(i,j,-1,grid, breadth, length)

grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

print(grid)
islandsAndTreasure(grid)
print(grid)