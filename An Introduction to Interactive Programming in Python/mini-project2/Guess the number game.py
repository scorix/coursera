# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code
def init(difficulty = 100):
    if difficulty == 100:
        range100()
    else:
        range1000()

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global answer, chances, difficulty
    print "Guess a number from 0 to 99. You have 7 chances."
    answer = random.randrange(0, 100)
    chances, difficulty = 7, 100
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global answer, chances, difficulty
    print "Guess a number from 0 to 999. You have 10 chances."
    answer = random.randrange(0, 1000)
    chances, difficulty = 10, 1000
    
def get_input(guess):
    # main game logic goes here	
    global answer, chances, difficulty
    print "Your guess is: " + guess
    if int(guess) > answer:
        print "Higher. Remaining chances: " + str(chances)
    elif int(guess) < answer:
        print "Lower. Remaining chances: " + str(chances)
    else:
        print "Correct! Let's play more.\n"
        init()
    chances -= 1
    if chances == 0:
        print "What a pity! Try Again!\n"
        init(difficulty)
     
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Guess a number here", get_input, 200)
init()

# start frame
frame.start

# always remember to check your completed program against the grading rubric
