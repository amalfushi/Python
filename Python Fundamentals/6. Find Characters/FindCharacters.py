#Find Characters
##input a list of strings and a string to search for in that list

word_list = ['hello', 'world', 'my', 'name', 'is', 'Dustin']
char = 'o'

def findCharacters(wList, findChar):
    newList = []
    for val in wList:
        if findChar in val:
            newList.append(val)
    print (newList)
findCharacters(word_list, char)