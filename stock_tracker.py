import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print("📊 Advanced Stock Portfolio Tracker")

portfolio = {}

n = int(input("Enter number of stocks: "))

# Input stocks
for i in range(n):
    stock = input(f"Enter stock {i+1} symbol (e.g. AAPL): ").upper()
    qty = int(input("Enter quantity: "))
    portfolio[stock] = qty

data = []
total_value = 0

# Fetch real-time data
for stock, qty in portfolio.items():
    try:
        ticker = yf.Ticker(stock)
        price = ticker.history(period="1d")["Close"].iloc[-1]
        value = price * qty
        total_value += value

        data.append([stock, qty, price, value])
    except:
        print(f"❌ Error fetching data for {stock}")

# Create DataFrame
df = pd.DataFrame(data, columns=["Stock", "Quantity", "Price", "Value"])

# Show output
print("\n📋 Portfolio Summary:")
print(df)

print("\n💰 Total Portfolio Value:", total_value)

# Save CSV
df.to_csv("portfolio.csv", index=False)
print("✅ Saved to portfolio.csv")

# Visualization
df.set_index("Stock")["Value"].plot(kind="bar")
plt.title("Portfolio Distribution")
plt.ylabel("Value")
plt.show()