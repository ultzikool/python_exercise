import os

with open("sketch.txt", "r") as the_file:

#逐行打印
    print(the_file.readline(),end="")
    print(the_file.readline(),end="")



#退回最开始
    the_file.seek(0)
    for each_line in the_file:
        print(each_line,end="")


