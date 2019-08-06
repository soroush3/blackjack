"""
This application effectively lets you play the popularly known poker game called
Blackjack. Basic functionality is implemented where the user can 'hit' or
'stay'. The dealer hand rules are followed where it must hit on a soft 17
(the total of the dealer hand that contains an ace and one or more cards). The
goal is to try and have a higher hand than the dealer.
General facts: standard 52 card deck, after the end of each hand, the whole
deck is reshuffled and redealt. The player is dealt a card, then the dealer,
and then again, for a total of two cards per person/dealer
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
        self.deck = list(itertools.product(range(2,11), [' of Hearts', ' of Diamonds',
                                                         ' of Clubs', ' of Spades']))

        

        # initialize hands(lists) for the dealer and player
        self.dealer_hand, self.player_hand = [], []

    def deal(self):
        """
        Effectively takes the shuffle deck and deals the cards to the player
        and dealer
        """
        # shuffle the cards
        random.shuffle(self.deck)
        for _ in range(2):
            # take the last card of the deck
            self.player_hand.append(self.deck.pop())
            self.dealer_hand.append(self.deck.pop())

def main():
    while True:
        blackjack = BlackJack()
        print(len(blackjack.deck))
        blackjack.deal()

        print(blackjack.player_hand, blackjack.dealer_hand)

        user_input = input("Would you like to play again? - (y)es or (n)o : ")
        print(user_input.lower())
        if user_input == "y" or user_input == 'n':
            continue
        else:
            print("DONEZO")
            break



if __name__ == "__main__":
    main()