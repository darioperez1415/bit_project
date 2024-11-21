#data

import pandas as pd
import os
import matplotlib.pyplot as plt

# Assuming all CSVs are in the 'data' directory
data_dir = '/Users/darioperez/Documents/School/MSDS-570-01 - Fall 2024 Visual & Unstruct Data Analysi/Exercises/bit_project/bit_project/archive/'
currency_files = os.listdir(data_dir)

# Filter out non-CSV files and initialize the dictionary
currency_data = {}
for file in currency_files:
    if file.endswith('.csv'):
        currency_name = file[:-4]  # Remove '.csv' from the filename to use as the key
        currency_data[currency_name] = pd.read_csv(os.path.join(data_dir, file))

# Example using Bitcoin data
btc_data = currency_data['BTC']

# Plotting closing prices
plt.figure(figsize=(10, 5))
plt.plot(btc_data['date'], btc_data['close'])
plt.title('Bitcoin Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()

# Display summary statistics
print(btc_data.describe())

# Correlation matrix
correlation_matrix = btc_data[['open', 'high', 'low', 'close', 'volume']].corr()
print(correlation_matrix)


