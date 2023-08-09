import random
from matplotlib import pyplot as plt
import numpy



Attempts = []
for _ in range(50):

    def Rounds():

        Suits = ["Diamonds","Spades","Hearts","Clubs"]
        Ranks = [1,2,3,4,5,6,7,8,9,10,"King","Queen","Jack"]



        Deck = {
    
        "Ace Spades":1,"Ace Hearts":1,"Ace Diamonds":1,"Ace Clubs":1,
        "Two Spades":2,"Two Hearts":2,"Two Diamonds":2,"Two Clubs":2,
        "Three Spades":3,"Three Hearts":3,"Three Diamonds":3,"Three Clubs":3,
        "Four Spades":4,"Four Hearts":4,"Four Diamonds":4,"Four Clubs":4,
        "Five Spades":5,"Five Hearts":5,"Five Diamonds":5,"Five Clubs":5,
        "Six Spades":6,"Six Hearts":6,"Six Diamonds":6,"Six Clubs":6,
        "Seven Spades":7,"Seven Hearts":7,"Seven Diamonds":7,"Seven Clubs":7,
        "Eight Spades":8,"Eight Hearts":8,"Eight Diamonds":8,"Eight Clubs":8,
        "Nine Spades":9,"Nine Hearts":9,"Nine Diamonds":9,"Nine Clubs":9,
        "Ten Spades":10,"Ten Hearts":10,"Ten Diamonds":10,"Ten Clubs":10,
        "King Spades":13,"Queen Spades":12,"Jack Spades":11,
        "King Hearts":13,"Queen Hearts":12, "Jack Spades":11,
        "King Diamonds":13,"Queen Diamonds":12, "Jack Diamonds":11,
        "King Clubs":13,"Queen Clubs":12,"Jack Clubs":11
        
     }




        Drawcard = {}


        Drawcard.update({(random.choice(Suits)):(random.choice(Ranks))})
        Randomcard = str(Drawcard)



        print("Your card is ") 
        print(Randomcard)
        Counter = 0

        for card in Deck:
            GuessCard = {(random.choice(Suits)):(random.choice(Ranks))}
            print("I guess ")
            print(str(GuessCard))
            Counter += 1

        
            


            if str(GuessCard) == Randomcard:
                print("That is your card")
                print("It took ")
                print(Counter)
                print("guesses.")
                Attempts.append(Counter)

             
        
        
                break

        else:
            print("I lose.")
            print("I guessed 51 times.")
            Attempts.append(51)

    Rounds()
    


#print(Attempts)



plt.plot(Attempts)
plt.show()