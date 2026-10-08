due = 50
while due > 0:
    print(f"Amount Due: {due}")
    coin = input("Coin: ")
    coin = int(coin)
    due -= coin

print(f"Change Owed: {abs(due)}")