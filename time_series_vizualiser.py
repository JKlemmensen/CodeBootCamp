import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date',parse_dates = True)
# Clean data
df = df[(df <= df.quantile(0.975)) &  (df >= df.quantile(0.025))]
#plt.figure(figsize=(15, 5)) 
#plt.title('Daily FreeCodeCamp Forum Page Views 5/2016-12/2019')
#sns.lineplot(df,x = 'date', y = 'value', color = 'red', linewidth=1)
#plt.xlabel('Date')
#plt.ylabel('Page Views')
#plt.show()

#def draw_line_plot():
    # Draw line plot




    # Save image and return fig (don't change this part)
 #   fig.savefig('line_plot.png')
#    return fig

#def draw_bar_plot():
    # Copy and modify data for monthly bar plot
 #   df_bar = None

    # Draw bar plot

resample_df = df.resample('M').mean()

monthly_averages = pd.DataFrame({
    'Year': resample_df.index.year,
    'Month': resample_df.index.month,
    'Average Page Views': resample_df['value']
}).reset_index(drop=True)
monthly_averages['Month'] = df.resample('M').mean().reset_index()['date'].dt.month_name().str.slice(stop=3)
print(monthly_averages)

month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#plt.figure(figsize=(10, 8))
sns.set(color_codes=True)
#sns.barplot(x='Year', y = 'Average Page Views', hue='Month', data=monthly_averages,hue_order=month_order)
#sns.color_palette("tab10")
#plt.show()

#print(monthly_avg_df)





    # Save image and return fig (don't change this part)
#    fig.savefig('bar_plot.png')
#    return fig

#def draw_box_plot():
    # Prepare data for box plots (this part is done!)
 #   df_box = df.copy()
 #   df_box.reset_index(inplace=True)
 #   df_box['year'] = [d.year for d in df_box.date]
 #   df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

print(monthly_averages)
sns.set()
fig, axes = plt.subplots(1, 2, figsize = (12,5))
sns.boxplot(data = monthly_averages, x = 'Year', y ='Average Page Views', ax = axes[0],palette='Set1')
axes[0].set_title('Boxplot by Year')
sns.boxplot(x = monthly_averages['Month'], y = monthly_averages['Average Page Views'], ax = axes[1], order=month_order,palette='Set1')
axes[1].set_title('Boxplot by Month')
plt.tight_layout()
plt.show()



    # Save image and return fig (don't change this part)
#    fig.savefig('box_plot.png')
#    return fig
