import pandas as pd


def sentiment_statistics(df):
    """Summary statistics grouped by market sentiment."""

    summary = (
        df.groupby("classification")
        .agg(
            Trades=("closed_pnl", "count"),
            Average_PnL=("closed_pnl", "mean"),
            Median_PnL=("closed_pnl", "median"),
            Total_PnL=("closed_pnl", "sum"),
            Average_Trade_Size=("size_usd", "mean"),
            Average_Fee=("fee", "mean")
        )
        .round(2)
        .sort_values("Average_PnL", ascending=False)
    )

    return summary


def win_rate_by_sentiment(df):
    """Calculate win rate for each sentiment."""

    temp = df.copy()

    temp["winning_trade"] = temp["closed_pnl"] > 0

    win_rate = (
        temp.groupby("classification")["winning_trade"]
        .mean()
        .mul(100)
        .round(2)
        .rename("Win Rate (%)")
    )

    return win_rate.reset_index()


def direction_statistics(df):
    """Statistics grouped by trading direction."""

    summary = (
        df.groupby("direction")
        .agg(
            Trades=("closed_pnl", "count"),
            Average_PnL=("closed_pnl", "mean"),
            Total_PnL=("closed_pnl", "sum")
        )
        .round(2)
    )

    return summary.sort_values("Average_PnL", ascending=False)


def coin_statistics(df, top_n=10):
    """Top coins ranked by total profit."""

    summary = (
        df.groupby("coin")
        .agg(
            Trades=("closed_pnl", "count"),
            Total_PnL=("closed_pnl", "sum"),
            Average_PnL=("closed_pnl", "mean")
        )
        .round(2)
        .sort_values("Total_PnL", ascending=False)
        .head(top_n)
    )

    return summary


def top_traders(df, top_n=10):
    """Top profitable traders."""

    summary = (
        df.groupby("account")
        .agg(
            Trades=("closed_pnl", "count"),
            Total_PnL=("closed_pnl", "sum"),
            Average_PnL=("closed_pnl", "mean")
        )
        .round(2)
        .sort_values("Total_PnL", ascending=False)
        .head(top_n)
    )

    return summary