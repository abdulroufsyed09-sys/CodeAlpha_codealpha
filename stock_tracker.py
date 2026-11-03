prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330}

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks:", prices)

portfolio = {}   # stock name -> quantity

while True:
    name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if name == "DONE":
        break

    if name not in prices:
        print("Stock not available.")
        continue

    qty = int(input("Enter quantity: "))
    portfolio[name] = portfolio.get(name, 0) + qty

# calculate total
total = 0
print("==========================================")
print("Your Portfolio:")
print("==========================================")
for name in portfolio:
    value = portfolio[name] * prices[name]
    total += value
    print(name, "-", portfolio[name], "shares x $", prices[name], "= $", value)

print("Total investment: $", total)

# optional: save to file
save = input("\nSave result to file? (y/n): ").lower()
if save == "y":
    file = open("portfolio.txt", "w")
    for name in portfolio:
        file.write(name + ": " + str(portfolio[name]) + " shares\n")
    file.write("Total investment: $" + str(total))
    file.close()
    print("Saved to portfolio.txt")