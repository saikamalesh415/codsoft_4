import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_game("Rock"))
        self.rock_button.pack(pady=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_game("Paper"))
        self.paper_button.pack(pady=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_game("Scissors"))
        self.scissors_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=("Helvetica", 12))
        self.score_label.pack(pady=20)

    def get_score_text(self):
        return f"User Score: {self.user_score}   Computer Score: {self.computer_score}   Ties: {self.ties}"

    def play_game(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        result = self.determine_winner(user_choice, computer_choice)

        if result == "Tie":
            self.ties += 1
        elif result == "User":
            self.user_score += 1
        elif result == "Computer":
            self.computer_score += 1

        self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. Result: {result}")
        self.score_label.config(text=self.get_score_text())

        self.root.after(100, self.ask_play_again)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                (user_choice == "Paper" and computer_choice == "Rock") or \
                (user_choice == "Scissors" and computer_choice == "Paper"):
            return "User"
        else:
            return "Computer"

    def ask_play_again(self):
        if messagebox.askyesno("Play Again?", "Do you want to play again?"):
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
