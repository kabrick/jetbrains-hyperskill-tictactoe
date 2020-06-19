def print_board():
    print("---------")

    for i in game_state:
        print("|", i[0], i[1], i[2], "|")

    print("---------")


def check_game_status():
    # check state of game
    is_game_won = False
    x_won = False
    o_won = False

    # check if game is won horizontally
    for row in game_state:
        if row.count(row[0]) == len(row) and row[0] != " ":
            is_game_won = True
            if row[0] == "O":
                o_won = True
            elif row[0] == "X":
                x_won = True
            break

    if not is_game_won:
        # won vertically
        for i in range(len(game_state)):
            column = []

            for row in game_state:
                column.append(row[i])

            if column.count(column[0]) == len(column) and column[0] != " ":
                is_game_won = True
                if column[0] == "O":
                    o_won = True
                elif column[0] == "X":
                    x_won = True
                break

    if not is_game_won:
        # won diagonally
        track_diagonal = []

        for row_idx in range(len(game_state)):
            for col_idx in reversed(range(len(game_state))):
                if (row_idx + col_idx) == (len(game_state) - 1):
                    track_diagonal.append(game_state[row_idx][col_idx])

        if track_diagonal.count(track_diagonal[0]) == len(track_diagonal) and track_diagonal[0] != " ":
            is_game_won = True
            if track_diagonal[0] == "O":
                o_won = True
            elif track_diagonal[0] == "X":
                x_won = True

        # reset our tracker variable
        track_diagonal = []

        for idx in range(len(game_state)):
            track_diagonal.append(game_state[idx][idx])

        if track_diagonal.count(track_diagonal[0]) == len(track_diagonal) and track_diagonal[0] != " ":
            is_game_won = True
            if track_diagonal[0] == "O":
                o_won = True
            elif track_diagonal[0] == "X":
                x_won = True

    if not is_game_won and " " not in cells_string:
        # "Draw" - when no side has a three in a row and the field has no empty cells;
        return "Draw"
    elif x_won:
        # "X wins" - when the field has three X in a row;
        return "X wins"
    elif o_won:
        # "O wins" - when the field has three O in a row;
        return "O wins"
    else:
        return "continue"


# write your code here
game_state = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

cells_string = ""

print_board()

current_player = "X"

while True:
    user_input = input("Enter the coordinates: ")
    coordinates = user_input.split(" ")
    x_coord = 1
    y_coord = 1

    try:
        x_coord = int(coordinates[0])
        y_coord = int(coordinates[1])
    except ValueError:
        print("You should enter numbers!")
        continue

    if x_coord > 3 or y_coord > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    # convert from coordinates to cartesian
    cartesian_i = 3 - y_coord
    cartesian_j = x_coord - 1

    # check if the cell is occupied
    if game_state[cartesian_i][cartesian_j] != " ":
        print("This cell is occupied! Choose another one!")
        continue

    # update the selected cell
    game_state[cartesian_i][cartesian_j] = current_player

    # edit the cells_string
    cells_string = "".join(["".join(row) for row in game_state])

    # change the player
    current_player = "O" if current_player == "X" else "X"

    # check the status of the game
    current_check_game_status = check_game_status()

    print_board()

    if current_check_game_status != "continue":
        print(current_check_game_status)
        break
