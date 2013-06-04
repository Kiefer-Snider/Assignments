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


def quiz():
    fin = open('Quiz.txt', 'r')
    line_list = fin.readlines()
    fin.close()

    quiz_list = []
    cor = 0
    in_cor = 0
    for k, line in enumerate(line_list):
        complete = False
        line1 = line.strip()

        if k % 2 == 0:
            question = line1
        if k % 2 == 1:
            answer = line1
            complete = True
        if complete is True:
            play_ans = raw_input(question)
            if play_ans == answer:
                print 'Correct'
                cor += 1
                pass
            else:
                print 'Incorrect'
                in_cor += 1
                pass
    return cor
    return in_cor


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
            break


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


def tic_win(player):
    for c in range(0, 3):  # Rows and Columns Counter

        # Horizontal Check
        if board[c][0] == player and board[c][1] == player and board[c][2] == player:
            print "*********\n\n%s wins\n\n*********" % player
            playerwin = True
            return playerwin
      
        # Vertical Check
        elif board[0][c] == player and board[1][c] == player and board[2][c] == player:
            print "*********\n\n%s wins\n\n*********" % player
            playerwin = True
            return playerwin
        
        # Diagonal Check (left to right)
        elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
            print "*********\n\n%s wins\n\n*********" % player
            playerwin = True
            return playerwin
        
        # Diagonal Check (right to left)
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
            print "*********\n\n%s wins\n\n*********" % player
            playerwin = True
            return playerwin
        else:
            playerwin = False
            return playerwin


def tic_turn(player):  # The Turn
    print "%s's turn" % player
    turn = 1
    while(turn):
        print "Select column [1-3]: ",
        col = int(raw_input()) - 1
        print "Select row [1-3]: ",
        row = int(raw_input()) - 1
        if board[row][col] == 'X' or board[row][col] == 'O':
            print "Already Taken!"
        else:
            board[row][col] = player
            turn = 0


def print_board():
    print board[0]
    print board[1]
    print board[2]


# The Board
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
player1 = 'X'
player2 = 'O'
win = False


def tic_game():
    turns = 0

    # The Actual Game
    print_board()
    while win is False:
        tic_turn(player1)
        turns += 1
        print_board()
        if tic_win(player1) is True:
            break
            if turns == 9:
                print 'This game has come to a draw!'
            break

        tic_turn(player2)
        turns += 1
        print_board()
        tic_win(player2)
        if tic_win(player2) is True:
            break

