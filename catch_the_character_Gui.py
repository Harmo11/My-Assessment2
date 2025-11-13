# catch_the_character_gui.py
import tkinter as tk
import random
import time

# Game variables
characters = ['A', 'B', 'C', 'D', 'E']
score = 0
round_num = 0
target = ''
bonus = False
start_time = 0
total_rounds = 5


# Function to start next round
def next_round():
    global round_num, target, bonus, start_time
    round_num += 1
    if round_num > total_rounds:
        end_game()
        return

    countdown_label.config(text=f"Round {round_num}: Get ready!")
    root.update()

    # Countdown 3..2..1
    root.after(500, lambda: countdown(3))


def countdown(n):
    if n > 0:
        countdown_label.config(text=f"Round {round_num}: {n}")
        root.update()
        root.after(500, lambda: countdown(n - 1))
    else:
        start_character()


def start_character():
    global target, bonus, start_time
    bonus = False
    if random.random() < 0.2:
        bonus = True

    target = random.choice(characters)
    if bonus:
        char_label.config(text=f"BONUS ROUND! Press '{target}' NOW!")
    else:
        char_label.config(text=f"Press '{target}' NOW!")

    root.update()
    start_time = time.time()


# Function to handle key presses
def key_pressed(event):
    global score
    if not target:
        return

    reaction_time = time.time() - start_time

    if reaction_time < 0.8:
        speed = "Fast!"
    elif reaction_time < 1.5:
        speed = "Average!"
    else:
        speed = "Slow!"

    if event.char.upper() == target:
        gained = 2 if bonus else 1
        score += gained
        result_label.config(text=f"Correct! Reaction: {reaction_time:.2f}s ({speed}) +{gained} point(s)")
    else:
        result_label.config(text=f"Oops! You pressed '{event.char.upper()}'. Correct was '{target}'. {speed}")

    root.update()
    # small delay before next round
    root.after(1000, next_round)


def end_game():
    char_label.config(text="")
    countdown_label.config(text=f"Game over! Score: {score}/{total_rounds}")
    if score == total_rounds:
        result_label.config(text="Amazing! Perfect score! 🎉")
    elif score >= 3:
        result_label.config(text="Nice job! 👍")
    else:
        result_label.config(text="Keep practicing! 💪")


# --- GUI setup ---
root = tk.Tk()
root.title("Catch the Character Game")

countdown_label = tk.Label(root, text="Welcome! Press any key to start.", font=("Helvetica", 16))
countdown_label.pack(pady=20)

char_label = tk.Label(root, text="", font=("Helvetica", 20, "bold"))
char_label.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Bind all key presses
root.bind("<Key>", key_pressed)


# Start the first round when any key is pressed
def start_game(event=None):
    global score, round_num
    score = 0
    round_num = 0
    next_round()


root.bind("<Key>", start_game, add="+")  # initial key starts the game

root.mainloop()
