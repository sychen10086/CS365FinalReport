import pandas as pd
import matplotlib.pyplot as plt

data_pricestats_bpp_series = pd.read_csv('data_pricestats_bpp_series.csv')
# Filter data for China and extract relevant columns for analysis
china_data = data_pricestats_bpp_series[data_pricestats_bpp_series['country'] == 'CHINA_S'][['date', 'annualCPI', 'annualPS']]

# Dropping rows with NaN values in the inflation rates for a cleaner analysis
china_data.dropna(subset=['annualCPI', 'annualPS'], inplace=True)

# Filter data for Japan and extract relevant columns for analysis
japan_data = data_pricestats_bpp_series[data_pricestats_bpp_series['country'] == 'JAPAN'][['date', 'annualCPI', 'annualPS']]

# Dropping rows with NaN values in the inflation rates for a cleaner analysis
japan_data.dropna(subset=['annualCPI', 'annualPS'], inplace=True)

# Create the plot
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

# Save the plot as a PNG file
image_path = "/mnt/data/china_japan_inflation_trends.png"
plt.savefig(image_path)
