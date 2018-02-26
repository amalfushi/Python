def draw_stars(starList):
    for val in starList:
        if isinstance(val, int):
            print (buildString(val))
        elif isinstance(val, str):
            print (buildString(len(val), val[0]))

def buildString(numTimes, symbol="*"):
    string =""
    for times in range(numTimes):
        # print times
        string += symbol
    return string

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

y = ['taco', 4, 6, 'banana']
draw_stars(y)