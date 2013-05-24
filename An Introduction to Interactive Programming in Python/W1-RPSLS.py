'''
Created on Apr 20, 2013
@author: Nenad

Rock-paper-scissors-lizard-Spock template
The key idea of this program is to equate the strings "rock", "paper", "scissors", "lizard", "Spock" to numbers as follows:
0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors

http://www.codeskulptor.org/#user10_mAqrqaJjwJ_1.py
'''
from random import randrange

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "invalid"

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1

def rpsls(name): 
    player_number = name_to_number(name)
    comp_number = randrange(0,5)
    comp_name = number_to_name(comp_number)
    print ('Player chooses', name)
    print ('Computer chooses', comp_name)
    if 1<=(player_number - comp_number) % 5<=2:
        print ('Player wins!')
    elif (player_number - comp_number) % 5 >2:
        print ('Computer wins!')
    else:
        print ('Player and computer tie!')
    print ()
    
# print results
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
