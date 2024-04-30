import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV data into pandas DataFrames
china_data_path = './china_data.csv'
japan_data_path = './japan_data.csv'

china_data = pd.read_csv(china_data_path)
japan_data = pd.read_csv(japan_data_path)

# Step 2: Convert 'date' columns to datetime format for proper time-series plotting
china_data['date'] = pd.to_datetime(china_data['date'])
japan_data['date'] = pd.to_datetime(japan_data['date'])

# Step 3: Handling missing values if necessary
china_data.fillna(method='ffill', inplace=True)  # Forward fill to propagate last valid observation
japan_data.fillna(method='ffill', inplace=True)  # Forward fill

# Step 4: Create the plot
plt.figure(figsize=(12, 6))
plt.plot(china_data['date'], china_data['annualCPI'], label='China CPI Inflation Rate', marker='o', linestyle='-')
plt.plot(china_data['date'], china_data['annualPS'], label='China PriceStats Inflation Rate', marker='x', linestyle='--')
plt.plot(japan_data['date'], japan_data['annualCPI'], label='Japan CPI Inflation Rate', marker='o', linestyle='-')
plt.plot(japan_data['date'], japan_data['annualPS'], label='Japan PriceStats Inflation Rate', marker='x', linestyle='--')
plt.title('Inflation Trends in China vs Japan (2007-2015)')
plt.xlabel('Year')
plt.ylabel('Annual Inflation Rate (%)')
plt.legend()
plt.grid(True)

# Step 5: Save the plot as a PNG file
image_path = "./china_japan_inflation_trends.png"
plt.savefig(image_path)
