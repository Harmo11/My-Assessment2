import tkinter as tk
import random
import time

# -----------------------------
# Globals for Catch the Character
# -----------------------------
characters = ['A', 'B', 'C', 'D', 'E']
score = 0
round_num = 0
target = ''
bonus = False
start_time = 0
total_rounds = 5


# -----------------------------
# Functions for Catch the Character
# -----------------------------
def next_round():
    global round_num, target, bonus, start_time
    round_num += 1
    if round_num > total_rounds:
        end_game()
        return

    countdown_label.config(text=f"Round {round_num}: Get ready!")
    root.update()
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


def start_catch_game():
    global score, round_num
    score = 0
    round_num = 0
    main_menu_frame.pack_forget()
    game_frame.pack()
    next_round()


# -----------------------------
# Simple Ludo (dice roll only) for demo
# -----------------------------
def start_ludo():
    main_menu_frame.pack_forget()
    ludo_frame.pack()


def roll_dice():
    dice = random.randint(1, 6)
    ludo_result_label.config(text=f"You rolled a {dice}!")


def back_to_menu():
    game_frame.pack_forget()
    ludo_frame.pack_forget()
    main_menu_frame.pack()


# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Mini Game Hub")

# --- Main menu ---
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(pady=50)

menu_label = tk.Label(main_menu_frame, text="Choose a game to play", font=("Helvetica", 16))
menu_label.pack(pady=10)

btn_catch = tk.Button(main_menu_frame, text="Catch the Character", command=start_catch_game)
btn_catch.pack(pady=5)

btn_ludo = tk.Button(main_menu_frame, text="Ludo (Dice Roll)", command=start_ludo)
btn_ludo.pack(pady=5)

# --- Catch the Character Frame ---
game_frame = tk.Frame(root)

countdown_label = tk.Label(game_frame, text="", font=("Helvetica", 16))
countdown_label.pack(pady=20)

char_label = tk.Label(game_frame, text="", font=("Helvetica", 20, "bold"))
char_label.pack(pady=20)

result_label = tk.Label(game_frame, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

back_button_game = tk.Button(game_frame, text="Back to Menu", command=back_to_menu)
back_button_game.pack(pady=10)

root.bind("<Key>", key_pressed)

# --- Ludo Frame ---
ludo_frame = tk.Frame(root)

ludo_label = tk.Label(ludo_frame, text="Ludo Dice Roll", font=("Helvetica", 16))
ludo_label.pack(pady=20)

roll_btn = tk.Button(ludo_frame, text="Roll Dice", command=roll_dice)
roll_btn.pack(pady=10)

ludo_result_label = tk.Label(ludo_frame, text="", font=("Helvetica", 14))
ludo_result_label.pack(pady=10)

back_button_ludo = tk.Button(ludo_frame, text="Back to Menu", command=back_to_menu)
back_button_ludo.pack(pady=10)

root.mainloop()
