#var = input()  # Data type is string by default, whole line

#print(type(var))
#print(type(int(var)))

my_int = int(input("Enter integer: ")) # data type is string
my_float = float(input("Enter integer: ")) # data type is string


# OUTPUT

print("Hello World!", "Again!\nAgain!")

    # Format Method 1
x = "abc"
y = 7654321.7654321
print("x is {}, y is {}".format(x,y))

    # Format method 2
print("x is {: >8}, y is {: .2f}".format(x,y)) # adds parameters {: >8} means always have 8 char, if not, add spaces before variable till 8 char (use "<" for spaces after). {:.2f} means only keep two decimal places (rounded)

    # Format method 3
print(f"x is {x: >8}, y is {y:.2f}")