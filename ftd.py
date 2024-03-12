import random 

global guesses
guesses = 2


def createDeck():
    rank  = list(range(2, 11))
    #my deck
    suits = ["H", "D", "C", "S"]
    faces = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    deck = []
    for suit in suits:
        for card in rank:
            deck.append(str(card) + suit)  
        for face in faces:
            deck.append(face + suit)
    return deck

def numExtract(card):
    return  int(card[-1])



def printDeck(deck):
    for card in deck:
        print(card)




def game(deck, playerNum):
    random.shuffle(deck)
    print("Shuffling deck...")
    print('Deck is now shuffled')
    startingPlayer = random.randint(0, playerNum - 1)
    print("The starting player is: " + str(startingPlayer))
    dealer = deck.pop()
    print("The dealer's card is: " + dealer)
    turns = 1
    for i in range(turns):
        print("dealer is "  + dealer + " and num of guesses is " + str(turns))
        guess = input("Guess the dealer's card? (e.g., 7S for 7 of Spades): \n")
        if guess == dealer:
            print("You guessed right! You win!")
            if turns == 1:
                extract = (numExtract  *2)
                print(dealer + " has to drink for " + extract + " seconds!")
        else:
            print("You guessed wrong! You lose!")
            print("The dealer's card was: " + dealer)
            print("Better luck next time!")



    
    

def main():
    print("Lets play F**k the dealer!")
    playerNum = input("Players join within 10 seconds by reacting with a thumbs up/ typing the num of players \n")

    print("The number of players is: " + playerNum)
    print("Creating deck...") 
    deck = createDeck()
    printDeck(deck)
    game(deck, int(playerNum))


if __name__ == "__main__":
    main()