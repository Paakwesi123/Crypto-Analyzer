import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Step 1: Fetch data from CoinGecko API (Bitcoin, last 30 days)
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    'vs_currency': 'usd',
    'days': '30',
    'interval': 'daily'
}

response = requests.get(url, params=params)
data = response.json()

# Step 2: Extract and clean prices
prices = data['prices']  # list of [timestamp, price]
df = pd.DataFrame(prices, columns=['timestamp', 'price'])

# Convert timestamp to readable date
df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('date', inplace=True)
df.drop(columns=['timestamp'], inplace=True)

# Save to CSV
df.to_csv("output/prices.csv")

# Step 3: Calculate daily returns
df['returns'] = df['price'].pct_change()

# Step 4: Moving average
df['7d MA'] = df['price'].rolling(window=7).mean()

# Step 5: Plotting
sns.set(style="darkgrid")

# Plot 1: Price trend
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['price'], label='Price')
plt.plot(df.index, df['7d MA'], label='7-Day MA', linestyle='--')
plt.title("Bitcoin Price - Last 30 Days")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.tight_layout()
plt.savefig("output/trends.png")
plt.close()

# Plot 2: Daily returns
plt.figure(figsize=(10, 5))
df['returns'].plot(kind='bar', color='orange')
plt.title("Bitcoin Daily Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.tight_layout()
plt.savefig("output/returns.png")
plt.close()

print("✅ Analysis complete. Check the 'output/' folder.")
