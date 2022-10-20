text_input = input()
cyclic_shift = input()
list = []


for x in range(len(cyclic_shift)):
    list.append(cyclic_shift[x:]+cyclic_shift[:x])
string_in_text = False

for string in list:
    if string in text_input:
        string_in_text = True
        break
if string_in_text == False:
    print("no")
else:        
    print("yes")        
