from random import randint
import art


def get_random_number():
    return randint(1, 100)


def set_difficulty():
    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_choice == "easy":
        return 10
    else:
        return 5


def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return attempts


def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = get_random_number()

    attempts = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, answer, attempts)

        if guess != answer:
            if attempts == 0:
                print("You've run out of guesses. You lose.")
                print(f"The answer was {answer}.")
                return
            else:
                print("Guess again.")

game()





