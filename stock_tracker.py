# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER      ")
print("===================================")

while True:

    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    # Check stock availability
    if stock_name not in stock_prices:
        print("Stock not found in database.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            continue

    except ValueError:
        print("Invalid quantity.")
        continue

    # Calculate investment
    investment = stock_prices[stock_name] * quantity

    # Save in portfolio
    portfolio[stock_name] = quantity

    total_investment += investment

    print(f"Added {quantity} shares of {stock_name}")
    print(f"Current Investment: ${investment}")

print("\n========== PORTFOLIO SUMMARY ==========")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty

    print(f"{stock} -> Quantity: {qty}, Price: ${price}, Value: ${value}")

print("\nTotal Investment Value: $", total_investment)

# Save to file
with open("portfolio_summary.txt", "w") as file:

    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("========================\n")

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty

        file.write(f"{stock} -> Quantity: {qty}, Value: ${value}\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio saved successfully in portfolio_summary.txt")
