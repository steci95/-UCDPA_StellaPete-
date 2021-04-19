# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import column, row


# Import csv file
vg = pd.read_csv('Video_Games.csv')

# Look at dataset & summary - column names, null values, data types, min/max/mean stats
print(vg.info())
print(vg.head())

# Function to check number of row and columns.


def rc_myfunc():
    print("The dataset has " + str(vg.shape[0]) + " rows." + " And has " + str(vg.shape[1]) + " columns.")


print(rc_myfunc())


# Check nulls & remove or fill with other
print(vg.isna().any())
print(vg.isna().sum())
vg['Genre'].fillna('Unknown', inplace=True)
vg['Publisher'].fillna('Unknown', inplace=True)
vg.dropna(subset=['Name'], inplace=True)
cols = ['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']
vg.drop(cols, axis=1, inplace=True)
print(rc_myfunc())

# Set index column, look at head again and description to know mean, max & min data
print(vg.columns)
vg.set_index('Name', inplace=True)
print(vg.head())
print(vg.describe())

# Create countplot to look at number of games per platform
Platform_chart = sns.countplot(vg["Platform"])
Platform_chart.set_ylabel('Number of Games')
Platform_chart.set_title('Number of Games by Platform')
plt.xticks(rotation=90)
plt.show()
plt.close()

# Year data
vg_year = vg.dropna(subset=['Year_of_Release'])
year_chart = sns.displot(vg_year['Year_of_Release'], bins=30)
year_chart.set(xlabel='Year of Release', ylabel='Number of Games')
plt.show()
plt.close()

# Genre data
vg['Total_Sales'] = vg['NA_Sales'] + vg['EU_Sales'] + vg['JP_Sales'] + vg['Other_Sales']
vg_genre = vg.groupby('Genre')['Total_Sales'].sum()
vg_genre.sort_values(ascending=True, inplace=True)
vg_genre.plot.bar()
plt.title('Total Sales by Genre')
plt.xlabel('Game Genre')
plt.ylabel('Total Sales')
plt.show()

# Genre sales over the years using bokeh
plot = figure(x_axis_label='Year', y_axis_label='Total_Sales')


# Loop function to determine parts of sales
NA_Sales_Perc = []
for x in vg['NA_Sales']/vg['Total_Sales']:
    if x >= 0.75:
        NA_Sales_Perc.append('High')
    elif x <= 0.25:
        NA_Sales_Perc.append('Low')
    else:
        NA_Sales_Perc.append('Medium')

vg['NA_Sales_Perc'] = NA_Sales_Perc

EU_Sales_Perc = []
for x in vg['EU_Sales']/vg['Total_Sales']:
    if x >= 0.75:
        EU_Sales_Perc.append('High')
    elif x <= 0.25:
        EU_Sales_Perc.append('Low')
    else:
        EU_Sales_Perc.append('Medium')

vg['EU_Sales_Perc'] = EU_Sales_Perc

JP_Sales_Perc = []
for x in vg['JP_Sales']/vg['Total_Sales']:
    if x >= 0.75:
        JP_Sales_Perc.append('High')
    elif x <= 0.25:
        JP_Sales_Perc.append('Low')
    else:
        JP_Sales_Perc.append('Medium')

vg['JP_Sales_Perc'] = JP_Sales_Perc

Other_Sales_Perc = []
for x in vg['Other_Sales']/vg['Total_Sales']:
    if x >= 0.75:
        Other_Sales_Perc.append('High')
    elif x <= 0.25:
        Other_Sales_Perc.append('Low')
    else:
        Other_Sales_Perc.append('Medium')

vg['Other_Sales_Perc'] = Other_Sales_Perc
print(vg)
print(rc_myfunc())

# Looking at top 15 sellers
vg_total = vg.sort_values('Total_Sales', ascending=False)
vg_top_sellers = vg_total.iloc[0:15]
print(vg_top_sellers)

# Create the pandas DataFrame
vg_data = pd.DataFrame(vg_top_sellers, columns= ['NA_Sales_Perc', 'EU_Sales_Perc', 'JP_Sales_Perc', 'Other_Sales_Perc'])
print(vg_data)

# Custom heatmap creation
List1 = ['High', 'Medium', 'Low']
List2 = [1, 2, 3]
vg_data['NA_Sales_Perc'] = vg_data['NA_Sales_Perc'].replace(List1, List2)
vg_data['EU_Sales_Perc'] = vg_data['EU_Sales_Perc'].replace(List1, List2)
vg_data['JP_Sales_Perc'] = vg_data['JP_Sales_Perc'].replace(List1, List2)
vg_data['Other_Sales_Perc'] = vg_data['Other_Sales_Perc'].replace(List1, List2)
print(vg_data)
sns.heatmap(vg_data)
plt.show()