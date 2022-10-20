def swapPositions(grid, pos1, pos2, pos3, pos4):
    grid[pos1], grid[pos2] = grid[pos2], grid[pos1]
    grid[pos3], grid[pos4] = grid[pos4], grid[pos3]
    return list

grid = ["1", "2", "3", "4"]
flip = input()

for x in range(len(flip)):
    if(flip[x] == "H"):
        pos1, pos2 = 1, 3
        pos3, pos4 = 2, 4
        swapPositions(grid, pos1-1, pos2-1, pos3-1, pos4-1)
    elif(flip[x] == "V"):
        pos1, pos2 = 2, 1
        pos3, pos4 = 4, 3
        swapPositions(grid, pos1-1, pos2-1, pos3-1, pos4-1)

print(grid[0], grid[1])
print(grid[2], grid[3])

