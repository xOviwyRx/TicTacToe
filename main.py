from random import randrange


def get_tuple_pos(pos):
    return (pos - 1) // 3, (pos - 1) % 3


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    delimiter1 = '+-------+-------+-------+'
    delimiter2 = '|       |       |       |'
    print(delimiter1)
    for i in range(3):
        print(delimiter2)
        for j in range(3):
            print('|  ', board[i][j], '  ', end='')
        print('|')
        print(delimiter2)
        print(delimiter1)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user_pos = int(input('Input move position '))
            if user_pos < 1 or user_pos > 9:
                print('Number must be greater than 0 and less than 10')
            else:
                break
        except ValueError:
            print('Enter a number')
    free_fields = make_list_of_free_fields(board)
    tuple_pos = get_tuple_pos(user_pos)
    if tuple_pos in free_fields:
        board[tuple_pos[0]][tuple_pos[1]] = 'O'


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] != 'X' and board[i][j] != 'O']


def horizontal_vertical_win(board, sign):
    for i in range(3):
        count_h = 0
        count_v = 0
        for j in range(3):
            if board[i][j] == sign:
                count_h += 1
            if board[j][i] == sign:
                count_v += 1
        if count_h == 3 or count_v == 3:
            break

    if count_v == 3 or count_h == 3:
        return True
    return False


def diagonal_win(board, sign):
    count = 0
    if (board[0][0] == sign and
            board[1][1] == sign and
            board[2][2] == sign):
        return True
    if (board[0][2] == sign and
            board[1][1] == sign and
            board[2][0] == sign):
        return True
    return False


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if horizontal_vertical_win(board, sign) or diagonal_win(board, sign):
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        pc_pos = randrange(9)
        tuple_pos = get_tuple_pos(pc_pos)
        free_fields = make_list_of_free_fields(board)
        if tuple_pos in free_fields:
            board[tuple_pos[0]][tuple_pos[1]] = 'X'
            break


board = [[1, 2, 3],
         [4, 'X', 6],
         [7, 8, 9]]

count_free_fields = 8
display_board(board)
while count_free_fields:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print('You win')
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print('PC win')
        break
    count_free_fields -= 2

if not count_free_fields:
    print("It's tie")

