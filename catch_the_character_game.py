import random
import time
import sys

def catch_the_character():
    print("Welcome to Catch the Character!")
    print("Press the correct key as fast as you can when it appears.")
    print("You have 5 rounds. Let's go!\n")

    score = 0
    characters = ['A', 'B', 'C', 'D', 'E']

    for round_num in range(1, 6):
        target = random.choice(characters)
        print(f"Round {round_num}: Get ready...")
        time.sleep(random.uniform(1, 3))  # Random delay before showing character
        print(f"Press '{target}' NOW!")

        start_time = time.time()
        user_input = input("Your input: ").strip().upper()
        reaction_time = time.time() - start_time

        if user_input == target:
            print(f"Good job! Reaction time: {reaction_time:.2f} seconds\n")
            score += 1
        else:
            print(f"Oops! You pressed '{user_input}'. The correct key was '{target}'.\n")

    print(f"Game over! Your score: {score}/5")

catch_the_character()
