from art import logo
again = 'yes'
auction = {}
print(logo)
print("Welcome to the Blind Auction")
while again == 'yes':
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: R$"))
    auction[name] = bid
    again = input("Are there any other bidders? Type 'yes' or 'no'\n")
    print("\n" * 100)

max_value = -99
max_name = ""
for key in auction:
    if auction[key] > max_value:
        max_value = auction[key]
        max_name = key
print(f"The winner is {max_name} with a bid of R${round(max_value, 2)}.")

