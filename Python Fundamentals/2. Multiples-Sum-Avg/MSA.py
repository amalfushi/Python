##Multiples
###Part 1 -- print all odd between 1 and 1000
def printOdds():
    for num in range(1, 1000):
        if num%2!=0:
            print(num)

###Part 2  -- multiples of 5 between 5 and 1,000,
def printFives():
    for num in range(5, 1000000):
        if num%5==0:
            print(num)

##Sum List -- Prints the sum of a list
a =  [1 ,2, 5, 10, 255, 3]
def sumList(numList):
    sum = 0
    for entry in numList:
        sum += entry
    print (sum)

##Average List -- Prints the average of a list
def avgList(numList):
    avg = 0
    for entry in numList:
        avg += entry
    print (avg/len(numList))

sumList(a)
avgList(a)
