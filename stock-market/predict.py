import pandas as pd
from datetime import datetime

sphist = pd.read_csv('sphist.csv')

sphist['Date'] = sphist['Date'].to_datetime

sphist['Date'] = sphist[sphist['Date'] > datetime(year=2015, month=4, day=1)]

sphist['Date'].sort_values()