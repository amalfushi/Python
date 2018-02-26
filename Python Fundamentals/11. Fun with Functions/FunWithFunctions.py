def odd_even(n1, n2):
    for number in range(n1, n2):
        pString = "Number is " + str(number) +". "
        if number % 2 == 0:
            pString += "This is an even number."
        else:
            pString += "This is an odd number."
        print(pString)

def multiply(mList, mult):
    newList = []
    for val in mList:
        newList.append(val*mult)
    return newList

def layered_multiples(arr):
    newArr = []
    for val in arr:
        pushArr = []
        for num in range(0, val):
            pushArr.append(1)
        newArr.append(pushArr)
    return newArr


odd_even(1, 20)

a = [2,4,10,16]
b = multiply(a, 5)
print b

x = layered_multiples(multiply([2,4,5],3))
print x