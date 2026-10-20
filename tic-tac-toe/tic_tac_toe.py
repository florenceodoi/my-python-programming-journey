from random import randrange


def display_board(board):
    print("+-------+-------+-------+")

    for row in board:
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(
            row[0], row[1], row[2]
        ))
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))

            if move < 1 or move > 9:
                print("Please enter a number from 1 to 9.")
                continue

            row = (move - 1) // 3
            column = (move - 1) % 3

            if board[row][column] in ["X", "O"]:
                print("That square is already occupied.")
                continue

            board[row][column] = "O"
            break

        except ValueError:
            print("Please enter a valid integer.")


def make_list_of_free_fields(board):
    free_fields = []

    for row in range(3):
        for column in range(3):
            if board[row][column] not in ["X", "O"]:
                free_fields.append((row, column))

    return free_fields


def victory_for(board, sign):
    # Check rows
    for row in range(3):
        if (
            board[row][0] == sign
            and board[row][1] == sign
            and board[row][2] == sign
        ):
            return True

    # Check columns
    for column in range(3):
        if (
            board[0][column] == sign
            and board[1][column] == sign
            and board[2][column] == sign
        ):
            return True

    # Check first diagonal
    if (
        board[0][0] == sign
        and board[1][1] == sign
        and board[2][2] == sign
    ):
        return True

    # Check second diagonal
    if (
        board[0][2] == sign
        and board[1][1] == sign
        and board[2][0] == sign
    ):
        return True

    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)

    if len(free_fields) > 0:
        move = randrange(len(free_fields))
        row, column = free_fields[move]
        board[row][column] = "X"


# Create the game board
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Computer makes the first move
board[1][1] = "X"


# Main game loop
while True:
    display_board(board)

    # User's move
    enter_move(board)

    # Check whether the user won
    if victory_for(board, "O"):
        display_board(board)
        print("You won!")
        break

    # Check for a tie
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Tie!")
        break

    # Computer's move
    draw_move(board)

    # Check whether the computer won
    if victory_for(board, "X"):
        display_board(board)
        print("Computer won!")
        break

    # Check for a tie again
    if len(make_list_of_free_fields(board)) == 0:
        display_board(board)
        print("Tie!")
        break
