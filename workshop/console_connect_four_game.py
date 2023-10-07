# import os
#
# ROWS = 6
# COLS = 7
#
#
# class FullColumnError(Exception):
#     pass
#
#
# def print_matrix(given_matrix):
#     for row in given_matrix:
#         print(row)
#
#
# def is_valid_column_choice(index):
#     if 0 <= index < COLS:
#         return True
#     return False
#
#
# def place_player_number(column_index, given_matrix, player_number):
#     for row_index in range(ROWS - 1, -1, -1):
#         if given_matrix[row_index][column_index] == 0:
#             matrix[row_index][column_index] = player_number
#             return row_index, column_index
#     else:
#         raise FullColumnError
#
#
# def winning_move(given_matrix, current_player):
#     # Check horizontal locations for win
#     for c in range(COLS - 3):
#         for r in range(ROWS):
#             if given_matrix[r][c] == current_player and \
#                     given_matrix[r][c + 1] == current_player and \
#                     given_matrix[r][c + 2] == current_player and \
#                     given_matrix[r][c + 3] == current_player:
#                 return True
#
#     # Check vertical locations for win
#     for c in range(COLS):
#         for r in range(ROWS - 3):
#             if given_matrix[r][c] == current_player and \
#                     given_matrix[r + 1][c] == current_player and \
#                     given_matrix[r + 2][c] == current_player and \
#                     given_matrix[r + 3][c] == current_player:
#                 return True
#
#     # Check positively sloped diagonals
#     for c in range(COLS - 3):
#         for r in range(ROWS - 3):
#             if given_matrix[r][c] == current_player and \
#                     given_matrix[r + 1][c + 1] == current_player and \
#                     given_matrix[r + 2][c + 2] == current_player and \
#                     given_matrix[r + 3][c + 3] == current_player:
#                 return True
#
#     # Check negatively sloped diagonals
#     for c in range(COLS - 3):
#         for r in range(3, ROWS):
#             if given_matrix[r][c] == current_player and \
#                     given_matrix[r - 1][c + 1] == current_player and \
#                     given_matrix[r - 2][c + 2] == current_player and \
#                     given_matrix[r - 3][c + 3] == current_player:
#                 return True
#
#
# def call_winnings_archive():
#     path = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(path, "winners.txt")
#     file = open(file_path, "r")
#
#     winnings_history = ''
#     for line in file:
#         winnings_history += f"{line}\n"
#     file.close()
#
#     return winnings_history
#
#
# matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
# player = 1
# tour_played = 0
#
# while True:
#     try:
#         selected_column_number = int(input(f"Player {player}, please choose a column: "))
#         selected_column_index = selected_column_number - 1
#         if not is_valid_column_choice(selected_column_index):
#             raise ValueError
#
#         current_row, current_col = place_player_number(selected_column_index, matrix, player)
#         print_matrix(matrix)
#     except ValueError:
#         print(f"Player {player}, please select number between 1 and {COLS}.")
#         continue
#     except FullColumnError:
#         print(f"Player {player}, this column is full, please select another one.")
#         continue
#
#     if winning_move(matrix, player):
#         print(f"The winner is player {player}!")
#         tour_played += 1
#
#         with open("winners.txt", "a") as file:
#             file.write(f"The winner of the tour {tour_played} is player {player}!\n")
#
#         play_again = input("Do you want to play again?\nYes or No: ")
#         give_archive = input("Do you want to check the current archive of game/s played?\nYes or No: ")
#
#         if give_archive.lower() == "yes":
#             print(call_winnings_archive())
#         if play_again.lower() == "yes":
#             matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
#         else:
#             with open("winners.txt", "w") as file:
#                 pass
#             break  # TO BE DEVELOPED
#
#     player += 1
#     player = 2 if player % 2 == 0 else 1

# USING TKINTER -----------------------------------------------------------------------------------------

import os
import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext

ROWS = 6
COLS = 7


class YesNoError(Exception):
    pass


class FullColumnError(Exception):
    pass


def print_matrix(given_matrix):
    for row in given_matrix:
        print(row)


def is_valid_column_choice(index):
    if 0 <= index < COLS:
        return True
    return False


def place_player_number(column_index, given_matrix, player_number):
    for row_index in range(ROWS - 1, -1, -1):
        if given_matrix[row_index][column_index] == 0:
            matrix[row_index][column_index] = player_number
            return row_index, column_index
    else:
        raise FullColumnError


def winning_move(given_matrix, current_player):
    # Check horizontal locations for win
    for c in range(COLS - 3):
        for r in range(ROWS):
            if given_matrix[r][c] == current_player and \
                    given_matrix[r][c + 1] == current_player and \
                    given_matrix[r][c + 2] == current_player and \
                    given_matrix[r][c + 3] == current_player:
                return True

    # Check vertical locations for win
    for c in range(COLS):
        for r in range(ROWS - 3):
            if given_matrix[r][c] == current_player and \
                    given_matrix[r + 1][c] == current_player and \
                    given_matrix[r + 2][c] == current_player and \
                    given_matrix[r + 3][c] == current_player:
                return True

    # Check positively sloped diagonals
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if given_matrix[r][c] == current_player and \
                    given_matrix[r + 1][c + 1] == current_player and \
                    given_matrix[r + 2][c + 2] == current_player and \
                    given_matrix[r + 3][c + 3] == current_player:
                return True

    # Check negatively sloped diagonals
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if given_matrix[r][c] == current_player and \
                    given_matrix[r - 1][c + 1] == current_player and \
                    given_matrix[r - 2][c + 2] == current_player and \
                    given_matrix[r - 3][c + 3] == current_player:
                return True


def call_winnings_archive():
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path, "winners.txt")
    file = open(file_path, "r")

    winnings_history = ''
    for line in file:
        winnings_history += f"{line}\n"
    file.close()

    return winnings_history


def reset_game():
    global matrix
    global player
    matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    player = 1
    update_board()


def update_board():
    for i in range(COLS):
        for j in range(ROWS):
            cell_value = matrix[j][i]
            if cell_value == 0:
                buttons[i][j].configure(bg='white')
            elif cell_value == 1:
                buttons[i][j].configure(bg='blue')
            elif cell_value == 2:
                buttons[i][j].configure(bg='yellow')


def yes_or_no(answer):
    if answer.lower() == 'yes' or answer.lower() == 'no':
        return True
    return False


def on_column_click(column):
    global player
    global tour_played

    try:
        selected_column_index = column
        if not is_valid_column_choice(selected_column_index):
            raise ValueError

        current_row, current_col = place_player_number(selected_column_index, matrix, player)
        print_matrix(matrix)
    except ValueError:
        print(f"Player {player}, please select a number between 1 and {COLS}.")
        return
    except FullColumnError:
        print(f"Player {player}, this column is full, please select another one.")
        return

    if winning_move(matrix, player):
        print(f"The winner is player {player}!")
        tour_played += 1

        with open("winners.txt", "a") as file:
            file.write(f"The winner of tour {tour_played} is player {player}!\n")

        end_flag = False
        while not end_flag:
            try:
                play_again = simpledialog.askstring("Play Again", "Do you want to play again? (Yes/No):")
                if not yes_or_no(play_again):
                    raise YesNoError

                end_flag = True
                if play_again and play_again.lower() == "yes":

                    end_flag_2 = False
                    while not end_flag_2:
                        try:
                            give_archive = simpledialog.askstring("Show Archive",
                                                        "Do you want to check the archive of games played? (Yes/No):")
                            if not yes_or_no(give_archive):
                                raise YesNoError

                            end_flag_2 = True
                            if give_archive and give_archive.lower() == "yes":
                                archive_text.delete(1.0, tk.END)
                            archive_text.insert(tk.END, call_winnings_archive())
                            reset_game()
                        except YesNoError:
                            print(f"Player {player}, please choose yes or no.")
                            continue
                else:
                    with open("winners.txt", "w") as file:
                        pass
                    root.destroy()
                    exit()
            except YesNoError:
                print(f"Player {player}, please choose yes or no.")
                continue

    player += 1
    player = 2 if player % 2 == 0 else 1
    update_board()


matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
player = 1
tour_played = 0

root = tk.Tk()
root.title("Console Connect Four - Game")
root.iconbitmap('game_icon.ico')
buttons = []
for i in range(COLS):
    button_row = []
    for j in range(ROWS):
        button = tk.Button(root, text='Connect Four', width=20, height=10, command=lambda i=i: on_column_click(i))
        button.grid(row=j, column=i)
        button_row.append(button)
    buttons.append(button_row)

# Create a scrolled text widget for displaying the archive
archive_text = scrolledtext.ScrolledText(root, width=30, height=10)
archive_text.grid(row=0, column=COLS)

update_board()
root.mainloop()

# USING TKINTER -----------------------------------------------------------------------------------------
