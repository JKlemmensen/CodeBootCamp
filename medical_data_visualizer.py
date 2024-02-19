import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

#df.info()

# Add 'overweight' column
df['overweight'] = (df['weight']/(df['height']/100)**2 > 25).astype(int)
#print(df['overweight'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['gluc'] = (df['gluc'] > 1).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)


# Draw Categorical Plot
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
selected_columns = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']

# Create a DataFrame for cat plot using pd.melt
df_cat = pd.melt(df, id_vars='cardio', value_vars=selected_columns, var_name='Metric', value_name='total')

# Display the melted DataFrame
#sns.countplot(x='cardio', hue='Metric', data=df_cat)
#plt.show()


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
df_cat = None
    


    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
fig = None


    # Do not modify the next two lines
#fig.savefig('catplot.png')


# Draw Heat Map

    # Clean the data

df = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025))]

correlation_matrix = df.corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
plt.figure(figsize=(10, 8)) 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, mask = mask)
plt.title('Correlation Matrix')
plt.show()


# Create a heatmap using Seaborn


    # Set up the matplotlib figure
#fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
#fig.savefig('heatmap.png')