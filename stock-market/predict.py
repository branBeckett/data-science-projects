import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Read in the data
sphist = pd.read_csv('sphist.csv')

# Convert the date to a Pandas date type
sphist['Date'] = pd.to_datetime(sphist['Date'])

# Sort the dataframe on the 'Date' column
sphist.sort_values('Date', ascending=True, inplace=True)

# Creating a 5 day average price column
sphist['day_5'] = sphist['Close'].rolling(window=5).mean().shift(1, axis=0)

# Creating a 30 day average price column
sphist['day_30'] = sphist['Close'].rolling(window=30).mean().shift(1, axis=0)

# Creating a 365 day average price column
sphist['day_365'] = sphist['Close'].rolling(window=30).mean().shift(1, axis=0)

# Remove rows that fall before 1951-01-03
sphist_clean = sphist[sphist['Date'] > datetime(year=1951, month=1, day=3)]
sphist_clean.dropna(axis=0, inplace=True)

# Create training and test sets
train = sphist_clean[sphist_clean['Date'] < datetime(year=2013, month=1, day=1)]
test = sphist_clean[sphist_clean['Date'] >= datetime(year=2013, month=1, day=1)]

# Linear regression model with MSE and MAE metrics
cols = ['day_5', 'day_30', 'day_365']

lr = LinearRegression()
lr.fit(train[cols], train['Close'])
predictions = lr.predict(test[cols])

mae = mean_absolute_error(test['Close'], predictions)
mse = mean_squared_error(test['Close'], predictions)

print('MAE: ', mae)
print('MSE: ', mse)