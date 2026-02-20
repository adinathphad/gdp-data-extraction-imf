# GDP Data Extraction Project
# Top 10 Largest Economies (IMF Data)

import pandas as pd
import numpy as np
import os

# Step 1: Define URL
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Step 2: Extract tables from webpage
tables = pd.read_html(URL)

# Step 3: Select IMF table (index 3)
df = tables[3]

# Step 4: Clean structure
df.columns = range(df.shape[1])
df = df[[0, 2]]
df = df.iloc[1:11, :]
df.columns = ['Country', 'GDP (Million USD)']

# Step 5: Convert to numeric (safe conversion)
df['GDP (Million USD)'] = pd.to_numeric(df['GDP (Million USD)'], errors='coerce')

# Step 6: Convert Million USD to Billion USD
df['GDP (Billion USD)'] = df['GDP (Million USD)'] / 1000

# Step 7: Round to 2 decimal places
df['GDP (Billion USD)'] = np.round(df['GDP (Billion USD)'], 2)

# Step 8: Drop old column
df = df.drop(columns=['GDP (Million USD)'])

# Step 9: Create data folder if not exists
os.makedirs("../data", exist_ok=True)

# Step 10: Save CSV
df.to_csv("../data/Top_10_Economies.csv", index=False)

print("Project Completed Successfully!")
df
