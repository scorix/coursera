# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def number_to_name(number):
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        print "unkown number."
        return ""

    
def name_to_number(name):
    if(name == "rock"):
        return 0
    elif(name == "Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name == "lizard"):
        return 3
    elif(name == "scissors"):
        return 4
    else:
        print "unkown name."
        return -1


def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange() modulo five
    comp_number = random.randrange(10) % 5
    
    # compute difference of player_number and comp_number
    diff = player_number - comp_number    
    
    # use if/elif/else to determine winner
    if(diff == 2 or diff == 1 or diff == -3 or diff == -4):
        winner = "Player"
    else:
        winner = "Computer"
    
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    
    # print results
    print "Player choose %s" % name
    print "Computer choose %s" % comp_name
    if(diff == 0):
        print "Player and computer tie!\n" 
    else:
        print "%s wins!\n" % winner
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

