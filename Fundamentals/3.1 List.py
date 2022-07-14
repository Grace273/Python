# List (any type, use bracket)

fruit_list = ["apple", "banana", "cherry", "pineapple"] #string
print(fruit_list)
print(fruit_list[1])            # index 1: banana because apple = 0
print(fruit_list[-2])           # index -1 is the last one, -2 is second last, etc.
print(fruit_list[0:2])          #items from index 0 to 2, index 2 is NOT included

print(len(fruit_list))          # Size of list

# don't need to define datatype so you can put whatever

other_list = ["apple", "banana", "cherry", 1, 10, "a", 5.3]     

if 1 in other_list:             # C++ use find function
    print("Yes, '1' is in the fruits list")

# M O D I F Y

fruit_list.append("orange")     # Add fruit to fruit_list to the end of the list
fruit_list.insert(2, "pear")    # Add fruit to fruit_list in between by index
fruit_list[1] = "blackcurrant"  # Modify item
print(fruit_list)

# R E M O V E

fruit_list.remove("cherry")     # Remove specific item
fruit_list.pop()                # Remove the last element
fruit_list.pop(1)               # Remove fruit_list[1]
print(fruit_list)

#fruit_list.clear()              # Empties the list
#print(fruit_list)

# I T E R A T E

for i in range(len(fruit_list)) : # Iterate by index, ex: 5; i: 0, 1, 2, 3, 4
    print(fruit_list[i])

for fruit in fruit_list:
    print(fruit)                  # Iterate list by item, the value is in the variable fruit

# C O P Y
new_fruit_list = ["grape", "berry"]
#just pointer, change new_fruit_list will change fruit_list
new_fruit_list = fruit_list #should avoid doing this
print(fruit_list)
# if New_fruit_list[0] = "a", so fruit_list[0] is "a" now

# two different list have same data
new_fruit_list = fruit_list.copy()
print(fruit_list)
# if New_fruit_list[0] = "a", so fruit_list[0] is still "grape" now

# S O R T

# Sort the list, the list will change order
list_1 = [6, 1, 19, 21, 3]
list_1.sort()
print(list_1)

old_list = list_1
# Make new list with sorted list
new_list = sorted(old_list)
print(old_list)

print(new_list)

# E X T E N D

list_1 = ["a", "bbb", "cccc"]
list_2 = [1, 2.12, 0.3]

list_3 = list_1 + list_2
print(list_3)

#list_1.extend(list_2)
#print(list_1)
#print(list_2)

# A P P E N D
list_1.append(list_2)
print(list_1)
#append list to list

# T U P L E - Immutable/unmodifiable list (any type, use bracket)
fruit_tuple = ["apple", "banana", "cherry", "pineapple"] #string
print(fruit_tuple)
print(fruit_tuple[1])            # index 1: banana because apple = 0
print(fruit_tuple[-2])           # index -1 is the last one, -2 is second last, etc.
print(fruit_tuple[0:2])          #items from index 0 to 2, index 2 is NOT included

# S E T - Unordered collections of unique elements (any type, use curly bracket)
fruit_set = {"apple", "cherry", "banana"}
fruit_set.add("orange")
fruit_set.add("apple") # set only keeps one of each item
print(fruit_set)

# Set in C++ is in ascending order
# Set in python is not in order

sorted(fruit_set)
print(sorted(fruit_set))