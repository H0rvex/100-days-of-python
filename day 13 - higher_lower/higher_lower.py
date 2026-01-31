import art
import game_data
import random
import os

CHOICE_A = {}
CHOICE_B = {}

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def clear_screen_pycharm():
    print("\n"*20)


def comparison(choice1_c, choice2_c):
    choice1_c_value = choice1_c["follower_count"]
    choice2_c_value = choice2_c["follower_count"]
    if choice1_c_value > choice2_c_value:
        return True
    elif choice1_c_value < choice2_c_value:
        return False


def choice_a():
    random_a = random.choice(game_data.data)
    global CHOICE_A
    CHOICE_A = random_a
    name = random_a["name"]
    description = random_a["description"]
    country = random_a["country"]
    print(f"Compare A: {name}, a {description}, from {country}.")
    return random_a, name, description, country



def choice_b():
    random_b = random.choice(game_data.data)
    global CHOICE_B
    CHOICE_B = random_b
    name2 = random_b["name"]
    description2 = random_b["description"]
    country2 = random_b["country"]
    print(f"Against B: {name2}, a {description2}, from {country2}.")
    return random_b, name2, description2, country2



def game():
    global CHOICE_A
    is_game_over = False
    score = 0
    message = ""
    first_round = True
    while not is_game_over:
        clear_screen_pycharm()
        print(art.logo)
        if message:
            print(message)
        if first_round:
            choice_a()
            first_round = False
        else:
            print(f"Compare A: {CHOICE_A['name']}, a {CHOICE_A['description']}, from {CHOICE_A['country']}.")
        print(art.vs)
        choice_b()
        comparison(choice1_c=CHOICE_A, choice2_c=CHOICE_B)
        answer = input("Who has more followers? Type 'a' or 'b':").lower()
        if answer == "a" and comparison(choice1_c=CHOICE_A, choice2_c=CHOICE_B) is True:
            score += 1
            message = f"You are right! Current score: {score}"
            CHOICE_A = CHOICE_B
            choice_b()
        elif answer == "b" and comparison(choice1_c=CHOICE_A, choice2_c=CHOICE_B) is False:
            score += 1
            message = f"You are right! Current score: {score}"
            CHOICE_A = CHOICE_B
            choice_b()
        elif answer == "a" and comparison(choice1_c=CHOICE_A, choice2_c=CHOICE_B) is False:
            is_game_over = True
            message = f"That's wrong. Final score: {score}"
        elif answer == "b" and comparison(choice1_c=CHOICE_A, choice2_c=CHOICE_B) is True:
            is_game_over = True
            message = f"That's wrong. Final score: {score}"
    clear_screen_pycharm()
    print(art.logo)
    print(message)

game()

