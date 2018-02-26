def scoresAndGrades (val):
    score = val
    string = "Score: " + str(score) +"; Your grade is "
    if score >= 90:
        string += "A"
    elif score >= 80:
        string += "B"
    elif score >= 70:
        string += "C"
    elif score >= 60:
        string += "D"
    else:
        string += "F"
    print string

import random
print "Scores and Grades"
for score in range(0, 10):
    random_num = scoresAndGrades(random.randint(60,101))
print "End of the program. Bye!"