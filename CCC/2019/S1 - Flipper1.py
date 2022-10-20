grid = [
    [1, 2], 
    [3, 4]
]

def horizontal():
    global grid
    grid[0], grid[1] = grid[1], grid[0]
    
def vertical():
    global grid
    grid[0][1], grid[0][0] = grid[0][0], grid[0][1]
    grid[1][1], grid[1][0] = grid[1][0], grid[1][1] 

input = input()
H = 0
V = 0

for x in range(len(input)):
    if(input[x] == "H"):
        H += 1
    elif(input[x] == "V"):
        V += 1

if (H % 2):
    horizontal()
if (V % 2):
    vertical()

print(grid[0][0], grid[0][1])
print(grid[1][0], grid[1][1])

