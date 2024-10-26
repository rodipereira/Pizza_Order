print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Pizza size code ->

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Your size don't exist.")

# Add pepperoni

if pepperoni == "Y":
    size == "S"
    bill += 2
else:
    bill += 3

# Add extra Cheese

if extra_cheese == "Y":
    bill += 1
total_bill = bill
print(f"Your total bill is ${total_bill}")

