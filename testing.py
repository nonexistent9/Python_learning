auction_value={}
name = input("Please enter your name: ")
bid = int(input("enter your bid amount "))
auction_value[name] = bid
more = input("Are there more members in the auction? Y/N ")
more = more.lower()
while more == "y":
    
    name = input("Please enter your name: ")
    bid = int(input("enter your bid amount "))
    auction_value[name] = bid
    more = input("Are there more members in the auction? Y/N ")

print(auction_value)

max_bid = 0
for i, name in enumerate(auction_value):
    
    if auction_value[name]>max_bid:
        max_bid = auction_value[name]
print(max_bid)
