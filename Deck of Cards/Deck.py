from Card import Card
import random

class Deck(object):
    def __init__(self):
        self.thisDeck = []

    def newDeck(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        cFaces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

        value = 0
        for suit in suits:
            for number in cFaces:
                if(number == "Jack"):
                    value = 10
                elif(number == "Queen"):
                    value = 10
                elif(number == "King"):
                    value = 10
                elif(number == "Ace"):
                    value = 11 ####### should be 1 OR 11
                else:
                    value = number

                newCard = Card(suit, number, value)
                self.thisDeck.append(newCard)
        return self

    def shuffle(self):
        for num in range(0, 51):
            rand = random.randint(0,51)
            temp = self.thisDeck[num]
            self.thisDeck[num] = self.thisDeck[rand]
            self.thisDeck[rand] = temp
        return self
    def display(self):
        for card in self.thisDeck:
            card.display()
        return self

    def removeCard(self, card):
        self.thisDeck[card.suit].remove(card.cFace)
        return self

if __name__ == "__main__":
    d1 = Deck()
    d1.newDeck().display()
    d1.shuffle().shuffle().shuffle().display()
