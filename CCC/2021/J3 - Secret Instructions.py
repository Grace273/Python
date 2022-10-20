# instruction = input()

# while(int(instruction) != 99999):
#     direction = int(instruction[0]) + int(instruction[1])
#     # if (((direction % 2) == 0) and (int(instruction[0]) != 0) and (int(instruction[1] != 0))):
#     if ((direction % 2) == 0):
#         turn = "right"
#     if ((direction % 2) != 0):
#         turn = "left"
#     # if (int(instruction[0]) == 0) and (int(instruction[1] == 0)):
    
#     print(turn, instruction[2:5])
#     instruction = input()

# instruction = input()
# while(instruction != '99999'):
#     direction = int(instruction[0]) + int(instruction[1])
 
#     if (direction == 0):
#         pass
#     elif (direction % 2):
#         turn = "left"
#     elif not (direction % 2):
#         turn = "right"
 
#     print(turn, instruction[2:5])
#     instruction = input()

instruction = input()
while(instruction != '99999'):
    direction = int(instruction[0]) + int(instruction[1])
 
    if (direction % 2):
        turn = "left"
    elif not (direction % 2):
        turn = "right"
    elif not direction:
        pass

    print(turn, instruction[2:5])
    instruction = input()
print(0%2)
