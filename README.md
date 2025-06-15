#  Crypto Analyzer

A simple and powerful data analysis project that fetches **live Bitcoin price data** from the [CoinGecko API](https://www.coingecko.com/), analyzes it using Python, and visualizes price trends and daily returns.

> Built with `requests`, `pandas`, `matplotlib`, and `seaborn`.

---

##  Features

-  Fetches **30-day historical Bitcoin prices** via API
-  Calculates **daily returns** and **7-day moving averages**
-  Generates 2 visualizations:
  - Line graph of price with 7-day moving average
  - Bar chart of daily returns
-  Exports cleaned data to `output/prices.csv`
-  Great for data engineering, analysis, and visualization portfolios

---

## 🛠 Technologies

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Requests

---

##  Output Files

After running the project, you'll find:

| File | Description |
|------|-------------|
| `output/prices.csv` | Cleaned BTC price data with daily returns and MA |
| `output/trends.png` | Line graph of price and 7-day moving average |
| `output/returns.png` | Bar chart of daily returns |

---

##  Installation

1. Clone this repo or download the files
2. Install dependencies:

```bash
pip install -r requirements.txt
