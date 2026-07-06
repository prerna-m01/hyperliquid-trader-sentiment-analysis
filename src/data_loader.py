"""
Data Loader Module
Responsible only for reading datasets.
"""

import pandas as pd

def load_trading_data(file_path):
    df = pd.read_csv(file_path)
    print(f"Trading dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def load_sentiment_data(file_path):
    df = pd.read_csv(file_path)
    print(f"Sentiment dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df