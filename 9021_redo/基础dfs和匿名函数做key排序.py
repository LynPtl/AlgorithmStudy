grid = [
    #0 1 2
    [1,1,1], #row0
    [0,1,0], #row1
    [1,1,0]  #row2
]
method=[(0,1),(0,-1),(1,0),(-1,0)]
result = []
visited = set()
def dfs(row,col):
    if grid[row][col] == 0 or (row,col) in visited:
        return
    #print(f"({row},{col})")
    result.append([row,col])
    #grid[row][col] = 0
    visited.add((row,col))
    
    if 0 <= row-1:
        dfs(row-1,col)
    if row+1<= len(grid)-1:
        dfs(row+1,col)
    if col-1>=0:
        dfs(row,col-1)
    if col+1<=len(grid[0])-1:
        dfs(row,col+1)
    """
    for (x,y) in method:
        if 0<=(row+x)<len(grid) and 0<=(col+y)<len(grid[0]):
            dfs(row+x,col+y)
    """
dfs(0,0)
result = sorted(result,key=lambda x:x[0])
print(result)
