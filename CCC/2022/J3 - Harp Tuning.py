input = input()
instruction = ""

for x in range (len(input)):
    if (input[x] == '+'):
        instruction += " tighten ".replace("\n", "")
    elif (input[x] == '-'):
        instruction += " loosen ".replace("\n", "")
    elif (input[x].isdigit()):
        instruction += input[x]
    else:
        if (input[x-1].isdigit() and x != 0):
            instruction += "\n"
            instruction += input[x]
        else:
            instruction += input[x]
print(instruction)


