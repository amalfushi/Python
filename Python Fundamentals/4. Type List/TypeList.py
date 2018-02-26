#input variables
x = ['magical unicorns',19,'hello',98.98,'world']
y = [2,3,1,7,4,12]
z = ['magical', 'unicorns']

def typeList(varList):
    resultString = "String: "
    sum = 0
    ints = 0
    strings = 0
    for val in varList:
        if isinstance(val, str):
            strings += 1
            resultString += val + " "
        elif isinstance(val, int) or isinstance(val, float):
            ints += 1
            sum += val
            
    if ints != 0 and strings !=0:
        print ("The list you entered is of mixed type")
        print (resultString)
        print ("Sum: " + str(sum))

typeList(x)