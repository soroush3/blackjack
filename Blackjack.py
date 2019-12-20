"""
This program lets you play the popularly known poker game called
Blackjack. Basic functionality is implemented where the user can 'hit' or
'stay'. The dealer must hit on 16. The goal is to try and have a higher hand
than the dealer. General facts: standard 52 card deck, after the end of each
hand, the deck is refreshed, reshuffled and redealt.
"""
import itertools, random

class BlackJack:
    """
    This class consists of functions to allow for a game of blackjack to occur
    between a dealer and one other player. The various funtions are named
    appropriately and are apparent of their function
    """
    def __init__(self):
        """
        Initializer of the BlackJack class, creates a deck and shuffles the
        cards
        """
        # a list of standard deck of 52 playing cards
        self.deck = list(itertools.product(range(2,11), \
            [' of Hearts', ' of Diamonds',' of Clubs', ' of Spades']))

        self.cardValue = {"Jack":10, "Queen":10, "King":10, "Ace":11}

        for i in range(2, 11):
            self.cardValue[i] = i

        faceCards = ["Jack", "Queen", "King", "Ace"]
        suits = [' of Hearts', ' of Diamonds', ' of Clubs', ' of Spades']

        # finish building the deck with face cards now included
        for card in faceCards:
            for suit in suits:
                self.deck.append( (card, suit ))

        # initialize hands(lists) for the dealer and player
        self.dealer_hand, self.player_hand = [], []

    def shuffle(self):
        '''
        Quick Shuffle of the deck
        '''
        random.shuffle(self.deck)

    def deal(self):
        """
        Effectively takes the shuffled deck and deals the cards to the player
        and dealer
        """
        # shuffle the cards
        random.shuffle(self.deck)
        for _ in range(2):
            # take the last card of the deck
            self.player_hand.append(self.deck.pop())
            self.dealer_hand.append(self.deck.pop())

    def dealtBlackJack(self):
        "Checks if the dealer and/or player hit BlackJack after the deal"
        # both players hit blackjack
        if self.checkHandScore()[0] == 21 and self.checkHandScore()[1] == 21:
            return "tie"
        elif self.dealer_hand[0][0] == "Ace" and \
                self.cardValue[self.dealer_hand[1][0]] == 10:
            return "dealer"
        elif self.checkHandScore()[1] == 21:
            return "player"

    def checkForWinner(self):
        '''
        Checks for a win condition for both the dealer and player
        '''
        score = self.checkHandScore()
        if score[0] > 21:
            return "dealer bust"
        elif score[0] <= 21 and score[0] > score[1]:
            return "dealer"
        elif score[1] <= 21 and score[1] > score[0]:
            return "player"
        elif score[0] <= 21 and score[0] == score[1]:
            return "tie"

    def printHand(self, showAllDealer=False):
        '''
        Prints the hands of both the dealer and player
        If showAllDealer is true, prints both cards of dealers hand
        '''
        if showAllDealer:
            print("Dealer has:")
            for card in self.dealer_hand:
                print("    ", "".join(str(i) for i in card))

        elif not showAllDealer:
            print("Dealer has:\n    " + \
                str(self.dealer_hand[0][0])+self.dealer_hand[0][1] + \
                                "\n    Second card hidden")

        print()
        print("You have:")
        for card in self.player_hand:
            print("    ", "".join(str(i) for i in card))
        print()

    def checkHandScore(self):
        # returns the sum of the dealer's and player's hand
        return sum(self.cardValue[i[0]] for i in self.dealer_hand), \
                            sum(self.cardValue[i[0]] for i in self.player_hand)

    def play(self):
        '''
        Function to actually initiate the play between the player and dealer
        '''
        self.shuffle()
        self.deal()
        while True:
            # dealer and/or player may have hit blackjack from the deal
            check = self.dealtBlackJack()
            if check == "dealer":
                self.printHand(True)
                print("Dealer has BlackJack!\nYou have lost.")
                break
            elif check == "player":
                self.printHand(True)
                print("You have BlackJack!\nYou have won.")
                break
            elif check == "tie":
                self.printHand(True)
                print("Both the Dealer and you have BlackJack!\nYou have tied.")
                break

            self.printHand()
            # check if player wants to hit or stay
            while True:
                user_input = input(\
                    "Would you like to hit or stay? -(h)it, (s)tay: ").lower()
                if user_input == "h" or user_input == "hit":
                    self.player_hand.append(self.deck.pop())
                    score = self.checkHandScore()
                    if score[1] > 21:
                        self.printHand(True)
                        print("You busted!\nYou have lost.")
                        break
                    self.printHand()
                    continue
                elif user_input == "s" or user_input == "s":
                    self.printHand(True)
                    while self.checkHandScore()[0] <= 16:
                        self.dealer_hand.append(self.deck.pop())
                        self.printHand(True)
                    winner = self.checkForWinner()
                    if winner == "player":
                        print("You have won.")
                    elif winner == "dealer":
                        print("You have lost.")
                    elif winner == "tie":
                        print("You have tied.")
                    elif winner == "dealer bust":
                        print("The dealer busted!\nYou have won")
                    break
                else:
                    print("Invalid response, please try again.")
            break
if __name__ == "__main__":
    while True:
        blackjack = BlackJack()
        print()
        blackjack.play()
        
        oneMoreHand = True

        while True:
            user_input = input(\
                "Would you like to play again? - (y)es or (n)o : ").lower()
            if user_input == "y" or user_input == "yes":
                break
            elif user_input == "n" or user_input == "no":
                print("Thanks for playing!")
                oneMoreHand = False
                break
            else:
                print("Invalid response, please try again.")

        if not oneMoreHand:
            break