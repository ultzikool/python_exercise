from list_print_function import print_lol
import pickle
'''
try:
    data = open("missing.txt")
    print(data.readline(),end = "")
except IOError as err:
    print('File error:' + str(err))
finally:
    if 'data' in locals():
        data.close()
'''


'''
try:
    with open('its.txt','w') as data:
        print("It's...",file = data)
except IOError as err:
    print('File error:' + str(err))
'''
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

try:
    with open('man_data.txt','wb') as man_file:
        pickle.dump(man, man_file)
    with open('other_data.txt','wb') as other_file:
        pickle.dump(other, other_file)
except pickle.PickleError as err:
    print('Pickling error:' + str(err))
