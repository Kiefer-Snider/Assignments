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


# Number Guesser
def guess():    
    print 'This is the Random Number Guesser!'
    print 'You will give me two numbers and then you will'
    print 'Guess a number between those numbers.'
    print 'Please enter 2 numbers.'

    num1 = raw_input('Number 1: ')
    num2 = raw_input('Number 2: ')

    import random
    for x in range(1):
        ran_num = random.randint(num1, num2)   
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
