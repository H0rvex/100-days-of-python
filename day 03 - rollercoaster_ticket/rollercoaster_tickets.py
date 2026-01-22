print("Welcome to the rollercoaster!")
height = int(input("What's your height?"))
bill = 0
if height >= 120:
    print("Thank you!")
    age = int(input("What's your age?"))
    if age >= 18:
        print("Adult tickets are $12.")
        bill = 12
    elif age <= 12:
        print("Child tickets are $5.")
        bill =5
    else:
        print("Youth tickets are $7.")
        bill = 7
    photo = input("Do you want photos, type y for Yes and n for No.")
    if photo == "y":
        print(f" Your total bill is: ${bill + 3}")
    if photo == "n":
        print(f"Your total bill is: ${bill}")
else:
    print("You are not tall enough!")

