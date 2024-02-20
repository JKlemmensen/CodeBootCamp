import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import linregress


    # Read data from file

df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

fig = plt.figure(figsize = (12,4))
sns.lineplot(data = df, x = 'Year', y='CSIRO Adjusted Sea Level', label='Sea Level').set(title='Rise in Sea Level')
sns.lineplot(data = df, x = 'Year', y='Lower Error Bound', color='tab:blue', alpha=0.1)
sns.lineplot(data = df, x = 'Year', y='Upper Error Bound', color='tab:blue', alpha=0.1)
plt.fill_between(df['Year'], df['Lower Error Bound'], df['Upper Error Bound'], color='blue', alpha=.2)
plt.ylabel('Sea Level [inches]')
sns.set_theme(palette = 'deep')
plt.tight_layout()
#plt.show()


    # Create first line of best fit

res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
Years = np.arange(1880,2051)
Best_fit1 = Years*res.slope + res.intercept

sns.lineplot(x= Years,y=Best_fit1, color = 'red',label='Bestfit2')
#plt.show()

    # Create second line of best fit

Years2 = np.arange(2000,2051)
res2 = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
Best_fit2 = Years2*res2.slope + res2.intercept

    # Add labels and title
sns.lineplot(x= Years2,y=Best_fit2, color = 'green', label='Bestfit2')
plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)