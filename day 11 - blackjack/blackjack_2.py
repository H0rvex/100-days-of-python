import random
import blackjack_art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went above 21, you lose!"
    elif computer_score > 21:
        return "Opponent went over 21, you win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print(blackjack_art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: [{computer_cards[0]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            want_card = input("Do you want to get another card: 'yes' or 'no'?").lower()
            if want_card == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards were: {user_cards}, score: {user_score}\nComputer's cards were: {computer_cards}, score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game?").lower() == "yes":
    print("\n"*20)
    play_game()












