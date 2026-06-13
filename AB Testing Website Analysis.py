
# A/B TESTING WEBSITE ANALYSIS

# 1. IMPORT LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime as dt
from scipy.stats import ttest_ind as tt
from statsmodels.stats.proportion import proportions_ztest as zt

# 2. LOAD DATASET

df = pd.read_csv(
    r'C:\Users\garre\Downloads\DA Projects\Python Project - GP\AB Testing Data.csv'
)

# 3. INITIAL DATA EXPLORATION

# Preview dataset
print('DATASET PREVIEW\n', df.head(), '\n')

# Dataset information
print('DATASET INFO')
df.info() 

# Column names
print('\nCOLUMN NAMES\n', df.columns, '\n')

# Data types
print('DATA TYPES\n', df.dtypes, '\n')

# Convert timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 4. DATA CLEANING

# Check for null values
print('NULL VALUES BY COLUMN\n', df.isnull().sum(), '\n')

# Check duplicate rows
print('DUPLICATE ROWS\n', df.duplicated().sum(), '\n')

# 5. EXPLORATORY DATA ANALYSIS (EDA)

# Group distribution
print('GROUP COUNTS\n', df['group'].value_counts(), '\n')

# Conversion totals by group
conversion_sum = df.groupby('group')['converted'].sum()

print('TOTAL CONVERSIONS BY GROUP\n', conversion_sum, '\n')

# Conversion rates by group
conversion_mean = df.groupby('group')['converted'].mean()

print('CONVERSION RATE BY GROUP\n', conversion_mean, '\n')

# 6. CONVERSION RATE VISUALIZATION

conversion_mean.plot(kind='bar')

plt.title('Conversion Rate by Group')
plt.xlabel('Group')
plt.ylabel('Conversion Rate')

plt.xticks(rotation=0)

plt.savefig('visuals/conversions_by_group.png')

plt.show()

# 7. WEEKDAY CONVERSION ANALYSIS

days_order = [
    'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday', 'Sunday'
]

df['weekday'] = df['timestamp'].dt.day_name()

weekday_conversion = (
    df.groupby('weekday')['converted']
    .mean()
    .reindex(days_order)
)

print('CONVERSION RATE BY WEEKDAY\n', weekday_conversion, '\n')

weekday_conversion.plot(kind='bar')

plt.title('Conversion Rate by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Conversion Rate')

plt.xticks(rotation=0)

plt.savefig('visuals/weekday_conversion.png')

plt.show()

# 8. MONTHLY CONVERSION TREND ANALYSIS

months_order = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

df['month'] = df['timestamp'].dt.month_name()

monthly_conversion = (
    df.groupby('month')['converted']
    .mean()
    .reindex(months_order)
)

print('MONTHLY CONVERSION RATE\n', monthly_conversion, '\n')

monthly_conversion.plot()

plt.title('Monthly Conversion Trend')
plt.xlabel('Month')
plt.ylabel('Conversion Rate')

plt.xticks(rotation=0)

plt.savefig('visuals/monthly_conversion_trend.png')

plt.show()

# 9. A/B HYPOTHESIS TESTING (Z-TEST)

# Filter conversion data by group
control = df[df['group'] == 'control']['converted']

treatment = df[df['group'] == 'treatment']['converted']

# Total conversions
successes = [
    control.sum(),
    treatment.sum()
]

# Total observations
observations = [
    len(control),
    len(treatment)
]

# Perform z-test
z_stat, p_value = zt(successes, observations)

print('Z-STATISTIC:', z_stat)
print('P-VALUE:', p_value, '\n')

# 10. RELATIVE LIFT ANALYSIS

old_pg_rate = 0.118726
new_pg_rate = 0.179489

rel_lift = (
    (new_pg_rate - old_pg_rate)
    / old_pg_rate
) * 100

print('RELATIVE LIFT (%):', rel_lift, '\n')

# 11. LOCATION ANALYSIS

# Conversion totals by location
conversion_location = (
    df.groupby('location')['converted']
    .sum()
)

# Conversion rate by location
conversion_loc_mean = (
    df.groupby('location')['converted']
    .mean()
)

print(
    'CONVERSION RATE BY LOCATION\n',
    conversion_loc_mean.sort_values(ascending=False),
    '\n'
)

print(
    'TOTAL CONVERSIONS BY LOCATION\n',
    conversion_location.sort_values(ascending=False),
    '\n'
)

# 12. DEVICE TYPE ANALYSIS

# Conversion totals by device
device_conv_tot = (
    df.groupby(['device_type', 'group'])['converted']
    .sum()
)

# Conversion rates by device
device_conv_rate = (
    df.groupby(['device_type', 'group'])['converted']
    .mean()
)

print(
    'CONVERSION TOTAL BY DEVICE\n',
    device_conv_tot,
    '\n'
)

print(
    'CONVERSION RATE BY DEVICE\n',
    device_conv_rate,
    '\n'
)

# 13. PURCHASE AMOUNT ANALYSIS

# Average purchase amount by group
print(
    'AVERAGE PURCHASE AMOUNT BY GROUP\n',
    df.groupby('group')['purchase_amount'].mean(),
    '\n'
)

# Total purchase amount by location
loc_purch = (
    df.groupby('location')['purchase_amount']
    .sum()
)

print(
    'TOTAL PURCHASE AMOUNT BY LOCATION\n',
    loc_purch.sort_values(ascending=False),
    '\n'
)

# 14. HOURLY CONVERSION ANALYSIS

df['hour'] = df['timestamp'].dt.hour

hour_conversion = (
    df.groupby('hour')['converted']
    .mean()
)

print(
    'CONVERSION RATE BY HOUR\n',
    hour_conversion.sort_values(ascending=False),
    '\n'
)

# 15. YEARLY + MONTHLY TREND ANALYSIS

df['year'] = df['timestamp'].dt.year
df['month_num'] = df['timestamp'].dt.month

month_conversion = (
    df.groupby(
        ['year', 'month_num', 'month', 'group']
    )['converted']
    .mean()
    .reset_index()
)

print(
    'CONVERSION RATE BY YEAR AND MONTH\n',
    month_conversion.sort_values(
        by=['year', 'month_num']
    )
)
