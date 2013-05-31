'''

print "Hello World"


if True or False and "Hello World":
    print "Woah"
    if True:
        pass
elif True:
    pass
else:
    pass


for i in range(len([1, 2])):
    print i


for item in ["hello", "world"]:
    print item


while False:
    pass


i = 9


result = raw_input("Find ")

if int(result) == 1:
    print 'correct'

# < > >= <= !=
'''


def clear():
    print '\n' * 15


# Quiz Code

'''print "Welcome to the Great Quiz!!"
print "Prepare to be amazed and test your Knowledge!!"
clear()'''


# Number Guesser Code

def guess():   
    print 'This is the Random Number Guesser!'
    print 'You will give me two numbers and then you will'
    print 'Guess a number between those numbers.'
    print 'Please enter 2 numbers.'

    num1 = raw_input('Number 1: ')
    num2 = raw_input('Number 2: ')

    import random
    for x in range(1):
        ran_num = random.randint(num1, num2)  # Gets a random integar between the numbers  
        answer = raw_input('Please guess the number: ')
        if answer == ran_num:
            print 'Correct'
        elif answer > ran_num:
            answer = raw_input('Sorry that is a little high, Try Again: ')
        elif answer < ran_num:
            answer = raw_input('Sorry that is a little low, Try Again: ')
        else:
            pass


def guess_game():
    guess()

    play = raw_input('Would you like to play again (y/n): ')

    if play == 'y':
        guess()
    elif play == 'n':
        pass
    else:
        pass

# Tic Tac Toe Code


def tic_start():

    print "Welcome to Tic Tac Toe!"
    print "Player 1 will be X and Player 2 will be O."
    print 'To choose a space enter the matching number.'
    print 'Here is a legend:'
    print '   1   2   3   '
    print '   4   5   6   '
    print '   7   8   9   '
    print " "


def tic_game():

    win = 0
    if win == 0:
        for counter in range(len(1, 9)):
            move = raw_input('Current Player: ')
            


def tic_play():
    tic_start()
    print 'If at anytime you wish to see the legend, just type legend.'
    ready = raw_input("Ready(y/n): ")
    if ready == 'y':
        tic_game()
    elif ready == 'n':
        print "Alright I'll reapeat myself then."
        clear()
        tic_start()
    elif ready == 'legend':
        print '   1   2   3   '
        print '   4   5   6   '
        print '   7   8   9   '
        print ' '
    else:
        pass
