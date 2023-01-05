from helper import *

# 1. Import the data from Wikipedia
data_url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"
prison_break_data = data_from_url(data_url)
# for prison_break in prison_break_list[0:3]:
#     print(prison_break)


# 2. Getting rid of the description column
index = 0
for row in prison_break_data:
    prison_break_data[index] = row[:-1]
    index += 1

# 3. Extracting the year
for row in prison_break_data:
    row[0] = fetch_year(row[0])

# 4. Creating a list of pairs containing the year and the number of attempts
# The pairs in the list should look like [year, nb_of_attempts]

# 4.1 Getting the min_year and the max_year from prison_break_data
min_year = min(prison_break_data, key=lambda x: x[0])[0]
max_year = max(prison_break_data, key=lambda x: x[0])[0]

# 4.2 Creating a list with all the years between min_year and max_year
years = []
for y in range(min_year, max_year + 1):
    years.append(y)

# 4.3 Creating attempts_per_year list of lists [year, nb_of_attempts]
attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])

# 4.4 Populating attempts_per_year list
for row in prison_break_data:
    for year_attempt in attempts_per_year:
        if row[0] == year_attempt[0]:
            year_attempt[1] += 1

# 5. Counting the occurrences for each country and display it
# 5.1 Creating a list of lists countries [country, nb_of_attempts]
attempts_per_country = []
for row in prison_break_data:
    if [row[2], 0] not in attempts_per_country:
        attempts_per_country.append([row[2], 0])

# Populating attempts_per_country list
for row in prison_break_data:
    for country_attempt in attempts_per_country:
        if row[2] == country_attempt[0]:
            country_attempt[1] += 1

# Displaying attempts_per_year and attempts_per_country with barplots
barplot(attempts_per_year)
barplot(attempts_per_country)
