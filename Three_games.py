import tkinter as tk
import random
import time

# -----------------------------
# Globals
# -----------------------------
# Catch the Character
characters = ['A', 'B', 'C', 'D', 'E']
score = 0
round_num = 0
target = ''
bonus = False
start_time = 0
total_rounds = 5

# WOT Game
wot_words = ["PYTHON", "GITHUB", "LUDO", "TKINTER", "CODE"]
wot_target = ""
wot_score = 0
wot_round = 0
wot_total_rounds = 3
wot_start_time = 0


# -----------------------------
# Catch the Character Functions
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
    if game_frame.winfo_ismapped() and target:  # only for Catch the Character
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

    # WOT Game input
    if wot_frame.winfo_ismapped() and event.keysym == "Return":
        check_wot_guess()


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
# Ludo Functions
# -----------------------------
def start_ludo():
    main_menu_frame.pack_forget()
    ludo_frame.pack()


def roll_dice():
    dice = random.randint(1, 6)
    ludo_result_label.config(text=f"You rolled a {dice}!")


# -----------------------------
# WOT Functions
# -----------------------------
def start_wot_game():
    global wot_round, wot_score
    wot_round = 0
    wot_score = 0
    main_menu_frame.pack_forget()
    wot_frame.pack()
    next_wot_round()


def next_wot_round():
    global wot_target, wot_start_time, wot_round
    wot_round += 1
    if wot_round > wot_total_rounds:
        end_wot_game()
        return
    wot_target = random.choice(wot_words)
    wot_label.config(text=f"Round {wot_round}: Guess the word!")
    wot_entry.delete(0, tk.END)
    wot_feedback_label.config(text="")
    wot_start_time = time.time()


def check_wot_guess():
    global wot_score
    guess = wot_entry.get().strip().upper()
    reaction_time = time.time() - wot_start_time
    if guess == wot_target:
        wot_score += 1
        feedback = f"Correct! +1 point ({reaction_time:.2f}s)"
    else:
        feedback = f"Wrong! The word was '{wot_target}' ({reaction_time:.2f}s)"
    wot_feedback_label.config(text=feedback)
    root.update()
    root.after(1000, next_wot_round)


def end_wot_game():
    wot_label.config(text=f"Game over! Score: {wot_score}/{wot_total_rounds}")
    wot_feedback_label.config(text="Back to menu to play again.")


# -----------------------------
# General GUI
# -----------------------------
root = tk.Tk()
root.title("Mini Game Hub - 3 Games")

# --- Main menu ---
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(pady=50)

menu_label = tk.Label(main_menu_frame, text="Choose a game to play", font=("Helvetica", 16))
menu_label.pack(pady=10)

btn_catch = tk.Button(main_menu_frame, text="Catch the Character", command=start_catch_game)
btn_catch.pack(pady=5)

btn_ludo = tk.Button(main_menu_frame, text="Ludo (Dice Roll)", command=start_ludo)
btn_ludo.pack(pady=5)

btn_wot = tk.Button(main_menu_frame, text="WOT Guessing Game", command=start_wot_game)
btn_wot.pack(pady=5)

# --- Catch the Character Frame ---
game_frame = tk.Frame(root)

countdown_label = tk.Label(game_frame, text="", font=("Helvetica", 16))
countdown_label.pack(pady=20)

char_label = tk.Label(game_frame, text="", font=("Helvetica", 20, "bold"))
char_label.pack(pady=20)

result_label = tk.Label(game_frame, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

back_button_game = tk.Button(game_frame, text="Back to Menu",
                             command=lambda: [game_frame.pack_forget(), main_menu_frame.pack()])
back_button_game.pack(pady=10)

# --- Ludo Frame ---
ludo_frame = tk.Frame(root)

ludo_label = tk.Label(ludo_frame, text="Ludo Dice Roll", font=("Helvetica", 16))
ludo_label.pack(pady=20)

roll_btn = tk.Button(ludo_frame, text="Roll Dice", command=roll_dice)
roll_btn.pack(pady=10)

ludo_result_label = tk.Label(ludo_frame, text="", font=("Helvetica", 14))
ludo_result_label.pack(pady=10)

back_button_ludo = tk.Button(ludo_frame, text="Back to Menu",
                             command=lambda: [ludo_frame.pack_forget(), main_menu_frame.pack()])
back_button_ludo.pack(pady=10)

# --- WOT Frame ---
wot_frame = tk.Frame(root)

wot_label = tk.Label(wot_frame, text="WOT Game", font=("Helvetica", 16))
wot_label.pack(pady=20)

wot_entry = tk.Entry(wot_frame)
wot_entry.pack(pady=5)
wot_entry.focus()

wot_feedback_label = tk.Label(wot_frame, text="", font=("Helvetica", 14))
wot_feedback_label.pack(pady=10)

back_button_wot = tk.Button(wot_frame, text="Back to Menu",
                            command=lambda: [wot_frame.pack_forget(), main_menu_frame.pack()])
back_button_wot.pack(pady=10)

# --- Bind keys ---
root.bind("<Key>", key_pressed)

root.mainloop()
