import pandas as pd


def standardize_columns(df):
    """Convert column names to lowercase with underscores."""

    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("-", "_")

    return df


def dataset_summary(df, dataset_name):
    """Display basic dataset information."""

    print(f"\n{'=' * 60}")
    print(dataset_name)
    print(f"{'=' * 60}")

    print(f"Shape           : {df.shape}")
    print(f"Rows            : {df.shape[0]}")
    print(f"Columns         : {df.shape[1]}")
    print(f"Duplicate Rows  : {df.duplicated().sum()}")

    print("\nMissing Values")
    print(df.isnull().sum())


def check_datatypes(df):
    """Display data types."""

    print("\nData Types")
    print(df.dtypes)


def remove_duplicates(df):
    """Remove duplicate rows."""

    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df


def convert_timestamp(df, column_name, unit):
    """Convert Unix timestamp into datetime."""

    df[column_name] = pd.to_datetime(df[column_name], unit=unit)

    return df


def add_date_column(df, timestamp_column):
    """Create date column from timestamp."""

    df["date"] = df[timestamp_column].dt.date

    return df


def convert_numeric(df, columns):
    """Convert selected columns into numeric."""

    for column in columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


def data_quality_report(df):
    """Generate a data quality report."""

    report = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.values,
        "Missing Values": df.isnull().sum().values,
        "Missing %": ((df.isnull().sum()/len(df))*100).round(2).values,
        "Unique Values": df.nunique().values
    })

    return report