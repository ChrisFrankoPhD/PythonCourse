import random

moves = ['rock', 'paper', 'scissors']
valid_moves = ['rock', 'paper', 'scissors', 'r', 'p', 's']
valid_new_game = ['yes', 'no', 'y', 'n']
comp_score = 0
user_score = 0


def is_move_valid(move):
    return move in valid_moves

def gen_result(score):
    message = ''
    global comp_score
    global user_score
    if score == -1:
        message += 'Point Computer!'
        comp_score += 1
    elif score == 1:
        message += 'Point User!'
        user_score += 1
    else:
        message += 'Tie, Try Again!'
    return message

def new_game():
    global comp_score
    global user_score
    comp_score = 0
    user_score = 0

    while (user_score < 3 and comp_score < 3):
        # pick random computer move from move list
        comp_move = random.choice(moves)

        # prompt user for their move
        user_move = input('rock, paper, scissors? ').lower().strip()
        if user_move == "quit" or user_move == "q":
            print('goodbye')
            return
        
        # prompt user to enter a valid move until they do
        while not is_move_valid(user_move):
            user_move = input('invalid move: please choose rock, paper, or scissors: ').lower().strip()
            if user_move == "quit" or user_move == "q":
                print('goodbye')
                return
        
        # clean up the move into 1 of 3 bins
        if user_move == 'r':
            user_move = 'rock'
        elif user_move == 'p':
            user_move = 'paper'
        elif user_move == 's':
            user_move = 'scissors'

        print(f'---------FIGHT!----------\n{comp_move.upper()} vs {user_move.upper()}\n')
        score = None
        if user_move == comp_move:
            score = 0
        if comp_move == 'rock' and user_move == 'paper':
            score = 1
        elif comp_move == 'paper' and user_move == 'scissors':
            score = 1
        elif comp_move == 'scissors' and user_move == 'rock':
            score = 1
        else:
            score = -1
        # if comp_move == 'rock':
        #     if user_move == 'paper':
        #         score = 1
        #     elif user_move == 'scissors':
        #         score = -1

        # if comp_move == 'paper':
        #     if user_move == 'scissors':
        #         score = 1
        #     elif user_move == 'rock':
        #         score = -1

        # if comp_move == 'scissors':
        #     if user_move == 'rock':
        #         score = 1
        #     elif user_move == 'paper':
        #         score = -1

        print (gen_result(score), '\n')
        print (f'SCORE:\nYOU:{user_score}, COMP:{comp_score}\n')

    if comp_score == 3:
        message = 'You Lost Fucko! :('
    if user_score == 3:
        message = 'Congratulations, you were victorious!'
    print(f'{message} by a score of {user_score} to {comp_score}')

    is_new_game = input('Would you like to play again? (Y / N) ').lower().strip()
    if is_new_game == "quit" or is_new_game == "q":
            print('goodbye')
            return
    
    while not is_new_game in valid_new_game:
        is_new_game = input('Invalid input, Would you like to play again? (Y / N) ').lower()
        if is_new_game == "quit" or is_new_game == "q":
            print('goodbye')
            return
        
    if is_new_game == 'y' or is_new_game == 'yes':
        new_game()
    elif is_new_game == 'n' or is_new_game == 'no':
        print('goodbye')
        return
    
new_game()