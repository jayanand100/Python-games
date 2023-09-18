import random
board_index = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_board():
    for row in [board_index[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')


def x_player():
    print("Player X")
    try:
        x_place = int(input("Put an X at: "))
    except ValueError:
        x_place = int(input("Put an X at !!!: "))

    if board_index[x_place] not in ['X', 'O']:
        board_index[x_place] = 'X'
    else:
        print("Choose some other location!!!")
        return x_player()

    print_board()


def o_player():
    print("Player O")
    try:
        o_place = int(input("Put an O at: "))
    except ValueError:
        o_place = int(input("Put an O at !!!: "))

    if board_index[o_place] not in ['X', 'O']:
        board_index[o_place] = 'O'
    else:
        print("Choose some other location!!!")
        return o_player()

    print_board()


def IntelligentPlayer():
    best_score = -1000
    best_move = 0
    for i in range(0,9):
        if(board_index[i]==' '):
            board_index[i] = 'O'
            score = MiniMax(board_index,0,False)
            board_index[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    board_index[best_move] = 'O'
    print_board()

def MiniMax(board_index, depth, isMaximizing):

    if check_winner('O'):
        return 100
    if check_winner('X'):
        return -100
    if check_tie():
        return 0
    if isMaximizing:
        best_score = -1000
        for i in range(0, 9):
            if (board_index[i] == ' '):
                board_index[i] = 'O'
                score = MiniMax(board_index, 0, True)
                board_index[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 800
        for i in range(0, 9):
            if (board_index[i] == ' '):
                board_index[i] = 'O'
                score = MiniMax(board_index, 0, False)
                board_index[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score


def ai_player():
    o_place = random.randint(0, 9)

    if board_index[o_place] not in ['X', 'O']:
        board_index[o_place] = 'O'
    else:
        return ai_player()
    print("player 'O' ended his turn...")
    print_board()

def check_winner(symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for combination in winning_combinations:
        if all(board_index[i] == symbol for i in combination):
            return True
    return False

def check_tie():
    for i in range(0,9):
        if board_index[i] != ' ':
            return True
    return False


#starts here.......

print_board()

while True:
    x_player()
    print(board_index)
    if check_winner('X'):
        print("Player X wins!")
        break

    IntelligentPlayer()
    print(board_index)
    if check_winner('O'):
        print("Player O wins!")
        break

    check_tie()


















