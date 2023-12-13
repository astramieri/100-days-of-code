print("Welcome to the secret auction program.")

bids = []

def add_bid(name, bid):
    new_bid = {}
    new_bid["name"] = name
    new_bid["bid"] = bid
    bids.append(new_bid)

def print_highest_bid():
    highest_bid = bids[0]
    for bid in bids:
        if bid["bid"] > highest_bid["bid"]:
            highest_bid = bid
    print(highest_bid)

new_bidder = True

while new_bidder:
    new_name = input("What is your name? ")
    new_bid = int(input("What is your bid (€)? "))

    add_bid(name=new_name, bid=new_bid)

    other_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")

    if other_bidder == 'no':
        new_bidder = False

print_highest_bid()


