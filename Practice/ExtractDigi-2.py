number = input()

for x in range(0, (len(number)), 1):
    if (x == 0):
        place = ("1st")
    elif x == 1:
        place = ("2nd")
    elif x == 2:
        place = ("3rd")
    else:
        place = (x+1,"th")
    print("The", place, "digit is: ", number[x])