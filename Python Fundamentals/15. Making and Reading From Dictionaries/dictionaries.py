dustin = {'name':'Dustin', 
    'age': 29, 
    'country of birth':'The United States',
    'favorite language':'Parseltongue']

#not in order
def printDict(dictionary):
    for key, val in dictionary:
        print "My ", key, " is ", val

printDict(dustin)