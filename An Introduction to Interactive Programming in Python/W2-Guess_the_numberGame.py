'''
Created on May 1, 2013
@author: Nenad

One of the simplest two-player games is “Guess the number”. The first player thinks of a secret number in some known range
while the second player attempts to guess the number. After each guess, the first player answers either “Higher”, “Lower” or
“Correct!” depending on whether the secret number is higher, lower or equal to the guess.
In this project, you will build a simple interactive program in Python where the computer will take the role of the first 
player while you play as the second player.

http://www.codeskulptor.org/#user11_mA3fVzJWUB_0.py
'''

import simplegui, random, math

low, high, attempts = 0, 100, 0
attemptsTotal = math.ceil(math.log((high-low),2))
secretNum = random.randrange(low, high)

def init():
    print("Started new game in range 0 - 100")
    print("You have " + str(attemptsTotal - attempts) + " attempts left!")
    print("")

def range100():
    global low, high, attempts, attemptsTotal, secretNum
    low, high, attempts = 0, 100, 0
    attemptsTotal = math.ceil(math.log((high-low),2))
    secretNum = random.randrange(low, high)
    print("Started new game in range 0 - 100")
    print("You have " + str(attemptsTotal - attempts) + " attempts left!")
    print("")
    l1.set_text("Attempts left: " + str(attemptsTotal - attempts))

def range1000():
    global low, high, attempts, attemptsTotal, secretNum
    low, high, attempts = 0, 1000, 0
    attemptsTotal = math.ceil(math.log((high-low),2))
    secretNum = random.randrange(low, high)
    print("Started new game in range 0 - 1000")
    print("You have " + str(attemptsTotal - attempts) + " attempts left!")
    print("")
    l1.set_text("Attempts left: " + str(attemptsTotal - attempts))
    
def get_input(guess):
    global secretNum, low, high, attempts
    if guess != "":
        attempts = attempts + 1
        print("Your attempt no " + str(attempts) + " was: " + guess)
    if float(guess) < secretNum:
        if attemptsTotal != attempts:
            print("Go higher!")
            print("You have " + str(attemptsTotal - attempts) + " attempts left!")
        else:
            print("Game over! You used all of your attempts!")
            print("The secret number was: " + str(secretNum))
            print("_________________________")
            secretNum = random.randrange(low, high)
            attempts = 0
        print("")
        iGuess.set_text("")
    elif float(guess) > secretNum:
        if attemptsTotal != attempts:
            print("Go lower!")
            print("You have " + str(attemptsTotal - attempts) + " attempts left!")
        else:
            print("Game over! You used all of your attempts!")
            print("The secret number was: " + str(secretNum))
            print("_________________________")
            secretNum = random.randrange(low, high)
            attempts = 0
        print("")
        iGuess.set_text("")
    elif float(guess) == secretNum:
        print("Correct! The secret number was: " + str(secretNum))
        print("You made it in " + str(attempts) + " attempts!")
        print("_________________________")
        secretNum = random.randrange(low, high)
        attempts = 0
        print("")
        iGuess.set_text("")
    l1.set_text("Attempts left: " + str(attemptsTotal - attempts))         

frame = simplegui.create_frame("Guess the number", 0, 300)
l0 = frame.add_label("Select the range to restart:")
frame.add_button("Range: 0 - 100", range100, 120)
frame.add_button("Range: 0 - 1000", range1000, 120)
frame.add_label("")
frame.add_label("")
l1 = frame.add_label("Attempts left: " + str(attemptsTotal - attempts))
frame.add_label("")
frame.add_label("")
iGuess = frame.add_input("Enter your guess:", get_input, 100)
frame.add_label("")
  
frame.start()    
    
init()