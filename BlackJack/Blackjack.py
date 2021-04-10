#! /usr/bin/env python3
import random
p1cards = []
p2cards = []

def dealer():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return(card)

def blackjack():
    p1sum = sum(p1cards)
    p2sum = sum(p2cards)
    if p1sum == 21:
        return(1)
    elif p2sum == 21:
        return(2)
    else:
        return(0)

def game():
    def deal(select):
        if select == 1:
            p1cards.append(dealer())
        if select == 2:
            p2cards.append(dealer())
        if select == 3:
            p1cards.append(dealer())
            p2cards.append(dealer())  
    
    def begin():
        deal(3)
        deal(3)
        if blackjack() == 1:
            print('You got Blackjack!')
        else:
            print('Your cards: ' + str(p1cards))
            print('Your score: ' + str(sum(p1cards)))
            print('Dealers Hand: ' + str(p2cards[0]))
            userin = input("Y for hit N for stay: ")
            while userin.upper() == 'Y':
                deal(1)
                print('Your cards: ' + str(p1cards))
                print('Your score: ' + str(sum(p1cards)))
                userin = input("Another?: ")
            show()
    def show():
        print('Your Final Hand: ' + str(p1cards) + ' , Final Score: ' + str(sum(p1cards)))
    begin()



def start():
    print('Welcome To Blackjack!')
    userin = input('Want to play a game? (Y/N): ')
    if userin.upper() == 'Y':
        game()
    elif userin.upper() == 'N':
        print("Why are you even here then?")
start()