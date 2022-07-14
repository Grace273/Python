#Function Without Parameter

def empty_function():
    pass            #pass means doing nothing

def my_function():                   # def = define
    print ("Hello from a function")

#calling function is the same as c++ ex:  empty_function()

#Function With Parameters (No Return Value)

def my_second_function (first_str, second_str):
    print(first_str + "" + second_str)

my_second_function("Merry ", "Christmas")   #Order matters!

def my_third_function(child_1, child_2, child_3="Lisa"):   #Lisa is default value
    print ("The third child is " + child_3)

my_third_function(child_2="Bruce", child_1="Alvin")
my_third_function(child_1="Amanda", child_2="Emma", child_3="Sara")

#Function with Parameters and Return Value

def num_of_balls(balls):
    return 5 * balls

y = num_of_balls(balls=3)
print(y)

print(num_of_balls(balls=5))
