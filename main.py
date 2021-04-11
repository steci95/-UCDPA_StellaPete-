# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Year data
vg_year = vg.dropna(subset=['Year_of_Release'])
year_chart = sns.displot(vg_year['Year_of_Release'], bins = 30)
year_chart.set(xlabel='Year of Release', ylabel='Number of Games')
plt.show()

# Genre data
vg['Total_Sales'] = vg['NA_Sales'] + vg['EU_Sales'] + vg['JP_Sales'] + vg['Other_Sales']
vg_genre = vg.groupby('Genre')['Total_Sales'].sum()
print(vg_genre)





