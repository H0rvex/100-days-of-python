print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n ").lower()
pepperoni = input("Would you like pepperoni on your pizza? Y or N\n").lower()
extra_cheese = input("Do you want extra cheese on your pizza? Y or N\n").lower()
bill = 0
if size == "s":
    bill += 15
    if pepperoni == "y":
        bill +=3
    if extra_cheese == "y":
        bill += 1

if size == "m":
    bill += 20
    if pepperoni == "y":
        bill +=3
    if extra_cheese == "y":
        bill += 1
if size == "l":
    bill += 25
    if pepperoni == "y":
        bill +=3
    if extra_cheese == "y":
        bill += 1
print(f"Your final bill is: ${bill}.")






