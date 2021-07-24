# Script for 'swiss_residents' program in Python
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
The program parses a xlsx file containing the data of the swiss population over the years 1950-2019,
and then produces bar plots of the results.

The initial file 'su-e-01.01.01.xlsx' is taken from the Swiss Federal Statistical Office repository repository:
https://www.bfs.admin.ch/asset/en/su-e-01.01.01
"""

import matplotlib.pyplot as plt; plt.rcdefaults() 
import pandas as pd

# Opens the xlsx file 'su-e-01.01.01.xlsx' from the Swiss Federal Statistical Office repository;
# Puts its data in the dataframe df:
url = 'https://www.bfs.admin.ch/bfsstatic/dam/assets/17104142/master'
df = pd.read_csv(url, sep=';')

# Collects the data of the swiss, foreign, male and female populations:
swiss_population = df.loc[(df['SEX'] == 'T') & (df['CITIZENSHIP_CATEGORY'] == 'CH')]
foreign_population = df.loc[(df['SEX'] == 'T') & (df['CITIZENSHIP_CATEGORY'] == 'F')]
male_population = df.loc[(df['SEX'] == 'M') & (df['CITIZENSHIP_CATEGORY'] == 'T')]
female_population = df.loc[(df['SEX'] == 'F') & (df['CITIZENSHIP_CATEGORY'] == 'T')]

years = swiss_population['YEAR']
males = male_population['VALUE']
females = female_population['VALUE']
swiss = swiss_population['VALUE']
foreign = foreign_population['VALUE']

# Creates a multiple plot figure;
# Fixes the width of the bars (1 = maximal width);
# Creates the bar charts;
# Defines the titles and legend;
# Plots the resulting figure;
fig, ax = plt.subplots()
width = 0.35

ax.bar(years, males, width, color='darkblue', label='Male')
ax.bar(years+width, females, width, color='dodgerblue', label='Female')

plt.title('Number of male/female residents in Switzerland (years 1950-2019)', fontsize=13)
plt.xlabel('year', fontsize=13)
plt.ylabel('number', fontsize=13)
ax.legend()

plt.tight_layout()
plt.show()

# Fixes a new width of the bars (1 = maximal width);
# Creates a second bar chart;
# Defines the titles and legend;
# Plots the resulting figure:
width_bis = 0.5

p1 = plt.bar(years, swiss, width_bis, color='royalblue', label='Swiss')
p2 = plt.bar(years, foreign, width_bis, color='lightskyblue', bottom=swiss, label='Foreign')

plt.title('Number of swiss/foreign residents in Switzerland (years 1950-2019)', fontsize=13)
plt.xlabel('year', fontsize=13)
plt.ylabel('number', fontsize=13)
plt.legend()

plt.tight_layout()
plt.show()

