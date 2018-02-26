numbers = ['x',1,2,3,4,5,6,7,8,9,10,11,12]

for row in range(0, len(numbers)):
    string = ""
    
    if row == 0:
        string += "x "
        for column in range(1, len(numbers)):
            string += str(numbers[column]) + " "
    else:
        string += str(row) + " "
        for column in range(1, len(numbers)):
            string += str(numbers[row]*numbers[column]) + " "
    print (string)