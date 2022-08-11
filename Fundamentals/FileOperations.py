# w_file = open("file.txt", "w")
# w_file.write("Now the file has more content!")
# w_file.close()

#Write  "w"=overwrite the last file or "a"=append
with open("file.txt", "a") as w_file: #True
    w_file.write("Hello World!\n")
    w_file.write("Hello World!")

#READ FILE

with open("file.txt", "r") as w_file:

    # Method 1
    for line in w_file:
        print(line)
        #cod