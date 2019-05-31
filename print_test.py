movies = ["The Holy Grail","The Life of Brian","The Meaning of Life"]
print(movies[1])

print("")

cast = ["Cleese","Palin","Jones","Idle"]
#打印列表cast
print(cast)

print("")

#打印列表cast的长度
print(len(cast))

print("")

#打印cast[1]
print(cast[1])

print("")

#在列表末尾增加一个数据项
cast.append("Gilliam")
print(cast)

print("")

#在列表末尾删除数据
cast.pop()
print(cast)

print("")

#在列表末尾增加一个数据项集合
cast.extend(["Gilliam","Chapman"])
print(cast)

print("")

#在列表中找到并删除一个特定的数据项
cast.remove("Chapman")
print(cast)

print("")

#在某个特定的位置前面增加一个数据项
cast.insert(0,"Chapman")
print(cast)

print("")


#for迭代处理数据
fav_movies = ["The Holy Grail","The Life of Brian"]

for each_flick in fav_movies:
    print(each_flick)

print("")

#while迭代处理数据
fav_movies = ["The Holy Grail","The Life of Brian"]

count = 0
while count < len(fav_movies):
    print(movies[count])
    count += 1

print("")

#列表镶嵌列表中
movies = ["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry jones"]]]
print(movies[4][1][3])
print(movies)

print("")

'''#条件语句
for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)
'''
print("")
111111111
