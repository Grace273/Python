#Dictionary called map in C++, ascending order

car_dict = {
    "brand": "Toyota",
    "model": "Corolla Sport",     # Key: Value
    "year": 2016
}
print(car_dict)
print(len(car_dict))              # len is length
print(car_dict["model"])           # try the key "model1", doesn't exist raises error
print(car_dict.get("model1"))       # try the key "model1", doesn't exist outputs "None"
if "model" in car_dict:
    print("Yes, 'model' is in the car_dict dictionary")