import matplotlib
from jedi.api.refactoring import inline

from helper import *


# Project showing the prison break attempts all around the world
# We want to answer 2 questions:
    # 1. In what year was there the most prison break attempts?
    # 2. In which country was there the most attempts?


# Getting data from Wikipedia
article_url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(article_url)

# Validate the data is correct
# for row in data[0:3]:
#     print(row)

# Removing the last column of data list
index = 0
for row in data:
    data[index] = row[:-1]
    index += 1

# Converting date to only year
for row in data:
    row[0] = fetch_year(row[0])
    print(row)

# Getting earliest and latest year from data
min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]

# Building a list of all the years from min_year to max_year
years = []
for y in range(min_year, max_year + 1):
    years.append(y)

# Building a list of lists attempts_per_year containing [year, number of attempts]
attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])
for row in data:
    for year in attempts_per_year:
        if row[0] == year[0]:
            year[1] += 1
print(f"attempts_per_year {attempts_per_year}")

# Displaying on bar plots graph
barplot(attempts_per_year)