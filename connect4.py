"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
"""
import random
import os


def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    valid_input = False
    while not valid_input:
        option = input(prompt)
        if option in valid_inputs:
            valid_input = True
            return int(option)
        else:
            print('Invalid input, please try again.')


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    row_num = 6
    col_num = 7
    new_board = []

    for row_index in range(row_num):
        row = [0] * col_num
        new_board.append(row)
    return new_board


def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    board_str = ""

    header = "========== Connect4 ========="
    players = "Player 1: X       Player 2: O"
    margin = ""
    col_numbers = "  1   2   3   4   5   6   7"
    border_horizontal = " --- --- --- --- --- --- ---"
    # board_str += (header + "\n" + border_top + "\n" + border_horizontal)
    board_str += "\n".join([header, players, margin, col_numbers, border_horizontal])

    for row in board:
        board_str += "\n|"
        for row_item in row:
            if row_item == 0:  # if empty cell
                display_token = " "
            elif row_item == 1:  # display player1's token
                display_token = "X"
            elif row_item == 2:  # display player2's token
                display_token = "O"
            board_str += f" {display_token} |"
        board_str += ("\n" + border_horizontal)
    footer = "============================="
    board_str += ("\n" + footer)
    print(board_str)


def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player who is dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    row_index_to_check = 5  # start checking from bottom-most row, check bottom-up
    col_index_to_check = column - 1
    while row_index_to_check >= 0:
        slot_to_check = board[row_index_to_check][col_index_to_check]
        if slot_to_check == 0:
            board[row_index_to_check][col_index_to_check] = player
            return True
        row_index_to_check -= 1
    return False


def execute_player_turn(player, board):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    drop_successful = False

    while not drop_successful:
        validated_col_option = validate_input(f'Player {player}, please enter the column you would like to drop your piece into: ', ['1', '2', '3', '4', '5', '6', '7'])
        drop_successful = drop_piece(board, player, validated_col_option)
        if drop_successful:
            return validated_col_option
        print('That column is full, please try again.')


def end_of_game(board):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # board = [
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0, 0, 0],
    #     [1, 2, 2, 2, 2, 0, 0]
    # ]
    zero_arr = []
    one_arr = []
    two_arr = []
    three_arr = []
    four_arr = []
    five_arr = []
    six_arr = []
    seven_arr = []
    index_vertical = 0
    num = 0

    while num < len(board):
        # print(len(board))
        i = board[num]
        index_in_i = 0

        # li = []
        while index_in_i < len(i):
            # print (len(i))
            if i[index_in_i] == 1:
                # li.append(index)
                if i[index_in_i] == i[index_in_i + 1] == i[index_in_i + 2] == i[index_in_i + 3]:
                    print(1)
                # li.clear()
            elif i[index_in_i] == 2:
                # li.append(index)
                if i[index_in_i] == i[index_in_i + 1] == i[index_in_i + 2] == i[index_in_i + 3]:
                    print(2)

                # li.clear()

            index_in_i += 1
            # print(index_in_i)

        num = num + 1
        print(num)
        # if index == 0 and len(i)> index_vertical:
        #     zero_arr.append(i[index])

        # for index_vertical in board:
        #
        #     index_vertical = 0
        #     if index_vertical == 0:
        #         zero_arr.append(i[index_vertical])
        #
        #     elif index_vertical == 1:
        #         one_arr.append((i[index_vertical]))
        #
        #     elif index_vertical == 2:
        #         two_arr.append(i[index_vertical])

        # for one in board:
        #     one = 1
        #     one_arr.append((i[one]))
        #
        # for two in board:
    raise NotImplementedError


def local_2_player_game():
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    # Implement your solution below
    raise NotImplementedError


def main():
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """
    # Implement your solution below
    raise NotImplementedError


def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    raise NotImplementedError


def cpu_player_medium(board, player):
    """
    Executes a move for the CPU on medium difficulty.
    It first checks for an immediate win and plays that move if possible.
    If no immediate win is possible, it checks for an immediate win
    for the opponent and blocks that move. If neither of these are
    possible, it plays a random move.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    raise NotImplementedError


def cpu_player_hard(board, player):
    """
    Executes a move for the CPU on hard difficulty.
    This function creates a copy of the board to simulate moves.
    <Insert player strategy here>

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    raise NotImplementedError


def game_against_cpu():
    """
    Runs a game of Connect 4 against the computer.

    :return: None
    """
    # Implement your solution below
    raise NotImplementedError


if __name__ == "__main__":
    main()
