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

def quiz():
    fin = open('Quiz.txt', 'r')  # Opens the Quiz txt file and imports

    while True:

        question = fin.readline()
        answer = fin.readline()
        if not question:
            break
        play_ans = raw_input(question)
        if play_ans == answer:
            print 'Correct'
        else:
            print 'Incorrect'

    fin.close()


# Number Guesser Code

def guess():
    print 'This is the Random Number Guesser!'
    print 'You will give me two numbers and then you will'
    print 'Guess a number between those numbers.'
    print 'Please enter 2 numbers.'

    num1 = int(raw_input('Number 1: '))
    num2 = int(raw_input('Number 2: '))

    import random
    for x in range(1):
        ran_num = random.randint(num1, num2)  # Gets a random integar between the numbers  
        answer = int(raw_input('Please guess the number: '))
        if answer == ran_num:
            print 'Correct'
        elif answer > ran_num:
            answer = raw_input('Sorry that is a little high, Try Again: ')
        elif answer < ran_num:
            answer = raw_input('Sorry that is a little low, Try Again: ')
        


# Tic Tac Toe Code


def tic_win(player):
    for c in range(0, 3):  # Rows and Columns Counter

        # Horizontal Check
        if board[c][0] == player and board[c][1] == player and board[c][2] == player:
            playerwin = True
              
        # Vertical Check
        elif board[0][c] == player and board[1][c] == player and board[2][c] == player:
            playerwin = True
            
        # Diagonal Check (left to right)
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            playerwin = True
                   
        # Diagonal Check (right to left)
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            playerwin = True

    print "*********\n\n%s wins\n\n*********" % player
    return playerwin
            

def tic_turn(player):  # The Turn
    print "%s's turn" % player
    turn = 1
    while(turn):
        col = int(raw_input("Select column [1-3]: ")) - 1
        row = int(raw_input("Select row [1-3]: ")) - 1
        if board[row][col] == 'X' or board[row][col] == 'O':
            print "Already Taken!"
        else:
            board[row][col] = player
            turn = 0


def print_board():
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    for c in range(0, 3):
        print ' '.join(board[c])



# The Board


def tic_game():
    turns = 0
    win = False
    player1 = 'X'
    player2 = 'O'

    # The Actual Game
    print_board()
    while not win:
        tic_turn(player1)
        turns += 1
        print_board()
        if tic_win(player1):
            pass  
        elif turns == 9:
            print 'This game has come to a draw!'
            

        tic_turn(player2)
        turns += 1
        print_board()
        tic_win(player2)
        if tic_win(player2):
            break

# Menu Code
i = True
if i is True:
    print 'Welcome to the Exciting Three-Game Menu!'
    print 'There are three games to choose from:'
    print '1. The Quiz on Canadian Provincial Capitals'
    print '2. The Two-Player Tic Tac Toe'
    print '3. The Random Number Guesser'
    print 'Please choose a game: '
    choice = int(raw_input())
   
    if choice == 1:
        clear()
        print "Welcome to the Quiz on Canadian Provincial Capitals."
        print "Prepare to be amazed and test your Knowledge!!"
        quiz()
               
    elif choice == 2:
        clear()
        print "Welcome to Tic Tac Toe."
        print 'I hope both players are ready.'
        tic_game()
        
    elif choice == 3:
        clear()
        guess()
        
    else:
        clear()
       
    again = raw_input("Would you like to play again(y/n)? ")

    if again == 'y':
        pass
    else:
        i = False
        
