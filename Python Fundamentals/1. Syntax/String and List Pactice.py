words = "It's thanksgiving day.  It's my birthday, too!"
print (words.find("day"))

newWords = words.replace("day", "month")
print (newWords)

x = [2, 54, -2, 7, 12, 98]
print (min(x))
print (max(x))

y = ["hello", 2, 54, -2, 7, 12, 98, "world"]
newY =[]
newY.append(y[0])
newY.append(y[len(y)-1])
print (newY)

v = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
def sortAndHalve(numList):
    numList.sort()
    p = []
    for idx in range(0, int(len(numList)/2)):
        p.append(numList[idx])
        print (p)
        
    for idx in range(1, int(len(numList)/2)):
        numList.pop(1)
        print (numList)
    numList[0] = p
    return numList
    
print(sortAndHalve(v))
