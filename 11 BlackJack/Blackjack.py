#! /usr/bin/env python3
import random
from art import logo
import subprocess

def dealer():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    return(random.choice(cards))

def scorer(cards):
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    elif sum(cards) > 21:
        score = 0
    else:
        score = sum(cards)
    return(score)

def compare(p1cards, p2cards):
    p1score = scorer(p1cards)
    p2score = scorer(p2cards)
    if p1score == 0:
        print('You Bust!')
    elif p2score == 0:
        print('Dealer Bust, You Win!')
    elif p1score == 21 or p2score == 21:
        if p1score ==21 and p2score == 21:
            print('You Both got Blackjack, Tie')
        if p1score == 21:
            print('You Got Blackjack!')
        if p2score == 21:
            print('Dealer Got Blackjack!')
    elif p2score > p1score:
        print('Dealer wins with a higher score!')
    elif p1score == p2score:
        print('Tie!')

def Play():
    print(logo)
    p1cards = []
    p2cards = []
    gameover = False
    for i in range(2):
        p1cards.append(dealer())
        p2cards.append(dealer())
        i
    while gameover == False:
        p1score = scorer(p1cards)
        p2score = scorer(p2cards)
        print(f'    Your Cards: ' + str(p1cards) + ' Your Score: ' + str(p1score))
        print(f'    Dealers First Card: ' + str(p2cards[0]))
        if p1score == 0 or p2score == 0 or p1score == 21:
            gameover = True
        else:
            Deal = input('Would You Like Another Card? (y/n)')
            if Deal == 'y':
                p1cards.append(dealer())
            else:
                gameover = True
    while p2score != 0 and p2score < p1score and p2score != 21:
        p2cards.append(dealer())
        p2score = scorer(p2cards)
    print('Your Final Hand: ' + str(p1cards) + ' Your Final Score: ' + str(p1score))
    print('Dealers Final Hand ' + str(p2cards) + ' Dealers Final Score: ' + str(p2score))
    compare(p1cards, p2cards)
    
while input('Want to play 11 BlackJack? (y/n): ') == 'y':
    subprocess.run(['clear'])
    Play()
else:
    print('Why Are You Even Here Then?')