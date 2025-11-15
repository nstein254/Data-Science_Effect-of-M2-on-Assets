#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV with the correct separator
df = pd.read_csv('/Users/babo/Downloads/Data Science Project.csv', sep=';')

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Convert the S&P 500 price column to a proper numeric type:
# 1) Remove thousand separators (.)
# 2) Replace decimal commas with decimal points
# 3) Remove the dollar sign
df['S&P 500 Index'] = df['S&P 500 Index'].str.replace('$', '', regex=False)
df['S&P 500 Index'] = df['S&P 500 Index'].str.replace('.', '', regex=False)  # Remove thousands separator
df['S&P 500 Index'] = df['S&P 500 Index'].str.replace(',', '.', regex=False)  # Replace comma with point
df['S&P 500 Index'] = pd.to_numeric(df['S&P 500 Index'], errors='coerce')

# Remove any rows with NaN values
df = df.dropna(subset=['Date', 'S&P 500 Index'])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['S&P 500 Index'])
plt.xlabel('Date')
plt.ylabel('S&P 500 Index')
plt.title('S&P 500 Index Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# Load the CSV with the correct separator
df = pd.read_csv('/Users/babo/Downloads/Data Science Project.csv', sep=';')

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Convert the S&P 500 price column to a proper numeric type:
# 1) Remove thousand separators (.)
# 2) Replace decimal commas with decimal points
# 3) Remove the dollar sign
df['M2 Money Supply (Bn)'] = df['M2 Money Supply (Bn)'].str.replace('$', '', regex=False)
df['M2 Money Supply (Bn)'] = df['M2 Money Supply (Bn)'].str.replace('.', '', regex=False)  # Remove thousands separator
df['M2 Money Supply (Bn)'] = df['M2 Money Supply (Bn)'].str.replace(',', '.', regex=False)  # Replace comma with point
df['M2 Money Supply (Bn)'] = pd.to_numeric(df['M2 Money Supply (Bn)'], errors='coerce')

# Remove any rows with NaN values
df = df.dropna(subset=['Date', 'M2 Money Supply (Bn)'])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['M2 Money Supply (Bn)'])
plt.xlabel('Date')
plt.ylabel('M2 Money Supply (Bn) in $')
plt.title('M2 Money Supply (Bn) Over Time')
plt.xticks(rotation=45)

plt.gca().yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))

plt.tight_layout()
plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV with the correct separator
df = pd.read_csv('/Users/babo/Downloads/Data Science Project.csv', sep=';')

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Convert the S&P 500 price column to a proper numeric type:
# 1) Remove thousand separators (.)
# 2) Replace decimal commas with decimal points
# 3) Remove the dollar sign
df['US Dollar Index'] = df['US Dollar Index'].str.replace('$', '', regex=False)
df['US Dollar Index'] = df['US Dollar Index'].str.replace('.', '', regex=False)  # Remove thousands separator
df['US Dollar Index'] = df['US Dollar Index'].str.replace(',', '.', regex=False)  # Replace comma with point
df['US Dollar Index'] = pd.to_numeric(df['US Dollar Index'], errors='coerce')

# Remove any rows with NaN values
df = df.dropna(subset=['Date', 'US Dollar Index'])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['US Dollar Index'])
plt.xlabel('Date')
plt.ylabel('US Dollar Index')
plt.title('US Dollar Index Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Load the CSV with the correct separator
df = pd.read_csv('/Users/babo/Downloads/Data Science Project.csv', sep=';')

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Clean and convert the Federal Funds Effective Rate column
df['Federal Funds Effective Rate (DFF)'] = df['Federal Funds Effective Rate (DFF)'].str.replace('%', '', regex=False)
df['Federal Funds Effective Rate (DFF)'] = df['Federal Funds Effective Rate (DFF)'].str.replace('.', '', regex=False)  # Remove thousands separator
df['Federal Funds Effective Rate (DFF)'] = df['Federal Funds Effective Rate (DFF)'].str.replace(',', '.', regex=False)  # Replace comma with decimal point
df['Federal Funds Effective Rate (DFF)'] = pd.to_numeric(df['Federal Funds Effective Rate (DFF)'], errors='coerce')

# Remove rows with missing values
df = df.dropna(subset=['Date', 'Federal Funds Effective Rate (DFF)'])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Federal Funds Effective Rate (DFF)'])
plt.xlabel('Date')
plt.ylabel('Federal Funds Effective Rate (DFF) in %')
plt.title('Federal Funds Effective Rate (DFF)')
plt.xticks(rotation=45)

# Format Y-axis to show percentage values
plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=100))

plt.tight_layout()
plt.show()


# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# Load the CSV with the correct separator
df = pd.read_csv('/Users/babo/Downloads/Data Science Project.csv', sep=';')

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Convert the Gold Futures column to numeric:
df['Gold Futures'] = df['Gold Futures'].str.replace('$', '', regex=False)
df['Gold Futures'] = df['Gold Futures'].str.replace('.', '', regex=False)  # Remove thousands separator
df['Gold Futures'] = df['Gold Futures'].str.replace(',', '.', regex=False)  # Replace comma with decimal point
df['Gold Futures'] = pd.to_numeric(df['Gold Futures'], errors='coerce')

# Remove any rows with NaN values
df = df.dropna(subset=['Date', 'Gold Futures'])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Gold Futures'])
plt.xlabel('Date')
plt.ylabel('Gold Futures in $')
plt.title('Gold Futures')
plt.xticks(rotation=45)

# Format Y-axis with $ sign and commas
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))

plt.tight_layout()
plt.show()


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# Load the CSV with the correct separator
df = pd.read_csv('/Users/babo/Downloads/Data Science Project.csv', sep=';')

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Convert the S&P 500 price column to a proper numeric type:
# 1) Remove thousand separators (.)
# 2) Replace decimal commas with decimal points
# 3) Remove the dollar sign
df['Crude Oil Futures'] = df['Crude Oil Futures'].str.replace('$', '', regex=False)
df['Crude Oil Futures'] = df['Crude Oil Futures'].str.replace('.', '', regex=False)  # Remove thousands separator
df['Crude Oil Futures'] = df['Crude Oil Futures'].str.replace(',', '.', regex=False)  # Replace comma with point
df['Crude Oil Futures'] = pd.to_numeric(df['Crude Oil Futures'], errors='coerce')

# Remove any rows with NaN values
df = df.dropna(subset=['Date', 'Crude Oil Futures'])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Crude Oil Futures'])
plt.xlabel('Date')
plt.ylabel('Crude Oil Futures in $')
plt.title('Crude Oil Futures')
plt.xticks(rotation=45)

plt.gca().yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))

plt.tight_layout()
plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# --- Load (semicolon CSV with possible BOM) ---
path = "/Users/babo/Downloads/Data Science Project.csv"  # <- your path
df = pd.read_csv(path, sep=';', engine='python')

# --- Parse date (dd.mm.yyyy) ---
df['Date'] = pd.to_datetime(df['Date'], format="%d.%m.%Y", errors='coerce')

# --- Clean BTC/USD Index (European -> US numeric) ---
# e.g. "$110.671,50" -> "110671.50"
price = (
    df['BTC/USD Index']
      .astype(str)
      .str.replace('$', '', regex=False)
      .str.replace('.', '', regex=False)   # remove thousands separator
      .str.replace(',', '.', regex=False)  # decimal comma -> dot
)
df['BTC_USD_Index'] = pd.to_numeric(price, errors='coerce')

# --- Keep valid rows & sort ---
df = df.dropna(subset=['Date', 'BTC_USD_Index']).sort_values('Date')

# --- Plot ---
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['BTC_USD_Index'])
plt.xlabel('Date')
plt.ylabel('BTC/USD Index')
plt.title('BTC/USD Index (2010–2025)')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
plt.tight_layout()
plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV with the correct separator
df = pd.read_csv('/Users/babo/Downloads/Data Science Project.csv', sep=';')

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Convert the S&P 500 price column to a proper numeric type:
# 1) Remove thousand separators (.)
# 2) Replace decimal commas with decimal points
# 3) Remove the dollar sign
df['CBOE Volatility Index (VIX)'] = df['CBOE Volatility Index (VIX)'].str.replace('$', '', regex=False)
df['CBOE Volatility Index (VIX)'] = df['CBOE Volatility Index (VIX)'].str.replace('.', '', regex=False)  # Remove thousands separator
df['CBOE Volatility Index (VIX)'] = df['CBOE Volatility Index (VIX)'].str.replace(',', '.', regex=False)  # Replace comma with point
df['CBOE Volatility Index (VIX)'] = pd.to_numeric(df['CBOE Volatility Index (VIX)'], errors='coerce')

# Remove any rows with NaN values
df = df.dropna(subset=['Date', 'CBOE Volatility Index (VIX)'])

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['CBOE Volatility Index (VIX)'])
plt.xlabel('Date')
plt.ylabel('CBOE Volatility Index (VIX)')
plt.title('CBOE Volatility Index (VIX)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# --- Load (semicolon CSV with possible BOM) ---
path = "/Users/babo/Downloads/Data Science Project.csv"  # <- your path
df = pd.read_csv(path, sep=';', engine='python')

# --- Parse date (dd.mm.yyyy) ---
df['Date'] = pd.to_datetime(df['Date'], format="%d.%m.%Y", errors='coerce')

# --- Clean BTC/USD Index (European -> US numeric) ---
# e.g. "$110.671,50" -> "110671.50"
price = (
    df['BTC/USD Index']
      .astype(str)
      .str.replace('$', '', regex=False)
      .str.replace('.', '', regex=False)   # remove thousands separator
      .str.replace(',', '.', regex=False)  # decimal comma -> dot
)
df['BTC_USD_Index'] = pd.to_numeric(price, errors='coerce')

# --- Keep valid rows & sort ---
df = df.dropna(subset=['Date', 'BTC_USD_Index']).sort_values('Date')

# --- Plot ---
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['BTC_USD_Index'])
plt.xlabel('Date')
plt.ylabel('BTC/USD Index')
plt.title('BTC/USD Index (2010–2025)')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
plt.tight_layout()
plt.show()

# Quick sanity check
print("Date range:", df['Date'].min().date(), "→", df['Date'].max().date(),
      "| rows:", len(df))


# In[ ]:




