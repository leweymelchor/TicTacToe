#Tic-Tac-Toe

def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()

def game_over(board, current_player):

    print_board(board)
    print(current_player, "has won")
    exit()


def is_row_winner(board, row_number):
    if board[0] == board[1] and board[1] == board[2]:
        return True
    elif board[3] == board[4] and board[4] == board[5]:
        return True
    elif board[6] == board[7] and board[7] == board[8]:
        return True


def is_column_winner(board, column_number):
    if board[0] == board[3] and board[3] == board[6]:
        return True
    if board[1] == board[4] and board[4] == board[7]:
        return True
    if board[2] == board[5] and board[5] == board[8]:
        return True
    else:
        return False


def is_diagnal_winner(board, diagnal_number):
    if board[0] == board[4] and board[4] == board[8]:
        return True
    if board[2] == board[4] and board[4] == board[6]:
        return True


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if is_row_winner(board, 1):
        game_over(board, current_player)
    elif is_row_winner(board, 2):
        game_over(board, current_player)
    elif is_row_winner(board, 3):
        game_over(board, current_player)
    elif is_column_winner(board, 1):
        game_over(board, current_player)
    elif is_column_winner(board, 2):
        game_over(board, current_player)
    elif is_column_winner(board, 3):
        game_over(board, current_player)
    elif is_diagnal_winner(board, 1):
        game_over(board, current_player)
    elif is_diagnal_winner(board, 2):
        game_over(board, current_player)

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")
