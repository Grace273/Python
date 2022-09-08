#Dictionary called map in C++, ascending order

from tkinter import N


car_dict = {
    "brand": "Toyota",
    "model": "Corolla Sport",     # Key: Value
    "year": 2016
}
print(car_dict)
print(len(car_dict))              # len is length
# print(car_dict["model1"])           # try the key "model1", doesn't exist raises error
print(car_dict.get("model1"))       # try the key "model1", doesn't exist outputs "None"
if "model" in car_dict:
    print("Yes, 'model' is in the car_dict dictionary")

#ADD ITEM
car_dict["seats"] = 5

#MODIFY year, if "year" exists
car_dict["year"] = 2018

print(car_dict)

# #Remove specific item
# car_dict.pop("model") # or
# #del car_dict["model"]

# #Removes the last inserted item
# car_dict.popitem()

# #Delete dictionary completely
# car_dict.clear() # or
# #del car_dict

#ITERATE
for key in car_dict:
    print(key)
    print(car_dict[key]) #or
    print("Key: {}, Value: {}".format(key, car_dict[key]))

for key, value in car_dict.items():
    print(key, value) #or
    print(f"Key: {key}, Value: {value}")

for value in car_dict.values():
    print(value) #dont know what key is

#COPY
#Just pointer, change new_car_dict will change car_dict
new_car_fict = car_dict

#Two different list have same data, more common
new_car_dict = car_dict.copy()

#SORT

for key in sorted(car_dict):
    print(key)
    print(car_dict[key])



#Nested Dictionaries

my_family = {
    "child_1": {
        "name": "Anne",
        "birth_year": 2004,
        "allergy": False
    }
}

