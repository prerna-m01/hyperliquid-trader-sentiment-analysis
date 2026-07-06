# Hyperliquid Trader Performance Analysis using Bitcoin Market Sentiment

## Overview

This project analyzes the relationship between **Bitcoin market sentiment** and **Hyperliquid trader performance** by combining historical trading data with the **Bitcoin Fear & Greed Index**.

The objective is to understand how market psychology influences trading behavior and profitability, while generating actionable insights that can contribute to smarter trading strategies.

The project follows a complete data analytics workflow including data preprocessing, exploratory data analysis (EDA), statistical analysis, and business insight generation.

---

## Problem Statement

Market sentiment is one of the major factors influencing cryptocurrency trading decisions. While the Bitcoin Fear & Greed Index captures overall market psychology, Hyperliquid provides detailed historical trading records.

This project investigates whether trader behavior and profitability change under different market sentiment conditions by answering questions such as:

- Does trader profitability vary across Fear, Neutral, and Greed markets?
- Which cryptocurrencies dominate trading activity?
- How do different trading directions perform?
- Which traders consistently generate higher profits?
- Can market sentiment provide useful context for trading decisions?

---

## Objectives

- Clean and preprocess multiple datasets.
- Merge trading data with the Bitcoin Fear & Greed Index.
- Perform exploratory data analysis.
- Compare trader performance across market sentiment categories.
- Generate statistical summaries and business insights.
- Recommend data-driven trading strategies.

---

## Dataset Description

### 1. Hyperliquid Historical Trading Dataset

Contains historical trade execution records.

Key columns include:

- Account
- Coin
- Execution Price
- Size (USD)
- Direction
- Closed PnL
- Fee
- Timestamp

---

### 2. Bitcoin Fear & Greed Index

Contains daily Bitcoin market sentiment.

Columns:

- Date
- Sentiment Score
- Market Sentiment Classification

---

## Project Workflow

```
Data Collection
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Dataset Merge
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Statistical Analysis
        │
        ▼
Business Insights
        │
        ▼
Recommendations
```

---

## Project Structure

```
hyperliquid-trader-sentiment-analysis/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_sentiment_analysis.ipynb
│
├── src/
│   ├── analysis.py
│   ├── config.py
│   ├── data_loader.py
│   ├── eda.py
│   ├── merge_data.py
│   └── preprocessing.py
│
├── README.md
├── requirements.txt
├── main.py
└── .gitignore
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Methodology

### Phase 1 — Data Loading

- Imported trading and sentiment datasets.
- Verified successful loading.

### Phase 2 — Data Cleaning

- Standardized column names.
- Converted timestamps into datetime.
- Removed duplicate records.
- Converted numerical columns.
- Created a common date column.

### Phase 3 — Data Integration

- Merged datasets using the date column.
- Validated merge quality.
- Removed records without matching sentiment for analysis.

### Phase 4 — Exploratory Data Analysis

Explored:

- Market sentiment distribution
- Top traded cryptocurrencies
- Trading directions
- Profitability across sentiment categories
- Trade size distribution
- Fee distribution

### Phase 5 — Statistical Analysis

Calculated:

- Average Closed PnL
- Median Closed PnL
- Total PnL
- Win Rate
- Performance by trading direction
- Coin-wise profitability
- Top performing trader accounts

---

## Key Findings

- Trading activity is concentrated during **Fear** market conditions.
- **HYPE** is the most actively traded cryptocurrency in the dataset.
- Long positions occur more frequently than short positions.
- Average trader profitability varies across different market sentiment categories.
- Trade sizes and transaction fees exhibit highly right-skewed distributions.
- A relatively small number of trader accounts contribute a significant share of total realized profits.

---

## Business Recommendations

Based on the analysis:

- Include Bitcoin market sentiment as an additional trading indicator.
- Combine sentiment analysis with technical indicators rather than relying on sentiment alone.
- Monitor trader behavior during Fear and Greed periods.
- Focus additional analysis on highly traded assets such as HYPE and BTC.
- Apply appropriate risk management during periods of extreme market sentiment.

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/prerna-m01/hyperliquid-trader-sentiment-analysis.git
```

### Navigate to the project

```bash
cd hyperliquid-trader-sentiment-analysis
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python main.py
```

### Open the notebook

```text
notebooks/01_sentiment_analysis.ipynb
```

Run all cells sequentially.

---

## Future Improvements

Future work could include:

- Integrating live Bitcoin price data.
- Adding market volatility indicators.
- Building predictive machine learning models.
- Performing time-series analysis.
- Developing an interactive dashboard using Streamlit or Power BI.

---

## Author

**Prerna Mishra**

GitHub: https://github.com/prerna-m01

LinkedIn: https://linkedin.com/in/prernamishra01