import os
def method_1(): 
 # in terminal: "\": Windows "/": Linux  with open("Sample/song.txt", "r") as w_file
    with open("songs.txt", "r") as r_file:
        for line in r_file:
            #print(line.strip()) remove all space from front and end of line
            # lstrip(), rstrip(), remove "whitespace"
            print(line.replace("\n", "")) # without .replace, there would be a \n from "print" and another from "line"

def method_2(): #Only read the first line of the file
    with open("songs.txt", "r") as r_file:
        while True:
            one_line = r_file.readline()
            if one_line: #if line has something
                print(one_line.strip())
                #print(one_line.replace("\n", ""))
            else:
                break;

def method_3():   #puts output in a list
    with open("songs.txt", "r") as r_file:
        all_lines = r_file.readlines()
        # for i in range(len(all_lines)) :
        #     print(all_lines[i].replace("\n", ""))
        for item in all_lines:
            print(item.replace("\n", ""))  

# method_1()
method_2()
# method_3()