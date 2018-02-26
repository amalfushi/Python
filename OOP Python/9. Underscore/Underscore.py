class Underscore(object):
    #returns a new list based by applying a function to every value in a list
    def map(self, arr, function):
        newArr = []
        for val in arr:
            newArr.append(function(val))
        return newArr
    
    #reduces the list to a single value based on the function passed
    #'reduce' is reserved
    def rReduce(self, arr, function):
        newVal= arr[0]
        for num in range(0, len(arr)-1):
            newVal = function(newVal, arr[num+1])
        return newVal

    #returns the first value of a list in which the function is true
    def find(self, arr, function):
        for val in arr:
            if function(val):
                return val
    
    #returns a list of values in which the function is true
    def filter(self, arr, function):
        newArr = []
        for val in arr:
            if function(val):
                newArr.append(val)
        return newArr

    #same as above, but returns the values that are false
    def reject(self, arr, function):
        newArr =[]
        for val in arr:
            if not function(val):
                newArr.append(val)
        return newArr


_ = Underscore()
numList = [1,2,3,4,5,6]


def multBy4(num):
    return num*4
mapped = _.map(numList, multBy4)
print "numList has been mapped via multBy4 function: ", mapped

def multiplyStuffTogether(num1, num2):
    return num1*num2
reduced = _.rReduce(numList, multiplyStuffTogether)
print "numList has been reduced via multipling values togther: ", reduced

def isMultipleOf3(num):
    return num % 3 == 0.0
find = _.find(numList, isMultipleOf3)
print "The first value in numList that is a multiple of 3 is: ", find

allMultsOf3 = _.filter(numList, isMultipleOf3)
print "numList filtered to all values that are multiples of 3 is: ", allMultsOf3

notMultsOf3 = _.reject(numList, isMultipleOf3)
print "The reject values of numList that aren't multiples of 3 is: ", notMultsOf3