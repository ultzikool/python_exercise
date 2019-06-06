
import pickle

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')



def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins,secs) = time_string.split(splitter)

    return(mins + '.' +secs)


clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_sarah = [sanitize(each_t) for each_t in sarah]


'''
print("降序排列")
print(sorted(clean_james,reverse = True))
print(sorted(clean_julie,reverse = True))
print(sorted(clean_mikey,reverse = True))
print(sorted(clean_sarah,reverse = True))
print("升序排列")
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
'''


james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])

unique_james = []
for m in james:
	if m not in unique_james:
		unique_james.append(m)

unique_julie = []
for m in julie:
	if m not in unique_julie:
		unique_julie.append(m)

unique_mikey = []
for m in mikey:
	if m not in unique_mikey:
		unique_mikey.append(m)

unique_sarah = []
for m in sarah:
	if m not in unique_sarah:
		unique_sarah.append(m)

print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])