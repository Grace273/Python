import json

str_json =  '[{"name": "John", "city": "Ottawa", "age": 30}, {"name": "Smith", "city": "Toronto", "age": 31}]'#string
data = json.loads(str_json) #JSON load from string
print(str_json)
print(type(data))
print(data)
print(data[0]["age"])
print(data[1]['city'])
# no difference between '' and "" but two of the same set of quote in a row may cause problem
# var = '"abc"'
# print(var)

#once you put this list into the file, it saves to your workspace and you don't need to access the website anymore
