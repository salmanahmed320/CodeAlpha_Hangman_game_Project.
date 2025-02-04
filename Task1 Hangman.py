# CODEALPHA
# Task#1: Hangman Game
# Objective: Design a text-based Hangman game. The program selects a random word, and the player guesses one letter at a time to uncover the word. You can set a limit on the number of incorrect guesses allowed.

# This is a GUI Based letter guesing game. 
# ******************************* HANGMAN GAME *****************************************************

import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
WORDS = ['python', 'hangman', 'challenge', 'programming', 'development']

# Game logic
class HangmanGame:
    def __init__(self):
        self.word = random.choice(WORDS)
        self.guessed_word = ['_' for _ in self.word]
        self.attempts_left = 6
        self.guessed_letters = []

    def make_guess(self, letter):
        if letter in self.guessed_letters:
            return 'Already guessed'
        
        self.guessed_letters.append(letter)
        if letter in self.word:
            for idx, char in enumerate(self.word):
                if char == letter:
                    self.guessed_word[idx] = letter
            return 'Correct'
        else:
            self.attempts_left -= 1
            return 'Incorrect'

    def is_game_over(self):
        return self.attempts_left <= 0 or '_' not in self.guessed_word

    def get_display_word(self):
        return ' '.join(self.guessed_word)

# GUI
class HangmanGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hangman Game")

        self.game = HangmanGame()

        self.word_label = tk.Label(master, text=self.game.get_display_word(), font=('Arial', 24))
        self.word_label.pack()

        self.input_label = tk.Label(master, text="Enter a letter:")
        self.input_label.pack()

        self.letter_entry = tk.Entry(master)
        self.letter_entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.guess_letter)
        self.guess_button.pack()

        self.status_label = tk.Label(master, text=f"Attempts left: {self.game.attempts_left}", font=('Arial', 16))
        self.status_label.pack()

    def guess_letter(self):
        letter = self.letter_entry.get()
        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        result = self.game.make_guess(letter)
        if result == 'Already guessed':
            messagebox.showinfo("Hangman", "You already guessed that letter.")
        elif result == 'Incorrect':
            messagebox.showinfo("Hangman", "Incorrect guess!")
        
        self.word_label.config(text=self.game.get_display_word())
        self.status_label.config(text=f"Attempts left: {self.game.attempts_left}")

        if self.game.is_game_over():
            if '_' not in self.game.guessed_word:
                messagebox.showinfo("Hangman", "Congratulations, you won!")
            else:
                messagebox.showinfo("Hangman", f"You lost! The word was: {self.game.word}")
            self.master.quit()

        self.letter_entry.delete(0, tk.END)

# Run the GUI
root = tk.Tk()
hangman_app = HangmanGUI(root)
root.mainloop()
