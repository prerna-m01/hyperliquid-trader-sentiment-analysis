# Hyperliquid Trader Performance vs Bitcoin Market Sentiment

## Project Overview

This project analyzes the relationship between trader performance on Hyperliquid and Bitcoin market sentiment using the Bitcoin Fear & Greed Index.

The objective is to identify patterns between market psychology and trading performance and derive insights that can support smarter trading strategies.

---

## Datasets

### Historical Trader Data

Contains historical trades executed on Hyperliquid.

Columns include:

- account
- coin
- execution_price
- size_usd
- direction
- closed_pnl
- fee
- timestamp

### Bitcoin Fear & Greed Index

Contains daily Bitcoin market sentiment.

Columns include:

- date
- value
- classification

---

## Project Workflow

1. Load datasets
2. Clean and preprocess data
3. Merge datasets using date
4. Perform exploratory data analysis
5. Compute statistical summaries
6. Generate business insights and recommendations

---

## Project Structure

```
Hyperliquid-Sentiment-Analysis/

│── data/
│── notebooks/
│── src/
│── reports/
│── README.md
│── requirements.txt
│── main.py
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Key Findings

- Trading activity is concentrated during Fear market conditions.
- HYPE is the most frequently traded asset.
- Trader profitability varies across market sentiment categories.
- Long positions dominate trading activity.
- Trade size and transaction fees are highly skewed.

---

## Future Improvements

- Include Bitcoin price data.
- Include volatility indicators.
- Apply machine learning models.
- Perform predictive sentiment analysis.