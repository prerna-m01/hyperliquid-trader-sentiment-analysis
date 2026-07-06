import pandas as pd


def check_date_range(df, dataset_name):
    """Display the minimum and maximum dates in the dataset."""

    print(f"\n{dataset_name}")
    print("-" * len(dataset_name))
    print(f"Start Date : {df['date'].min()}")
    print(f"End Date   : {df['date'].max()}")


def merge_datasets(trade_df, sentiment_df):
    """Merge trading data with sentiment data."""

    merged_df = pd.merge(
        trade_df,
        sentiment_df[["date", "classification", "value"]],
        on="date",
        how="left"
    )

    return merged_df


def check_merge_results(df):
    """Check merge quality."""

    print("\nMerged Dataset Shape:", df.shape)

    print("\nMissing Sentiment Values:")
    print(df["classification"].isnull().sum())

    print("\nSentiment Distribution:")
    print(df["classification"].value_counts(dropna=False))