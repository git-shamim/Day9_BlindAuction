
from art import logo
# from os import system, name

print(logo)

bid_records = {}
bidding_finish = False


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_records:
        bid_amount = bid_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print("The winner is {0} with a bid price of ${1}".format(winner, highest_bid))


while not bidding_finish:
    bidder_name = input("What is your name?\n: ")
    bid_price = int(input("What is your bid? \n: $"))
    bid_records[bidder_name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n: ").lower()
    if should_continue == 'no' or should_continue == 'yes':
        if should_continue == 'no':
            bidding_finish = True
            find_highest_bid(bid_records)
    else:
        print("Please enter a valid response")
