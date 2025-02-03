import tkinter as tk
from tkinter import messagebox


class InvalidPositionNumber(Exception):
    pass


class PositionTaken(Exception):
    pass


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player1_name = ""
        self.player2_name = ""
        self.player1_symbol = ""
        self.player2_symbol = ""
        self.current_player_name = ""
        self.turns_count = 1
        self.matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.position_mapper = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        self.player_to_symbol = {}
        self.buttons = {}
        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack()

        tk.Label(self.welcome_frame, text="Player 1, enter your name:").grid(row=0, column=0)
        self.player1_entry = tk.Entry(self.welcome_frame)
        self.player1_entry.grid(row=0, column=1)

        tk.Label(self.welcome_frame, text="Player 2, enter your name:").grid(row=1, column=0)
        self.player2_entry = tk.Entry(self.welcome_frame)
        self.player2_entry.grid(row=1, column=1)

        tk.Label(self.welcome_frame, text="Player 1, select your symbol (X or O):").grid(row=2, column=0)
        self.symbol_entry = tk.Entry(self.welcome_frame)
        self.symbol_entry.grid(row=2, column=1)

        tk.Button(self.welcome_frame, text="Start Game", command=self.start_game).grid(row=3, column=0, columnspan=2)

    def start_game(self):
        self.player1_name = self.player1_entry.get()
        self.player2_name = self.player2_entry.get()
        symbol = self.symbol_entry.get().upper()

        if symbol not in ["X", "O"]:
            messagebox.showerror("Invalid Symbol", "Please select a valid symbol (X or O).")
            return

        self.player1_symbol = symbol
        self.player2_symbol = "O" if self.player1_symbol == "X" else "X"
        self.player_to_symbol = {
            self.player1_name: self.player1_symbol,
            self.player2_name: self.player2_symbol
        }
        self.current_player_name = self.player1_name

        self.welcome_frame.destroy()
        self.create_game_board()

    def create_game_board(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        for i in range(1, 10):
            row, col = self.position_mapper[i]
            button = tk.Button(self.game_frame, text=" ", font=('normal', 20), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=row, column=col)
            self.buttons[i] = button

    def on_button_click(self, position):
        try:
            if self.matrix[self.position_mapper[position][0]][self.position_mapper[position][1]] != ' ':
                raise PositionTaken
            self.update_board(position)
        except PositionTaken:
            messagebox.showerror("Position Taken", "Please select an empty position.")

    def update_board(self, position):
        row, col = self.position_mapper[position]
        player_symbol = self.player_to_symbol[self.current_player_name]
        self.matrix[row][col] = player_symbol
        self.buttons[position].config(text=player_symbol)

        if self.turns_count >= 5 and self.is_winner(player_symbol):
            messagebox.showinfo("Game Over", f"{self.current_player_name} is the winner!")
            self.reset_game()
            return

        self.turns_count += 1
        if self.turns_count == 10:
            messagebox.showinfo("Game Over", "No winner - game over")
            self.reset_game()
            return

        self.current_player_name = self.player2_name if self.turns_count % 2 == 0 else self.player1_name

    def is_winner(self, player_symbol):
        # Check rows
        for row in self.matrix:
            if all([el == player_symbol for el in row]):
                return True
        # Check columns
        for col_index in range(len(self.matrix)):
            if all([self.matrix[row_index][col_index] == player_symbol for row_index in range(len(self.matrix))]):
                return True
        # Check diagonals
        main_diagonal_winner = all([self.matrix[index][index] == player_symbol for index in range(len(self.matrix))])
        diagonal_winner = all(
            [self.matrix[(len(self.matrix)) - 1 - col_index][col_index] == player_symbol for col_index in
             range(len(self.matrix))])
        return main_diagonal_winner or diagonal_winner

    def reset_game(self):
        self.matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for button in self.buttons.values():
            button.config(text=" ")
        self.turns_count = 1
        self.current_player_name = self.player1_name


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
