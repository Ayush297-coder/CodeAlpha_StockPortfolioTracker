# CodeAlpha_StockPortfolioTracker - Task 2

A clean, beginner-friendly, console-based **Stock Portfolio Tracker** developed in Python for **Task 2** of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
The **Stock Portfolio Tracker** is a Python console application designed to calculate total investment value based on manually defined stock prices. Users can add multiple stocks and their respective quantities, aggregate repeated entries, view a formatted breakdown of their portfolio with the highest-value holding highlighted, and export their summary to a timestamped `.txt` or `.csv` file.

This project is built purely in standard Python with zero external libraries or APIs, focusing on dictionary operations, user input validation, arithmetic computation, and file handling.

---

## 🚀 Features
- **Standard Library Only**: No external libraries, web scraping, or third-party APIs required.
- **Predefined Stock Pricing Dictionary**: Contains 5 major tech stocks (`AAPL`, `TSLA`, `GOOGL`, `MSFT`, `AMZN`).
- **Case-Insensitive Input**: Automatically converts user input to uppercase (e.g., `aapl` or `Aapl` -> `AAPL`).
- **Robust Quantity Validation**:
  - Rejects text, empty inputs, zeros, negative numbers, and decimals.
  - Accepts only positive whole numbers.
- **Smart Holdings Aggregation**: Adding an existing stock automatically adds to its quantity rather than overwriting it.
- **Formatted Table Summary**: Clear column alignment displaying Stock Symbol, Quantity, Price per Share, and Total Value.
- **Top Performer Indicator**: Highlights the stock with the largest financial holding value.
- **File Export**: Save the portfolio summary to `.txt` or `.csv` with an automated date/time stamp.
- **Graceful Termination**: Handles `Ctrl+C` (`KeyboardInterrupt`) cleanly without stack traces.

---

## 🛠️ Concepts & Technologies Used
- **Dictionaries**: Fast lookups, price mapping, and dynamic accumulation (`portfolio[symbol] = portfolio.get(symbol, 0) + qty`).
- **Input/Output & String Methods**: `.strip()`, `.upper()`, `.lower()`, and formatted f-strings (`:<10`, `:>15.2f`).
- **Control Flow**: `while` loops for validation and interactive re-prompts, `if-elif-else` branches.
- **Basic Arithmetic**: Unit multiplication (`qty * price`) and cumulative addition (`total_val += val`).
- **File Handling**: Writing formatted text reports (`.txt`) and comma-separated values (`.csv`) with the `with open(...)` context manager.
- **Date & Time**: `datetime.now()` for automated file timestamps.
- **Best Practices**: PEP 8 compliance, single-responsibility functions, and `if __name__ == "__main__":` entry point.

---

## 💻 How to Run the Project

### Prerequisites
- Python 3.x installed on your computer.

### Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/CodeAlpha_StockPortfolioTracker.git
   cd CodeAlpha_StockPortfolioTracker
   ```
2. Run the tracker in your terminal or command prompt:
   ```bash
   python stock_tracker.py
   ```

---

## 🎮 Sample Console Output

```text
==========================================
   CODEALPHA STOCK PORTFOLIO TRACKER   
==========================================
Stock Symbol         Price per Share
------------------------------------------
AAPL            $             180.00
TSLA            $             250.00
GOOGL           $             140.00
MSFT            $             330.00
AMZN            $             125.00
------------------------------------------
Enter stock symbol: AAPL
Enter quantity (whole number): 10
-> Added 10 shares of AAPL (Total AAPL: 10).

Add another stock? (y/n): y
Enter stock symbol: TSLA
Enter quantity (whole number): 5
-> Added 5 shares of TSLA (Total TSLA: 5).

Add another stock? (y/n): y
Enter stock symbol: aapl
Enter quantity (whole number): 5
-> Added 5 shares of AAPL (Total AAPL: 15).

Add another stock? (y/n): n

=======================================================
                 PORTFOLIO SUMMARY                 
=======================================================
Stock        Quantity     Price/Share     Total Value
-------------------------------------------------------
AAPL               15 $        180.00 $       2700.00
TSLA                5 $        250.00 $       1250.00
-------------------------------------------------------
Total Investment Value:               $       3950.00
Highest-Value Holding: AAPL ($2700.00)
=======================================================

Save result to file? (y/n): y
Choose file format (.txt or .csv): txt
Success! Portfolio saved as 'portfolio_summary.txt' in current folder.

Thank you for using Stock Portfolio Tracker! Happy investing!
```

---

## 📄 Exported File Samples

### `portfolio_summary.txt`
```text
STOCK PORTFOLIO REPORT
Date: 2026-10-24 23:00:56
=============================================
Stock        Quantity      Price      Value
---------------------------------------------
AAPL               15 $   180.00 $  2700.00
TSLA                5 $   250.00 $  1250.00
---------------------------------------------
Total Investment: $3950.00
```

### `portfolio_summary.csv`
```csv
# Date: 2026-10-24 23:01:15
Stock,Quantity,PricePerShare,TotalValue
GOOGL,10,140.00,1400.00
MSFT,5,330.00,1650.00
Total,,,3050.00
```

---

## 🔮 Future Improvements
- Integrate live stock prices using standard financial APIs (e.g., Yahoo Finance or Alpha Vantage).
- Add functionality to delete or sell shares from the portfolio.
- Visualize portfolio distribution using a ASCII or Matplotlib pie chart.

---

## 👤 Author
- **Intern Name**: Beginner Intern
- **Internship**: Python Programming Intern at [CodeAlpha](https://www.linkedin.com/company/codealpha/)
