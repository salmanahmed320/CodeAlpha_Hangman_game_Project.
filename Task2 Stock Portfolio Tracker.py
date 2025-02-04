# CODEALPHA
# Task#2: Stock Portfolio Tracker
# Objective: Create a stock portfolio tracking tool that allows users to add, remove, and track the performance of their stock investments. Utilize financial APIs for real-time stock data.

# This is a Console Based Portfolio Tracker App. 
# ******************************* Stock Portfolio Tracker *****************************************************

import requests

# Replace with your own Alpha Vantage API key
API_KEY = "PXIN90JDMTTKJHWW"  # Replace "demo" with your Alpha Vantage API key
BASE_URL = "https://www.alphavantage.co/query"

# Sample portfolio to begin with
portfolio = {
    "AAPL": {"shares": 10, "price_per_share": 150},
    "MSFT": {"shares": 5, "price_per_share": 300},
}

def get_stock_price(symbol):
    """
    Fetch the current stock price for a given symbol using Alpha Vantage API.
    """
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    try:
        price = float(data["Global Quote"]["05. price"])
        return price
    except (KeyError, ValueError):
        print(f"Error fetching data for {symbol}. Check the stock symbol or API key.")
        return None

def add_stock(symbol, shares, price_per_share):
    """
    Add a stock to the portfolio.
    """
    portfolio[symbol] = {"shares": shares, "price_per_share": price_per_share}
    print(f"Added {shares} shares of {symbol} at ${price_per_share} per share.")

def remove_stock(symbol):
    """
    Remove a stock from the portfolio.
    """
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")

def view_portfolio():
    """
    Display the current portfolio with real-time prices and performance.
    """
    print("\nYour Stock Portfolio:")
    print("-" * 40)
    total_value = 0
    for symbol, info in portfolio.items():
        shares = info["shares"]
        price_per_share = info["price_per_share"]
        current_price = get_stock_price(symbol)
        
        if current_price:
            value = shares * current_price
            total_value += value
            gain_loss = value - (shares * price_per_share)
            print(f"{symbol}: {shares} shares | Bought at ${price_per_share} | "
                  f"Current Price: ${current_price:.2f} | Value: ${value:.2f} | "
                  f"Gain/Loss: ${gain_loss:.2f}")
    print("-" * 40)
    print(f"Total Portfolio Value: ${total_value:.2f}")
    print("-" * 40)

def main():
    """
    Main menu to manage the portfolio.
    """
    while True:
        print("\nStock Portfolio Tracker")
        print("1. View Portfolio")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_portfolio()
        elif choice == "2":
            symbol = input("Enter stock symbol (e.g., AAPL, MSFT): ").upper()
            shares = int(input("Enter the number of shares: "))
            price_per_share = float(input("Enter the price per share: "))
            add_stock(symbol, shares, price_per_share)
        elif choice == "3":
            symbol = input("Enter the stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
