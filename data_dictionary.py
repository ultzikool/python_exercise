
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins,secs) = time_string.split(splitter)

    return(mins + '.' +secs)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return({'Name' : templ.pop(0),'DOB' : templ.pop(0), 'Times' : str(sorted(set([sanitize(t) for t in templ]))[0:3])})
        
    except IOError as ioerr:
        print('FIle error:' + str(ioerr))
        return(None)



sarah = get_coach_data('sarah2.txt')
print(sarah['Name'] +"'s fastest times are:" + sarah['Times'])

#(sarah_name , sarah_dob) = sarah.pop(0) , sarah.pop(0)

#print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

'''
sarah_data = {}
sarah_data['name'] = sarah.pop(0)
sarah_data['DOB']  = sarah.pop(0)
sarah_data['Times'] = sarah

print(sarah_data['name'] + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
'''


