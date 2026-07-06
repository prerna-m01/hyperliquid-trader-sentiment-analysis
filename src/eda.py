import matplotlib.pyplot as plt
import pandas as pd


def sentiment_distribution(df):
    """Plot market sentiment distribution."""

    sentiment_counts = df["classification"].value_counts()

    plt.figure(figsize=(8,5))
    sentiment_counts.plot(kind="bar")

    plt.title("Market Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Trades")

    plt.tight_layout()
    plt.show()


def top_traded_coins(df, top_n=10):
    """Plot top traded coins."""

    coin_counts = df["coin"].value_counts().head(top_n)

    plt.figure(figsize=(10,5))
    coin_counts.plot(kind="bar")

    plt.title(f"Top {top_n} Traded Coins")
    plt.xlabel("Coin")
    plt.ylabel("Trades")

    plt.tight_layout()
    plt.show()


def pnl_by_sentiment(df):
    """Average Closed PnL by market sentiment."""

    pnl = (
        df.groupby("classification")["closed_pnl"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(8,5))
    pnl.plot(kind="bar")

    plt.title("Average Closed PnL by Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Average Closed PnL")

    plt.tight_layout()
    plt.show()


def direction_distribution(df):
    """Trading direction distribution."""

    direction = df["direction"].value_counts()

    plt.figure(figsize=(6,5))
    direction.plot(kind="bar")

    plt.title("Trading Direction")
    plt.xlabel("Direction")
    plt.ylabel("Trades")

    plt.tight_layout()
    plt.show()


def pnl_by_direction(df):
    """Average PnL by direction."""

    pnl = df.groupby("direction")["closed_pnl"].mean()

    plt.figure(figsize=(6,5))
    pnl.plot(kind="bar")

    plt.title("Average Closed PnL by Direction")
    plt.xlabel("Direction")
    plt.ylabel("Average Closed PnL")

    plt.tight_layout()
    plt.show()


def trade_size_distribution(df):
    """Distribution of trade sizes."""

    plt.figure(figsize=(8,5))

    plt.hist(df["size_usd"], bins=40)

    plt.title("Trade Size Distribution (USD)")
    plt.xlabel("Trade Size")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


def fee_distribution(df):
    """Distribution of fees."""

    plt.figure(figsize=(8,5))

    plt.hist(df["fee"], bins=40)

    plt.title("Fee Distribution")
    plt.xlabel("Fee")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

def boxplot_trade_size(df):
    """Boxplot for trade size."""

    plt.figure(figsize=(8,5))

    plt.boxplot(df["size_usd"].dropna(), vert=False)

    plt.title("Boxplot of Trade Size (USD)")
    plt.xlabel("Trade Size (USD)")

    plt.tight_layout()
    plt.show()


def boxplot_fee(df):
    """Boxplot for trading fee."""

    plt.figure(figsize=(8,5))

    plt.boxplot(df["fee"].dropna(), vert=False)

    plt.title("Boxplot of Trading Fee")
    plt.xlabel("Fee")

    plt.tight_layout()
    plt.show()


def boxplot_closed_pnl(df):
    """Boxplot for Closed PnL."""

    plt.figure(figsize=(8,5))

    plt.boxplot(df["closed_pnl"].dropna(), vert=False)

    plt.title("Boxplot of Closed PnL")
    plt.xlabel("Closed PnL")

    plt.tight_layout()
    plt.show()