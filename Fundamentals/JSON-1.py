# JSON (JavaScript Object Notation)
# JSON is a syntax(text) for storing and exchanging data
# JSON is nested lists and dictionaries

# peoples = [            #[] bracket is list, {} is dictionary
#     {
#         "name": "Sally",
#         "city": "Ottawa",
#         "age": 25
#     },
#     {
#         "name": "Roy",
#         "city": "Vancouver",
#         "age": 37
#     }
# ]

# for person in peoples:
#     for key in person:
#         print(key + ':', person[key])
#     print()

data = {
    "Canadian":
    [
        {
            "name": "Haley",
            "city": "Toronto",
            "age": 23
        },
        {
            "name": "Sam",
            "city": "Ottawa",
            "age": 22
        }
    ],
    "American":
    [
        {
            "name": "Tom",
            "city": "Las Vegas",
            "age": 30
        },
        {
            "name": "Lena",
            "city": "New York",
            "age": 34
        }
    ]
}

for citizen, person in data.items():
    print(citizen)
    for category in person:
        for detail in category: 
            print("    ", detail + ':', category[detail])
        print()    
    print()