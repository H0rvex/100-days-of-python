import auction_art

database = {}


other_bidders = True

print(auction_art.logo)
while other_bidders == True:
    ask_name = str(input("What is your name?:")).lower()
    ask_bid = int(input("What is your bid?: $"))
    ask_if_other_bidders = input("Are there other users who want to bid?").lower()

    database[f"{ask_name}"] = ask_bid

    if ask_if_other_bidders == "yes":
        other_bidders = True
        print("\n"*20)
    elif ask_if_other_bidders == "no":
        other_bidders = False
        for keys in database:
            winner = max(database, key=database.get)
            winning_bid = database[winner]
        print(f"The winner is {winner} with a ${winning_bid} bid.")















