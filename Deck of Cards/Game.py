from Card import Card
from Deck import Deck
from Player import Player

p1 = Player()
dealer = Player()
class Game(object):
    def __init__(self):
        self.round = 0
        self.cardIndex = 0
        self.deck = Deck()
        self.continuePlaying = True
    def playGame(self):
        if self.round == 0:
            self.play = raw_input('\n\nWelcome to BlackJack! You have been awarded $100! Enter yes if you would like to place a bet: ')
        else: 
            self.play = raw_input("You have {} dollars left. Would you like to continue playing? ".format(p1.cashValue))

        if self.play == 'yes':
            self.deck.newDeck().shuffle().shuffle()
            self.listenforbet()
            self.dealCard(p1)
            self.dealCard(p1)
            self.dealCard(dealer)
            self.dealCard(dealer)
            p1.showHand()
            self.listenforplayer()
            self.dealerDrawCards()
            if self.continuePlaying:
                self.compareHands()
        else:
            print 'Thanks for playing'

    def dealCard(self, aPlayer):
        aPlayer.hand.append(self.deck.thisDeck[self.cardIndex])
        self.cardIndex += 1

    def listenforbet(self):
        self.bet = raw_input("Good choice! How much would you like to bet?: ")
        self.continuePlaying = True
        p1.placebet(int(self.bet))

    def listenforplayer(self):   
        
        while self.continuePlaying == True:
            self.hit = raw_input('Would you like to hit? Enter yes of no please: ')
            if self.hit == 'yes':
                print '\nHere are your cards'
                self.dealCard(p1)
                p1.showHand()
                if p1.checkForBust():
                    # print p1.checkForBust()
                    self.continuePlaying == False
                    print 'YOU LOSE!'
                    p1.resetHand()     
            else:
                self.continuePlaying == False
                break

    def dealerDrawCards(self):
        while dealer.getHandValue() <= 17:
            self.dealCard(dealer)

    def compareHands(self):
        print "Dealer's Hand"
        dealer.showHand()
        if p1.getHandValue() > dealer.getHandValue():
            print "YOU WIN"
            p1.cashValue += (p1.bet * 2)
            p1.resetHand()
            dealer.resetHand()
        elif p1.getHandValue() == dealer.getHandValue():
            "You Tied!"
            p1.resetHand()
            dealer.resetHand()
        else:
            if dealer.getHandValue() >21:
                print "YOU WIN!"
            else:
                print 'YOU LOSE!'
            dealer.resetHand()
            p1.resetHand()
game1 = Game()
game1.playGame()