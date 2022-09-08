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

for key in my_family:
    print(key)
    for p_id, p_info in my_family.items():
        for key in p_info:
            print("    ", key + ':', p_info[key])

