# Secret auction bid:

# How to get the max value in a dictionary of key, val pairs
# How to get the key with the max value in a dictionary of key, val pairs

def keep_bidding(answer):
    if answer == "yes" or answer == "no":
        return answer == "yes"
    else:
        return keep_bidding(input("Invalid option, please type - 'yes' or 'no': ").lower())


def try_float(amount):
    try:
        return float(amount)
    except (ValueError, TypeError):
        return try_float(input("Please enter a valid bid: £"))


bid_dictionary = {}
while True:
    name = input("Please enter a name: ")
    bid = try_float(input("Please enter your bid: £"))
    bid_dictionary[name] = bid
    if not keep_bidding(input("Any more bidders? - 'yes' or 'no'?: ").lower()):
        break

print(f"Bids were: ")
for bid in bid_dictionary:
    print(f"{bid} £{bid_dictionary[bid]}")


top_bid = max(list(bid_dictionary.values()))
top_bid = f"{round(top_bid, 2):.2f}"
top_bidder = max(bid_dictionary, key=bid_dictionary.get)  # gets the key with the highest value from a dictionary
print(f"The top bidder was {top_bidder} with a bid of £{top_bid}")

