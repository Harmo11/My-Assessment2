# catch_the_character.py
import random
import time

def catch_the_character():
    print("Welcome to Catch the Character!")
    print("Press the correct key as fast as you can when it appears.")
    print("You have 5 rounds. Let's go!\n")

    score = 0
    characters = ['A', 'B', 'C', 'D', 'E']

    for round_num in range(1, 6):
        target = random.choice(characters)

        # Countdown
        print(f"Round {round_num}: Get ready...")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(0.5)
        time.sleep(random.uniform(0.5, 1.5))  # small random delay

        # Occasionally choose a bonus character
        bonus = False
        if random.random() < 0.2:  # 20% chance
            target = random.choice(characters)
            print(f"BONUS ROUND! Press '{target}' NOW!")
            bonus = True
        else:
            print(f"Press '{target}' NOW!")

        start_time = time.time()
        user_input = input("Your input: ").strip().upper()
        reaction_time = time.time() - start_time

        # Reaction feedback
        if reaction_time < 0.8:
            speed = "Fast!"
        elif reaction_time < 1.5:
            speed = "Average!"
        else:
            speed = "Slow!"

        if user_input == target:
            gained = 2 if bonus and target == user_input else 1
            score += gained
            print(f"Good job! Reaction time: {reaction_time:.2f}s ({speed}) +{gained} point(s)\n")
        else:
            print(f"Oops! You pressed '{user_input}'. The correct key was '{target}'. {speed}\n")

    # Fun end message
    print(f"Game over! Your total score: {score}/5")
    if score == 5:
        print("Amazing! Perfect score! 🎉")
    elif score >= 3:
        print("Nice job! 👍")
    else:
        print("Keep practicing! 💪")

# Call the game
catch_the_character()
