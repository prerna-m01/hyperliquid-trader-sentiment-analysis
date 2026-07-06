from src.config import *
from src.data_loader import *
from src.preprocessing import *
from src.utils import print_heading


def main():

    print_heading("Loading Datasets")

    trade_df = load_trading_data(TRADING_DATA_PATH)
    sentiment_df = load_sentiment_data(SENTIMENT_DATA_PATH)

    trade_df = standardize_columns(trade_df)
    sentiment_df = standardize_columns(sentiment_df)

    print_heading("Trading Dataset Summary")
    dataset_summary(trade_df, "Trading Dataset")

    print_heading("Sentiment Dataset Summary")
    dataset_summary(sentiment_df, "Sentiment Dataset")


if __name__ == "__main__":
    main()