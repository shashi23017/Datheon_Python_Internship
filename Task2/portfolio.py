
import csv
import yfinance as yf
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(folder_path, "portfolio_summary.csv")

portfolio = {}

print("====================================")
print("   STOCK PORTFOLIO PERFORMANCE TRACKER")
print("====================================")

while True:
    ticker = input("\nEnter stock ticker (or 'done' to finish): ").upper().strip()

    if ticker == "DONE":
        break

    if not ticker:
        print("Please enter a valid ticker.")
        continue

    if ticker in portfolio:
        print("This stock has already been added.")
        continue

    try:
        buy_price = float(input("Enter buying price: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than zero.")
            continue

        portfolio[ticker] = {
            "buy_price": buy_price,
            "quantity": quantity
        }

        print("Stock added successfully!")

    except ValueError:
        print("Please enter valid numbers.")

if not portfolio:
    print("\nNo stocks were added.")

else:
    total_invested = 0
    total_market_value = 0

    print("\n========== PORTFOLIO SUMMARY ==========")

    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Ticker",
            "Buy Price",
            "Current Price",
            "Quantity",
            "Invested Amount",
            "Current Value",
            "Profit/Loss",
            "Gain/Loss (%)"
        ])

        for ticker, details in portfolio.items():

            try:
                stock = yf.Ticker(ticker)
                history = stock.history(period="5d")

                if history.empty:
                    print(f"\nPrice not available for {ticker}.")
                    continue

                current_price = float(history["Close"].dropna().iloc[-1])

                buy_price = details["buy_price"]
                quantity = details["quantity"]

                invested_amount = buy_price * quantity
                current_value = current_price * quantity

                profit_loss = current_value - invested_amount

                percentage = (profit_loss / invested_amount) * 100

                total_invested += invested_amount
                total_market_value += current_value

                print(f"\nStock: {ticker}")
                print(f"Buy Price: ${buy_price:.2f}")
                print(f"Current Price: ${current_price:.2f}")
                print(f"Quantity: {quantity}")
                print(f"Invested Amount: ${invested_amount:.2f}")
                print(f"Current Value: ${current_value:.2f}")
                print(f"Profit/Loss: ${profit_loss:.2f}")
                print(f"Gain/Loss: {percentage:.2f}%")

                writer.writerow([
                    ticker,
                    round(buy_price, 2),
                    round(current_price, 2),
                    quantity,
                    round(invested_amount, 2),
                    round(current_value, 2),
                    round(profit_loss, 2),
                    round(percentage, 2)
                ])

            except Exception as error:
                print(f"\nUnable to retrieve data for {ticker}: {error}")

    total_profit_loss = total_market_value - total_invested

    if total_invested > 0:
        total_percentage = (total_profit_loss / total_invested) * 100
    else:
        total_percentage = 0

    print("\n========== TOTAL PORTFOLIO ==========")
    print(f"Total Invested: ${total_invested:.2f}")
    print(f"Total Market Value: ${total_market_value:.2f}")
    print(f"Total Profit/Loss: ${total_profit_loss:.2f}")
    print(f"Total Gain/Loss: {total_percentage:.2f}%")

    print("\nPortfolio summary saved to:")
    print(csv_path)

print("\nThank you for using the tracker!")
