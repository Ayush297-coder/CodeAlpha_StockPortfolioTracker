"""
CodeAlpha Python Programming Internship - Task 2
Project: Stock Portfolio Tracker (Console)
"""

from datetime import datetime

# Hardcoded dictionary for stock prices (no APIs / external libraries)
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 330.00,
    "AMZN": 125.00
}


def show_stocks():
    """Display welcome banner and available stocks with prices."""
    print("\n" + "=" * 42)
    print("   CODEALPHA STOCK PORTFOLIO TRACKER   ")
    print("=" * 42)
    print(f"{'Stock Symbol':<15} {'Price per Share':>20}")
    print("-" * 42)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<15} ${price:>19.2f}")
    print("-" * 42)


def get_stock_name():
    """Prompt user for a valid stock symbol (case-insensitive)."""
    while True:
        symbol = input("Enter stock symbol: ").strip().upper()
        if symbol in STOCK_PRICES:
            return symbol
        print(f"Error: '{symbol}' not found. Please choose from the list.")


def get_quantity():
    """Prompt user for a positive whole number quantity."""
    while True:
        qty_str = input("Enter quantity (whole number): ").strip()
        if qty_str.isdigit() and int(qty_str) > 0:
            return int(qty_str)
        print("Invalid input! Please enter a whole number greater than 0.")


def calculate_total(portfolio):
    """Calculate total investment value and identify top holding."""
    total_val, top_stock, top_val = 0.0, None, 0.0
    for symbol, qty in portfolio.items():
        val = qty * STOCK_PRICES[symbol]
        total_val += val
        if val > top_val:
            top_val, top_stock = val, symbol
    return total_val, top_stock, top_val


def display_summary(portfolio, total_val, top_stock, top_val):
    """Display a clean formatted summary table of holdings."""
    print("\n" + "=" * 55)
    print("                 PORTFOLIO SUMMARY                 ")
    print("=" * 55)
    print(f"{'Stock':<10} {'Quantity':>10} {'Price/Share':>15} {'Total Value':>15}")
    print("-" * 55)
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        print(f"{symbol:<10} {qty:>10} ${price:>14.2f} ${qty * price:>14.2f}")
    print("-" * 55)
    print(f"{'Total Investment Value:':<37} ${total_val:>14.2f}")
    if top_stock:
        print(f"Highest-Value Holding: {top_stock} (${top_val:.2f})")
    print("=" * 55)


def save_to_file(portfolio, total_val):
    """Optionally save the summary to a .txt or .csv file with timestamp."""
    if input("\nSave result to file? (y/n): ").strip().lower() != "y":
        return
    while True:
        fmt = input("Choose file format (.txt or .csv): ").strip().lower()
        if fmt in ["txt", ".txt", "csv", ".csv"]:
            break
        print("Invalid format! Please enter 'txt' or 'csv'.")

    ext = "csv" if "csv" in fmt else "txt"
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"portfolio_summary.{ext}"

    with open(filename, "w", encoding="utf-8") as f:
        if ext == "txt":
            f.write(f"STOCK PORTFOLIO REPORT\nDate: {ts}\n" + "=" * 45 + "\n")
            f.write(f"{'Stock':<10} {'Quantity':>10} {'Price':>10} {'Value':>10}\n" + "-" * 45 + "\n")
            for s, q in portfolio.items():
                p = STOCK_PRICES[s]
                f.write(f"{s:<10} {q:>10} ${p:>9.2f} ${q * p:>9.2f}\n")
            f.write("-" * 45 + f"\nTotal Investment: ${total_val:.2f}\n")
        else:
            f.write(f"# Date: {ts}\nStock,Quantity,PricePerShare,TotalValue\n")
            for s, q in portfolio.items():
                p = STOCK_PRICES[s]
                f.write(f"{s},{q},{p:.2f},{q * p:.2f}\n")
            f.write(f"Total,,,{total_val:.2f}\n")
    print(f"Success! Portfolio saved as '{filename}' in current folder.")


def main():
    """Main program execution loop with replay and graceful exit."""
    try:
        portfolio = {}
        show_stocks()
        while True:
            symbol = get_stock_name()
            qty = get_quantity()
            portfolio[symbol] = portfolio.get(symbol, 0) + qty
            print(f"-> Added {qty} shares of {symbol} (Total {symbol}: {portfolio[symbol]}).")

            if input("\nAdd another stock? (y/n): ").strip().lower() != "y":
                break

        total_val, top_stock, top_val = calculate_total(portfolio)
        display_summary(portfolio, total_val, top_stock, top_val)
        save_to_file(portfolio, total_val)
        print("\nThank you for using Stock Portfolio Tracker! Happy investing!")
    except KeyboardInterrupt:
        print("\n\nProgram closed gracefully. Goodbye!")


if __name__ == "__main__":
    main()
