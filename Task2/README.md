# Task 2 – Stock Portfolio Performance Tracker

## Project Description

The Stock Portfolio Performance Tracker is a Python application that helps users track their stock investments. It calculates the current market value of stocks and identifies the profit or loss of each investment.

## Features

- Enter stock ticker symbols.
- Enter buying prices and number of shares.
- Retrieve the latest available stock prices using Yahoo Finance.
- Calculate total invested amount.
- Calculate current market value.
- Calculate profit or loss for each stock.
- Calculate overall portfolio profit or loss.
- Save portfolio details to a CSV file.

## Technologies Used

- Python 3
- CSV Module
- yfinance Library
- Dictionaries
- File Handling

## Project Structure

```text
Task2/
│
├── portfolio.py
├── constituents.csv
├── portfolio_summary.csv
└── README.md
```

## Installation

Install the required library:

```bash
pip install yfinance
```

## How to Run

Run the following command in the terminal:

```bash
python portfolio.py
```

## How It Works

1. Enter a stock ticker symbol (e.g., AAPL or MSFT).
2. Enter the buying price.
3. Enter the number of shares.
4. Repeat to add more stocks.
5. Type `done` to finish entering stocks.
6. The program retrieves stock prices and calculates the portfolio performance.
7. The results are displayed in the terminal and saved in `portfolio_summary.csv`.

## Output

The program displays:

- Buy Price
- Current Price
- Quantity
- Invested Amount
- Current Value
- Profit/Loss
- Gain/Loss Percentage
- Total Portfolio Summary

The generated `portfolio_summary.csv` file stores the portfolio results.

## Author

Datheon Python Programming Internship – Task 2
