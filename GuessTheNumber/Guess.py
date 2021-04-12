#! /usr/bin/env python3
import random
import subprocess


def menu():
    subprocess.run(['clear'])
    print('Welcome to The Number Game!')
    print("I'm thinking of a number between 1 and 100")
    difficulty = input('Choose a difficulty, Easy or Hard:')
    return difficulty


def picknumber():
    r = random.choice(range(0, 100))
    return(r)


def compare(guess, number):
    guess = int(guess)
    if guess > number:
        r = 0
        print('Too High!')
    elif guess < number:
        r = 1
        print('Too Low!')
    elif guess == number:
        r = 2
        print('You Got It!')
    return(r)


def game():
    difficulty = menu().lower()
    number = picknumber()
    comp = ()
    if difficulty == 'easy':
        guesses = 10
    if difficulty == 'hard':
        guesses = 5
    while guesses > 0 and comp !=2:
        guess = input('Guess a Number: ')
        comp = compare(guess, number)
        guesses -= 1
        print('Guesses Remaining: ' + str(guesses))
    if guesses == 0 and comp != 2:
        print('You Ran Out of Guesses!')


gameover = False
while gameover == False:
    game()
    user = input('Play Again? (y/n):')
    if user == 'n':
        gameover = True
    