import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will play 5 rounds against the computer.\n")

    choices = ["rock", "paper", "scissors"]
    score_player = 0
    score_computer = 0

    for round_num in range(1, 6):
        print(f"Round {round_num}")
        player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if player_choice not in choices:
            print("Invalid choice! Try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!\n")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!\n")
            score_player += 1
        else:
            print("Computer wins this round!\n")
            score_computer += 1

    print("Game Over!")
    print(f"Your score: {score_player}")
    print(f"Computer score: {score_computer}")

    if score_player > score_computer:
        print("Congratulations! You won the game! 🎉")
    elif score_player < score_computer:
        print("Computer won the game! Better luck next time!")
    else:
        print("It's a tie overall!")

# Run the game
rock_paper_scissors()
