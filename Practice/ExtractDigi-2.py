number = input()

for x in range((len(number))):
    if (x == 0):
        print("The 1st digit is: {}". format(number[x]))
    elif x == 1:
        print("The 2nd digit is: {}". format(number[x]))
    elif x == 2:
        print("The 3rd digit is: {}". format(number[x]))
    else:
        print("The {}th digit is: {}". format(x, number[x]))