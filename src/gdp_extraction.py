import pandas as pd
import numpy as np


def extract_gdp_data():
    """
    Extracts the top 10 largest economies by GDP (Nominal)
    from IMF data available on Wikipedia (archived link).
    Returns a cleaned pandas DataFrame.
    """

    URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

    # Read tables from webpage
    tables = pd.read_html(URL)

    # IMF table (index 3 based on inspection)
    df = tables[3]

    # Reset column headers
    df.columns = range(df.shape[1])

    # Keep Country and IMF GDP column
    df = df[[0, 2]]

    # Keep top 10 economies
    df = df.iloc[1:11, :]

    # Rename columns
    df.columns = ['Country', 'GDP (Million USD)']

    # Clean GDP column
    df['GDP (Million USD)'] = df['GDP (Million USD)'].str.replace(',', '')
    df['GDP (Million USD)'] = pd.to_numeric(df['GDP (Million USD)'])

    # Convert Million to Billion
    df['GDP (Billion USD)'] = df['GDP (Million USD)'] / 1000

    # Round to 2 decimal places
    df['GDP (Billion USD)'] = np.round(df['GDP (Billion USD)'], 2)

    # Drop old column
    df = df.drop(columns=['GDP (Million USD)'])

    return df


if __name__ == "__main__":
    df = extract_gdp_data()
    df.to_csv("../data/Top_10_Economies.csv", index=False)
    print("CSV file successfully created!")
