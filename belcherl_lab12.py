# pip --version = pip 25.3 
# 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# References
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 
# Python CSV files - with PANDAS by John Watson Rooney
# https://www.youtube.com/watch?v=ClNP-lTzKgI 
# 
# Complete Python Pandas Data Science Tutorial! (Reading CSV/Excel files, Sorting, Filtering, Groupby) by Keith Galli
# https://www.youtube.com/watch?v=vmEHCJofslg
#
# Damian Lillard Stats in CSV file via https://www.basketball-reference.com/players/l/lillada01.html 
# 
# Advanced Stat Equations https://www.fromtherumbleseat.com/pages/advanced-basketball-statistics-formula-sheet
#
# Pandas documentation https://pandas.pydata.org/docs/index.html 
#
# Other tutorials I used:
# https://www.slingacademy.com/article/pandas-insert-a-row-to-a-specific-position-in-a-dataframe/
# https://www.geeksforgeeks.org/python/python-delete-rows-columns-from-dataframe-using-pandas-drop/ 

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 1. Reading the CSV as a DataFrame
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Importing pandas and naming it pd, which is conventional
import pandas as pd

# This uses the read_csv method in pandas. read_ works with several files types. The csv file contains stats for basketball player, Damian lillard.
df = pd.read_csv('dame_stats.csv')

# This prints the columns of the csv which shows me what names I can use in the next command.
print(df.columns)

# This line uses df[x][r], where df is the imported stats, x is a list containing the columns of stats of interest, and r is a range of rows to display.
# I am displaying select stats from a time period of interest. This can be useful for making calulations or just highlighting specific data for analysis. 
print(df[['Season','PTS', '3P%','AST', 'TOV']][4:10])

# +++++++++++++++++++++++++++++++++++++++++++++++++++
# Manipulating information in a CSV
# +++++++++++++++++++++++++++++++++++++++++++++++++++

# The stat FT can be divided by FGA to get the advanced NBA  statistic "Free Throw Rate" (FTR).
# This code takes the value in the FT column and divides it by corresponding value in the FGA column, which makes a column 
df['FTR'] = df['FT'] / df['FGA']

# This shows the addition of the new column
print(df.columns)
print(df.head())

# .drop is used to remove information. In this case I am removing the colums for FT, FGA, and FTR. I am assigning the changed data to a new variable. 
new_df = df.drop(columns=['FTR', 'FT', 'FGA'])

# Printing the names of columns to show what's changed.
print(new_df.columns)

# using .sort to sort the list. I use 'by =' and select a column name to sort by that column. Storing in a new variable.
df2 = new_df.sort_values(by = 'AST')

# Showing the sorted dataframe
print(df2.head())

# This uploads the selected dataframe, df2, to a designated CSV. The 'to_ ' method also works with other file formats
df2.to_csv('dame_stats_copy.csv')

# Data frames can be lists of dictionaries or dictionaries of lists. I made a short, two coulmn dictionary made of lists to add to a dataframe
new_row = {
    'Season': ['2025-2026'],
    'PTS' : [55.0]
    }

# The .DataFrame method converts a specified object to a dataframe. 
new_row = pd.DataFrame(new_row)

# .iloc allows me to select a specific section of a dataframe based on the index values. This is part of adding a row.
# To insert a row of data in the middle of a CSV I split the index into two parts: before and after the index I want to place my new row.
# I want my new row to be at index 13, I set the before value as 12, and the after value as the original index 13.
df3 = new_df.iloc[:12]
df4 = new_df.iloc[13:]

# .concat concatentates the three dataframes into one data frame.
# .reset_index() copies the index values of the data fram and then renumbers them, otherwise we would see incorrect index values.
# drop=True takes the original index column and removes it, leaving only the current, accurate index column.
df_final = pd.concat([df3, new_row, df4]).reset_index(drop=True)

# Uploads new dataframe to a different csv, thsi could also be uploaded to the original but I wanted it to upload to a test sheet to make the work processes easier.
df_final.to_csv('test3.csv')
