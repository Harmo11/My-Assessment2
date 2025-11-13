import random


def math_quiz():
    print("Welcome to the Math Quiz Game!")
    print("You will be asked 5 simple math questions.\n")

    score = 0
    rounds = 5

    for i in range(1, rounds + 1):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])

        if operator == "+":
            correct_answer = num1 + num2
        elif operator == "-":
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        print(f"Question {i}: {num1} {operator} {num2} = ?")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! 🎉\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}.\n")
        except:
            print(f"Invalid input! The correct answer is {correct_answer}.\n")

    print("Quiz Over!")
    print(f"Your score: {score}/{rounds}")
    if score == rounds:
        print("Perfect score! Amazing job! 🏆")
    elif score >= 3:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")


# Run the game
math_quiz()
