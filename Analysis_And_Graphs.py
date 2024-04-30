import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

# Load the dataset
data = pd.read_csv('data_pricestats_bpp_series.csv') 
data['date'] = pd.to_datetime(data['date'], format='%d%b%Y')

# Filter data for China and Japan
china_data = data[data['country'] == 'CHINA_S']
japan_data = data[data['country'] == 'JAPAN']

# Group by date and calculate mean of annualCPI for smoother data
china_monthly_cpi = china_data.groupby('date')['annualCPI'].mean()
japan_monthly_cpi = japan_data.groupby('date')['annualCPI'].mean()

# Plotting the CPI data
plt.figure(figsize=(14, 7))
plt.plot(china_monthly_cpi, label='China', marker='o')
plt.plot(japan_monthly_cpi, label='Japan', marker='x')
plt.title('Comparative Analysis of Annual CPI: China vs Japan')
plt.xlabel('Date')
plt.ylabel('Annual CPI')
plt.legend()
plt.grid(True)
plt.savefig('cpi_comparison_plot.png')  # Save the plot

# Save the decomposed plot for China
fig, axes = plt.subplots(ncols=1, nrows=4, sharex=True, figsize=(10, 8))
decompose_china.observed.plot(ax=axes[0], title='China Observed')
decompose_china.trend.plot(ax=axes[1], title='China Trend')
decompose_china.seasonal.plot(ax=axes[2], title='China Seasonality')
decompose_china.resid.plot(ax=axes[3], title='China Residuals')
plt.tight_layout()
china_decomposed_plot_path = '/mnt/data/china_decomposed_plot.png'
fig.savefig(china_decomposed_plot_path)

# Save the decomposed plot for Japan
fig, axes = plt.subplots(ncols=1, nrows=4, sharex=True, figsize=(10, 8))
decompose_japan.observed.plot(ax=axes[0], title='Japan Observed')
decompose_japan.trend.plot(ax=axes[1], title='Japan Trend')
decompose_japan.seasonal.plot(ax=axes[2], title='Japan Seasonality')
decompose_japan.resid.plot(ax=axes[3], title='Japan Residuals')
plt.tight_layout()
japan_decomposed_plot_path = '/mnt/data/japan_decomposed_plot.png'
fig.savefig(japan_decomposed_plot_path)

# Decomposing the time series
china_monthly_resampled = china_monthly_cpi.resample('M').mean().dropna()
japan_monthly_resampled = japan_monthly_cpi.resample('M').mean().dropna()

decompose_china = seasonal_decompose(china_monthly_resampled, model='additive')
decompose_japan = seasonal_decompose(japan_monthly_resampled, model='additive')

# Function to perform ADF test
def adf_test(series, title=''):
    result = adfuller(series.dropna())
    print(f'ADF Statistic for {title}: {result[0]}')
    print(f'p-value: {result[1]}')
    for key, value in result[4].items():
        print(f'\t{key}: {value}')

# ADF test
adf_test(china_monthly_resampled, 'China')
adf_test(japan_monthly_resampled, 'Japan')
