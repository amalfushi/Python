import random

def coinToss(howMany=20):
    heads = 0
    tails = 0
    for attempt in range(1, howMany+1):
        x = round(random.random())

        string = "Attempt #" + str(attempt) + " Throwing a coin... It's a "

        if x == 0:
            heads += 1
            string += "head"
        else:
            tails += 1
            string += "tail"

        string += "!... Got " + str(heads) + " heads(s) so far and " + str(tails) + " tail(s) so far"
        print string

coinToss(5000)