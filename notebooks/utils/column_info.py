import pandas as pd

def get_column_info(df):
    """
    Generate a DataFrame with information about each column in the input DataFrame.

    Parameters:
    - df: pandas DataFrame

    Returns:
    - pandas DataFrame with columns: 'Column', 'Unique Values', 'Data Type', 'Missing Values', 'Example Values'
    """
    data = []
    for column in df.columns:
        unique_values = df[column].nunique()
        data_type = df[column].dtype
        missing_values = df[column].isnull().sum()
        example_values = df[column].dropna().unique()[:5]
        data.append({
            'Column': column,
            'Unique Values': unique_values,
            'Data Type': data_type,
            'Missing Values': missing_values,
            'Example Values': example_values
        })
    
    df_info = pd.DataFrame(data)
    return df_info