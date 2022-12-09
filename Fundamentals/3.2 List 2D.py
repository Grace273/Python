# list_2d = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in list_2d:
#     for j in i:
#         print(j, end = " ")
#     print('\n')

# nested_dict = {
#     'ground_1': {'1': 1, '2': 2, '3': 3},
#     'ground_2': {'4': 4, '5': 5, '6': 6},
#     'ground_3': {'7': 7, '8': 8, '9': 9}
# }

# for ground, value in nested_dict.items(): #items give you the key AND the value
#     for name in value:
#         for number in name:
#             print(number, end = " ")
#     print()

json = [
    {'1': 1, '2': 2, '3': 3},
    {'4': 4, '5': 5, '6': 6},
    {'7': 7, '8': 8, '9': 9}
]

# for dictionary in json:
#     for key in dictionary:
#         for value in key:
#             print(value, end = " ")
#     print()

for item in json:
    for key, value in item.items(): # using .items() THE PROPER WAY
        print(f'{key}:{value}', end = " ") # you can also use '+' sign for no extra space
    print()

for item in json:
    for key in item:
        print(f'{key}:{item[key]}', end = " ")
    print() 
