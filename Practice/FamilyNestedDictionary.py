my_family = {
    "child_1": {
        "name": "Grace",
        "birth_year": 2006,
        "allergy": False
    },
    "child_2": {
        "name": "Tyler",
        "birth_year": 2010,
        "allergy": False
    },
    "pet": {
        "name": "Meow",
        "birth_year": 2016,
        "allergy": True
    },
}

# for key, value in my_family.items(): #.items() picks up all the items so you can have a value variable or else you have to do dict[key]
for member, detail in my_family.items(): #member and detail are variables that hold the items
    print(member)
    for key in detail:
        print("    ", key + ':', detail[key])

