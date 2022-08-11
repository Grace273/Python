with open("songs.txt", "r") as w_file:

    # # Method 1
    # for line in w_file:
    #     print(line.replace("\n", "")) # without .replace, there would be a \n from "print" and another from "line"

    # # Method 2 - Only read the first line of the file
    # one_line = w_file.readline()
    # print(one_line)

    # Method 3 
    all_lines = w_file.readlines()
    print(all_lines)