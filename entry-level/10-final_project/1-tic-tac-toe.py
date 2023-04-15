from random import randrange

# for i in range(10):
#     print(randrange(8))

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print('+-------+-------+-------+')
        print('|       |       |       |')
        print('|   {}   |   {}   |   {}   |'.format(*row))
        print('|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.

    move = int(input('Enter your move: ')) - 1
    row = move // 3
    col = move % 3
    free_fields = make_list_of_free_fields(board)
    if (row, col) not in free_fields:
        print('This is not a free field')
        enter_move(board)
    else:
        board[row][col] = 'O'

def make_list_of_free_fields(board: list):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []

    for row in range(3):
        for col in range(3):
            if type(board[row][col]) == int:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    turned_board = [list(row) for row in zip(*board)]
    diagonal1 = []
    diagonal2 = []

    for row in range(3):
        if (board[row].count(sign) == 3):
            return True
        if (turned_board[row].count(sign) == 3):
            return True
        diagonal1.append(board[row][row])
        diagonal2.append(board[row][2 - row])

    if diagonal1.count(sign) == 3 or diagonal2.count(sign) == 3:
        return True

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    rand_position = randrange(len(free_fields))
    choosed_position = free_fields[rand_position]
    row = choosed_position[0]
    col = choosed_position[1]
    board[row][col] = 'X'

def game_loop():
    board = [[x + y * 3 for x in range(1, 4)] for y in range(3)]
    whose_turn = 'O'
    next_turn = 'X'
    board[1][1] = 'X'
    winner = None

    while winner == None and len(make_list_of_free_fields(board)):
        display_board(board)
        if whose_turn == 'X':
            draw_move(board)
        else:
            enter_move(board)
        winner = victory_for(board, whose_turn)
        whose_turn, next_turn = next_turn, whose_turn

    display_board(board)
    if winner != None:
        if whose_turn == 'X':
            print('You won!')
        else:
            print('I won!')
    else:
        print('It is a draw, good game')

game_loop()
