a = 17

def func():
    global a #declare this global variable, c++ don't need to declare because they are the same variable a
    a = 23 #common to this function
    print (2,a)

print(1, a)
func()
print(3,a)

# use indent for the scope and storage class