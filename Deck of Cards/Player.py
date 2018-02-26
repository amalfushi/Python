from Card import Card
class Player(object):
    def __init__(self):
        self.hand = []
        self.isBust = False
        self.bet = 0
        self.cashValue = 100
    def placebet(self, bet):
        self.bet = bet
        self.cashValue -= self.bet
        return self
    def addCard(self, card):
        self.hand.append(card)
        return self

    def getHandValue(self):
        temp = 0
        for card in self.hand:
            # card.display()
            temp += card.getCardValue()
        return temp

    def currentCashValue(self):
        if self.isBust == True:
            self.cashValue = cashValue - self.bet
        else:
            self.cashValue = cashValue + (self.bet * 2)

    def checkForBust(self):
        if self.getHandValue() > 21:
            self.isBust = True
        return self.isBust

    def showHand(self):
        for Card in self.hand:
            print Card
        print self.getHandValue() , '\n'
        return self

    def resetHand(self):
        self.hand = []