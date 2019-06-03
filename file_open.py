import os

'''with open("sketch.txt", "r") as the_file:

#逐行打印
    print(the_file.readline(),end="")
    print(the_file.readline(),end="")

    print("")

#退回最开始
    the_file.seek(0)
    for each_line in the_file:
        print(each_line,end="")

    the_file.close()'''

'''
#抽取数据
the_file = open("sketch.txt")
for each_line in the_file:
    (role,line_spoken) = each_line.split(":",1)
    print(role, end="")
    print(" said: ",end="")
    print(line_spoken,end="")
print("")
'''

'''
#find（）查找
with open("sketch.txt", "r") as the_file:

    for each_line in the_file:
        if not each_line.find(":") == -1:
            (role,line_spoken) = each_line.split(":",1)
            print(role, end="")
            print(" said: ",end="")
            print(line_spoken,end="")

the_file.close()
'''
'''
#异常处理1
with open("sketch.txt", "r") as the_file:

    for each_line in the_file:
        try:
            (role,line_spoken) = each_line.split(":",1)
            print(role, end="")
            print(" said: ",end="")
            print(line_spoken,end="")
        except:
            pass
        
the_file.close()
'''

'''
#判断文件是否存在
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    for each_line in data:
        if not each_line.find(":") == -1:
            (role,line_spoken) = each_line.split(":",1)
            print(role, end="")
            print(" said: ",end="")
            print(line_spoken,end="")
    data.close()
else:
    print('The data file is missing!')
'''

'''
#异常处理2
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(":",1)
            print(role, end="")
            print(" said: ",end="")
            print(line_spoken,end="")
        except ValueError:
            pass
        
    data.close()
except IOError:
    print('The data file is missing!')
'''

'''
#持久储存
man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(":",1)
            line_spoken = line_spoken.strip() #strip()方法从字符串中取出不想要的空白符
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
        
    data.close()
except IOError:
    print('The datafile is missing!')

print(man)
print(other)
'''

#读写储存
man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(":",1)
            line_spoken = line_spoken.strip() #strip()方法从字符串中取出不想要的空白符
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
        
    data.close()
except IOError:
    print('The datafile is missing!')


try:
    
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')
    
    print(man,file = man_file)
    print(other,file = other_file)
    man_file.close()
    other_file.close()
except IOError:
    print("File error")


