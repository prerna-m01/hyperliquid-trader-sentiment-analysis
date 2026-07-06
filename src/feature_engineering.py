import numpy as np

def create_win_loss(df):

    df["trade_result"] = np.where(
        df["closedPnL"] > 0,
        "Win",
        "Loss"
    )

    return df