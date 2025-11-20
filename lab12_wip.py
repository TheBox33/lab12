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

# Importing pandas and naming it pd, which is conventional
import pandas as pd

# This uses the read_csv method in pandas. read_ works with several files types. The csv file contains stats for basketball player, Damian lillard.
df = pd.read_csv('dame_stats.csv')

# This prints the columns of the csv which shows me what names I can use in the next command.
print(df.columns)

# This line uses df[x][r], where df is the imported stats, x is a list containing the columns of stats of interest, and r is a range of rows to display.
# I am displaying select stats from a time period of interest. This can be useful for making calulations.
print(df[['Season','PTS', '3P%','AST', 'TOV']][4:10])